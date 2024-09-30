# -*- coding: utf-8 -*-
import json5

from fastcodedog.prepare.model_and_schema_to_crud.prepare import prepare_crud
from fastcodedog.prepare.model_to_schema.prepare import prepare_schema
from fastcodedog.prepare.pdm_to_model.prepare import prepare_model
from fastcodedog.prepare.schema_and_crud_to_api.prepare import prepare_api
from fastcodedog.util.deep_update import deep_update
from fastcodedog.util.find_file import find
from fastcodedog.context.context import ctx_instance

import os
os.chdir(r'D:\workspaces\cti\review_py')
setting_file = 'docs\setting.json5'
# setting_file = r'D:\workspaces\tourhoo\fastcodedog2\docs\setting.json5'


def test_all():
    ctx_instance.load(setting_file, with_prepared_source=False)
    pre_process_scripts = {}
    for file in find('.', ctx_instance.source_directory.pre_process_scripts_file):
        pre_process_scripts = deep_update(pre_process_scripts, json5.load(open(file, 'r', encoding='utf-8')))

    prepare_model(pre_process_scripts)
    ctx_instance.load_models(ctx_instance.source_directory.model)
    prepare_schema(pre_process_scripts)
    ctx_instance.load_schemas(ctx_instance.source_directory.schema)
    prepare_crud(pre_process_scripts)
    ctx_instance.load_cruds(ctx_instance.source_directory.crud)
    prepare_api(pre_process_scripts)
    ctx_instance.load_apis(ctx_instance.source_directory.api)
