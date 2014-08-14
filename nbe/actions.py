# coding: utf-8

import click
import json
import requests
import yaml

from .utils import nbeerror


def yaml_to_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.dumps(yaml.load(f))
    except IOError:
        click.echo(nbeerror('file %s not exist.' % filename))


def register_app(name, version):
    data = {
        'name': name,
        'version': version,
        'app_yaml': yaml_to_json('app.yaml'),
        'config_yaml': yaml_to_json('config.yaml'),
    }
    r = requests.post('http://10.1.201.99:46666/app/new', data=data)
    return r.status_code == 200


def add_app(name, version, host):
    data = {
        'host': host,
    }
    r = requests.post('http://10.1.201.99:46666/app/%s/%s' % (name, version), data)
    return r.status_code == 200