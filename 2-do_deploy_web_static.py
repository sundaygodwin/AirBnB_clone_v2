#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes
archive to my web servers
"""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['34.227.101.172', '54.237.100.121']


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        return False

    try:
        filename = archive_path.split("/")[-1]
        base_name = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, base_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, base_name))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, base_name))
        run('rm -rf {}{}/web_static'.format(path, base_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, base_name))
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
