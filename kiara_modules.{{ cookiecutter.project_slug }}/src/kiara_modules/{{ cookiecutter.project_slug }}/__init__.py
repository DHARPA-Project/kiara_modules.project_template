# -*- coding: utf-8 -*-

"""Top-level package for kiara_modules.{{ cookiecutter.project_slug }}."""


import logging
import os

from kiara import KiaraEntryPointItem, find_kiara_modules_under, \
    find_kiara_pipelines_under

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"

from kiara.utils.class_loading import find_metadata_schemas_under, find_value_types_under

log = logging.getLogger("kiara_modules")

modules: KiaraEntryPointItem = (find_kiara_modules_under, ["kiara_modules.{{ cookiecutter.project_slug }}"])
pipelines: KiaraEntryPointItem = (find_kiara_pipelines_under, ["kiara_modules.{{ cookiecutter.project_slug }}"])

def get_version():
    from pkg_resources import DistributionNotFound, get_distribution

    try:
        # Change here if project is renamed and does not equal the package name
        dist_name = __name__
        __version__ = get_distribution(dist_name).version
    except DistributionNotFound:

        try:
            version_file = os.path.join(os.path.dirname(__file__), "version.txt")

            if os.path.exists(version_file):
                with open(version_file, encoding="utf-8") as vf:
                    __version__ = vf.read()
            else:
                __version__ = "unknown"

        except (Exception):
            pass

        if __version__ is None:
            __version__ = "unknown"

    return __version__
