from typing import Any
from typing import Optional
from typing import Union

import os
import sys


from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from config import project_config
SECRETS_PATH = project_config.get("pathing", "secrets_path")
RSA_KEYS_PATH = os.path.join(SECRETS_PATH, "rsa_keys")

from pkg.sig_tools import pwd


class InsecureEncrpytionOptionsError(Exception):
	pass


def save_rsa_key_pair_to_file(keyname: str, rsa_private_key: rsa.RSAPrivateKey, password: str, password_encoding: str="utf-8") -> None:
	rsa_public_key: rsa.RSAPublicKey = rsa_private_key.public_key()
	pem_public, pem_private = encode_rsa_key_pair(rsa_public_key, rsa_private_key, encryption_algorithm=serialization.BestAvailableEncryption(password.encode(encoding=password_encoding)))
	output_dir: os.PathLike = os.path.join(RSA_KEYS_PATH, keyname)
	if os.path.exists(output_dir):
		raise FileExistsError(f"Directory {output_dir} already exists.")
	os.mkdir(output_dir)

	with open(os.path.join(output_dir, f".private"), "wb") as file:
		file.write(pem_private)
	with open(os.path.join(output_dir, f".public"), "wb") as file:
		file.write(pem_public)
	

def encode_rsa_key_pair(
		public_key: rsa.RSAPublicKey, 
		private_key: rsa.RSAPrivateKey,
		encoding: serialization.Encoding=serialization.Encoding.Raw,
		public_format: serialization.PublicFormat=serialization.PublicFormat.SubjectPublicKeyInfo,
		private_format: serialization.PrivateFormat=serialization.PrivateFormat.Raw,
		encryption_algorithm: Optional[serialization.KeySerializationEncryption]=serialization.NoEncryption(),
	) -> tuple[bytes, bytes]:
	pem_private: bytes = private_key.private_bytes(
		encoding=encoding,
		format=private_format,
		encryption_algorithm=encryption_algorithm,
	)
	pem_public: bytes = public_key.public_bytes(
		encoding=encoding,
		format=public_format,
	)
	return pem_public, pem_private


def generate_rsa_key_pair(
		encryption_algorithm: Optional[Any]=serialization.BestAvailableEncryption,
		password: Optional[Union[str, bytes]]=None,
		password_encoding: str="utf-8",
		generate_password: bool=False,
		generate_password_length: int=64,
		generate_password_segments: Optional[int]=None,
		generate_password_filename: Optional[str]=None,

		key_size: int=4096,
		public_exponent: int=65537,
		
	) -> rsa.RSAPrivateKey:
	if key_size < 2048:
		raise InsecureEncrpytionOptionsError(f"The keysize of {key_size} is too small and insecure, rsa keys require a keysize must be 2048 or larger.")
	
	if generate_password:
		password = pwd.generate_random_password(length=generate_password_length, segments=generate_password_segments)
		if generate_password_filename is not None:
			password_dst: os.PathLike = pwd.save_password_to_file(password, generate_password_filename, encoding=password_encoding)
	
	#^ Encode the password if it is a string, catch the error if it is not a string or bytes and requires a password.
	encoded_password: Optional[bytes] = None
	if isinstance(password, bytes):
		encoded_password = password
	elif isinstance(password, str):
		encoded_password=password.encode(encoding=password_encoding)
	elif password is not None:
		raise TypeError("Password must be a string or bytes, unless no password is required.")
	elif encryption_algorithm is not serialization.NoEncryption:
		raise TypeError("Password must be a string or bytes, unless no password is required.")

	if encoded_password is None and encryption_algorithm is not serialization.NoEncryption:
		raise TypeError("Password must be a string or bytes, unless no password is required.")
	elif encoded_password is not None:
		encryption_algorithm = encryption_algorithm(encoded_password)

	private_key: rsa.RSAPrivateKey = rsa.generate_private_key(
		public_exponent=public_exponent,
		key_size=key_size,
	)

	return private_key