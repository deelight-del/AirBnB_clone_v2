#!/usr/bin/python3
""" This module contains using Fabric to compress local
files, and then later transport the given file to the server"""
from fabric.api import *
from datetime import datetime
from pathlib import Path

env.hosts = ["34.229.70.28", "54.89.45.26"]
env.exit_on_error = False


def do_pack():
    """Fab defined functions"""
    # Make versions folder for archives
    local("mkdir -p versions")
    archive_suffix = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{archive_suffix}.tgz"
    value = local(f"tar -czvf {archive_name} web_static", capture=True)
    print(value)
    if value:
        return(archive_name)
    else:
        return (None)


def do_deploy(archive_path):
    """Function to deploy the static files respectively"""
    file_path = Path(archive_path)
    file_stem = file_path.stem
    if not file_path.exists():
        return False
    # Put the file to the archive path.
    put(file_path, "/tmp")
    sudo(f"mkdir -p /data/web_static/releases/{file_stem}")
    sudo(
        f"tar -xzf /tmp/{file_stem}.tgz -C\
        /data/web_static/releases/{file_stem}"
        )
    sudo(
        f"cp -rf /data/web_static/releases/{file_stem}/web_static/*\
        /data/web_static/releases/{file_stem}"
        )
    sudo(f"rm -rf /data/web_static/releases/{file_stem}/web_static")
    sudo(f"rm -f /tmp/{file_stem}.tgz")
    sudo(f"rm -rf /data/web_static/current")
    sudo(
        f"ln -s /data/web_static/releases/{file_stem}\
        /data/web_static/current"
        )
    print("New version deployed!")
    return(True)


def deploy():
    """Fucntion to finally deploy our easter esgg"""
    archive_path = do_pack()
    if archive_path is None:
        return(False)
    value = do_deploy(archive_path)
    return(value)
