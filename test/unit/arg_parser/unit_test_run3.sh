#!/bin/bash
# Unit testing program for the arg_parser.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:"
python3 test/unit/arg_parser/_make_dir.py
python3 test/unit/arg_parser/arg_add_def.py
python3 test/unit/arg_parser/arg_cond_req.py
python3 test/unit/arg_parser/arg_cond_req_or.py
python3 test/unit/arg_parser/arg_default.py
python3 test/unit/arg_parser/arg_dir_chk.py
python3 test/unit/arg_parser/arg_dir_chk_crt.py
python3 test/unit/arg_parser/arg_file_chk.py
python3 test/unit/arg_parser/arg_noreq_xor.py
python3 test/unit/arg_parser/arg_parse2.py
python3 test/unit/arg_parser/arg_require.py
python3 test/unit/arg_parser/arg_req_or_lst.py
python3 test/unit/arg_parser/arg_req_xor.py
python3 test/unit/arg_parser/arg_set_path.py
python3 test/unit/arg_parser/arg_validate.py
python3 test/unit/arg_parser/arg_valid_val.py
python3 test/unit/arg_parser/arg_wildcard.py
python3 test/unit/arg_parser/arg_xor_dict.py
python3 test/unit/arg_parser/parse_multi.py
python3 test/unit/arg_parser/parse_single.py
python3 test/unit/arg_parser/file_create.py

