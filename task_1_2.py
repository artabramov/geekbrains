import os
import yaml


def make_dir(path: str):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception as e:
            print(e)


def make_file(filename: str):
    if not os.path.exists(filename):
        try:
            open(filename, 'w').close()
        except Exception as e:
            print(e)


def make_nodes(node, path='.'):
    if path != '.':
        make_dir(path)

    for _ in node:
        if not isinstance(_, str):
            for child in _:
                make_nodes(_[child], os.path.join(path, child))
        else:
            make_file(os.path.join(path, _))


def load_yaml(filename: str):
    try:
        with open(filename) as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(e)


# Task 1
tmp = [{
    'my_project': [{
        'settings': [],
        'mainapp': [],
        'adminapp': [],
        'authapp': [{
            'register': [],
            'login': [],
            'logout': [],
        }],
        'media': [{
            'images': [],
            'css': [],
        }],
        'trash': [],
    }],
}]
make_nodes(tmp)

# Task 2
make_nodes(load_yaml('./template.yml'))
