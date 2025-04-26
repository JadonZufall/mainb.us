import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from config import project_config

from sig_tools.pwd import generate_random_password
from sig_tools.pwd import save_password_to_file
from sig_tools.keys import generate_rsa_key_pair
from sig_tools.keys import save_rsa_key_pair_to_file

if __name__ == "__main__":
	if os.path.exists(os.path.join(os.path.join(project_config["pathing"]["secrets_path"], "passwords"), "primary_rsa_key.pwd")):
		os.remove(os.path.join(os.path.join(project_config["pathing"]["secrets_path"], "passwords"), "primary_rsa_key.pwd"))
	password = generate_random_password(length=16, segments=4)
	save_password_to_file(password, "primary_rsa_key.pwd", encoding="utf-8")
	private_key = generate_rsa_key_pair(password=password, password_encoding="utf-8", key_size=2048, public_exponent=65537)
	save_rsa_key_pair_to_file("primary_rsa_key", private_key, password=password, password_encoding="utf-8")

	