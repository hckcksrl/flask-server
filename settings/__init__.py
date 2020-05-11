import os
import json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_SETTINGS_COMMON_FILE = os.path.join(BASE_DIR, '.config/config.json')
config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())
