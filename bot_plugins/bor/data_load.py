import yaml

# 加载talk.yaml
def load_yaml():
    with open('public/resources/bor.yml', 'r', encoding='utf_8') as talk:
        result = yaml.load((talk.read()), Loader=yaml.FullLoader)
        return result