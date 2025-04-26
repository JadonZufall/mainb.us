from typing import Optional

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


from config import project_config
SECRETS_PATH = project_config.get("pathing", "secrets_path")
PASSWORDS_PATH = os.path.join(SECRETS_PATH, "passwords")
if not os.path.exists(PASSWORDS_PATH):
	print("Creating passwords directory...")
	os.mkdir(PASSWORDS_PATH)

def save_password_to_file(password: str, file_name: str, encoding: str="utf-8") -> os.PathLike:
	output_fp: os.PathLike = os.path.join(PASSWORDS_PATH, file_name)
	if os.path.exists(output_fp):
		raise FileExistsError(f"File {output_fp} already exists.")
	with open(output_fp, "w", encoding=encoding) as file:
		file.write(password)
	return output_fp


def generate_random_password(length: int=64, segments: Optional[int]=None) -> str:
	if segments is not None and length % segments != 0:
		raise ValueError("Length must be divisible by segments.")
	result: str = os.urandom(length).hex()
	if segments is not None:
		result = "-".join([result[i:i+length//segments] for i in range(0, len(result), length//segments)])
	return result