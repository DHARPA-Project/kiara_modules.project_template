# -*- coding: utf-8 -*-

"""This module contains the metadata (and other) models that are used in the ``kiara_modules.{{ cookiecutter.project_slug }}`` package.

Those models are convenience wrappers that make it easier for *kiara* to find, create, manage and version metadata -- but also
other type of models -- that is attached to data, as well as *kiara* modules.

Metadata models must be a sub-class of [kiara.metadata.MetadataModel][kiara.metadata.MetadataModel]. Other models usually
sub-class a pydantic BaseModel or implement custom base classes.
"""
from kiara import KiaraEntryPointItem
from kiara.utils.class_loading import find_kiara_models_under

value_metadata: KiaraEntryPointItem = (find_kiara_models_under, ["kiara_modules.{{ cookiecutter.project_slug }}.metadata_models"])
