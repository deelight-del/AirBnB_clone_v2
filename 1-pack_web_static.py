#!/usr/bin/python3
""" This module contains using Fabric to compress local
files"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """Fab defined functions"""
    #Make versions folder for archives
    local("mkdir -p versions")
    archive_suffix = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{archive_suffix}.tgz"
    value = local(f"tar -czvf {archive_name} web_static")
    if (value == 0):
        return(archive_name)
    else:
        return (0)
