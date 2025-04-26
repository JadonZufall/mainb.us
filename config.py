import os
import sys
import configparser


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pkg"))


project_config = configparser.ConfigParser()
project_config.read(os.path.join(os.path.dirname(__file__), "config.ini"))

project_config["pathing"]["secrets_path"] = project_config["pathing"]["secrets_path"].replace("\\", os.path.sep)
project_config["pathing"]["secrets_path"] = project_config["pathing"]["secrets_path"].replace("/", os.path.sep)
project_config["pathing"]["secrets_path"] = project_config["pathing"]["secrets_path"].replace("{PROJECT_DIRECTORY}", os.path.dirname(__file__))