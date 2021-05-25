#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `kiara_modules_default` package."""

import pytest  # noqa

import kiara_modules.{{ cookiecutter.project_slug }}


def test_assert():

    assert kiara_modules.{{ cookiecutter.project_slug }}.get_version() is not None
