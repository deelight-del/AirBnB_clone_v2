#!/usr/bin/python3
""" This module contains using Fabric to compress local
files, and then later transport the given file to the server"""
from fabric.api import *
from datetime import datetime
from pathlib import Path

env.hosts = ["34.229.70.28", "54.89.45.26"]
env.warn_only = True


def do_pack():
    """Fab defined functions"""
    # Make versions folder for archives
    local("mkdir -p versions")
    archive_suffix = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{archive_suffix}.tgz"
    value = local(f"tar -czvf {archive_name} web_static")
    if (value == 0):
        return(archive_name)
    else:
        return (0)


def do_deploy(archive_path):
    """Function to deploy the static files respectively"""
    file_path = Path(archive_path)
    file_stem = file_path.stem
    if not file_path.exists():
        return False
    # Put the file to the archive path.
    result = put(file_path, "/tmp")
    if result.failed:
        return(False)

    result = sudo(f"mkdir -p /data/web_static/releases/{file_stem}")
    if result.failed:
        return(False)

    result = sudo(
            f"tar -xzf /tmp/{file_stem}.tgz -C \
            /data/web_static/releases/{file_stem}"
            )
    if result.failed:
        return(False)

    result = sudo(
        f"cp -rf /data/web_static/releases/{file_stem}/web_static/*\
        /data/web_static/releases/{file_stem}"
        )
    if result.failed:
        return(False)

    result = sudo(f"rm -rf /data/web_static/releases/{file_stem}/web_static")
    if result.failed:
        return(False)

    result = sudo(f"rm -f /tmp/{file_stem}.tgz")
    if result.failed:
        return(False)

    result = sudo(f"rm -rf /data/web_static/current")
    if result.failed:
        return(False)

    result = sudo(
            f"ln -s /data/web_static/releases/{file_stem}\
            /data/web_static/current"
            )
    if result.failed:
        return(False)
    print("New version deployed!")
    return True
