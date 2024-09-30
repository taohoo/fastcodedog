# -*- coding: utf-8 -*-
from fastcodedog.context.context import ctx_instance
from fastcodedog.generation.api.generation import generate_api
from fastcodedog.generation.commonfiles.generation import generate_common_files
from fastcodedog.generation.crud.generation import generate_crud
from fastcodedog.generation.model.generation import generate_model
from fastcodedog.generation.schema.generation import genenrate_schema
import os
os.chdir(r'D:\workspaces\cti\review_py')
setting_file = 'docs\setting.json5'
# 使用正在开发的工程测试
# setting_file = r'D:\workspaces\tourhoo\fastcodedog2\docs\setting.json5'


def test_all():
    ctx_instance.load(setting_file)
    generate_common_files()
    generate_model()
    genenrate_schema()
    generate_crud()
    generate_api()


# def test_specific():
#     ctx_instance.load(setting_file)
#     # generate_common_files()
#     # generate_model()
#     # genenrate_schema(['Order'])
#     generate_crud(['Parameter'])
#     # generate_api()
