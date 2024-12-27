
import json

class ConfigLoader:
    @staticmethod
    def load(file_path='config/default.json'):
        try:
            with open(file_path, 'r') as file:
                config = json.load(file)
                return config
        except FileNotFoundError:
            raise Exception("Configuration file not found.")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON format in configuration file.")

    @staticmethod
    def validate(config):
        if not config.get("api_key"):
            raise Exception("API Key is missing in the configuration file.")
        return True
    