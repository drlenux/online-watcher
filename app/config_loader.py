import yaml


def load_config():
    with open('./app/config.yml', 'r') as file:
        return yaml.safe_load(file)
