# -*- coding: utf-8 -*-
from fastcodedog.generation.base.required_import import RequiredImport, Import


def test_required_import():
    assert ('from os import path as os_path' == RequiredImport().add('from os import path as os_path').serialize().strip())
    assert ('from os import path' == RequiredImport().add('from os import path').serialize().strip())
    assert ('import os' == RequiredImport().add('import os').serialize().strip())
    assert ('from os import path as os_path' == RequiredImport().add('path', 'os', 'os_path').serialize().strip())
    assert ('from os import path as os_path' == RequiredImport().add(Import('path', 'os', 'os_path')).serialize().strip())
    assert ('from os import path' == RequiredImport().add('path', 'os').serialize().strip())
    assert ('import os' == RequiredImport().add('os').serialize().strip())
    assert ('from os import path as os_path' == RequiredImport().add('path', from_='os', as_='os_path').serialize().strip())
    assert ('from os import path as os_path' == RequiredImport().add(import_='path', from_='os', as_='os_path').serialize().strip())
    assert ('from os import path as os_path, envriron' == RequiredImport()
            .add(import_='path', from_='os', as_='os_path')
            .add('envriron', 'os').serialize().strip())

def test_tmp():
    assert ('from sqlalchemy.orm import declarative_base' ==
            RequiredImport().add('from sqlalchemy.orm import declarative_base').serialize().strip())