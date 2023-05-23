import yaml


def read_yaml(path: str) -> dict:

    with open(path, encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        
    return data