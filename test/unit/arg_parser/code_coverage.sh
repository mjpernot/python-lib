#!/bin/bash
# Unit test code coverage for gen_libs module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=arg_parser test/unit/arg_parser/_make_dir.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_add_def.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_cond_req.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_cond_req_or.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_default.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_dir_chk_crt.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_file_chk.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_noreq_xor.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_parse2.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_require.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_req_or_lst.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_req_xor.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_set_path.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_validate.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_valid_val.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_wildcard.py
coverage run -a --source=arg_parser test/unit/arg_parser/arg_xor_dict.py
coverage run -a --source=arg_parser test/unit/arg_parser/parse_multi.py
coverage run -a --source=arg_parser test/unit/arg_parser/parse_single.py
coverage run -a --source=arg_parser test/unit/arg_parser/file_create.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
