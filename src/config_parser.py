def parse_config(raw):
    settings = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key, _, value = line.partition('=')
        settings[key] = value.strip()
    return settings


def load_file(path):
    with open(path) as f:
        return parse_config(f.read())
