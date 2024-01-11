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
    value = local(f"tar -czvf {archive_name} web_static")
    if (value == 0):
        return(archive_name)
    else:
        return (0)


def do_deploy(archive_path):
    """Function to deploy the static files respectively"""
    try:
        with open(archive_path, "rb") as f:
            pass
        archive_stem = Path(archive_path)
        archive_stem = archive_stem.stem
        put(archive_path, '/tmp/')
        # Make Folder for where to copy to
        run(f"mkdir -p /data/web_static/releases/{archive_stem}")
        sudo(
            f"tar -xzf /tmp/{archive_stem}.tgz\
            -C /data/web_static/releases/{archive_stem}"
            )
        sudo(f"rm /tmp/{archive_stem}.tgz")
        run(
            f"mv /data/web_static/releases/{archive_stem}/web_static/*\
            /data/web_static/releases/{archive_stem}"
            )
        run(
            f"rm -rf /data/web_static/releases/{archive_stem}/web_static"
            )
        run("rm -rf /data/web_static/current")
        run(
            f"ln -s /data/web_static/releases/{archive_stem}\
            /data/web_static/current"
            )
        return (True)
    except (FileNotFoundError, SystemExit):
        return False
