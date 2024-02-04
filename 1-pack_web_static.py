#!/usr/bin/python3
"""
Fabric script to genereate tgz archive and
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import local, env
from fabric.context_managers import lcd


env.hosts = ['34.227.101.172', '54.237.100.121']


def do_pack():
    """
    Making an archive of the web_static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.tgz'
    local('mkdir -p versions')

    with lcd('versions'):
        result = local('tar -cvzf {} ../web_static'.format(archive))

    if result.succeeded:
        return 'versions/{}'.format(archive)
    else:
        return None
