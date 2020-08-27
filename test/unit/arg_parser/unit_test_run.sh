#!/bin/bash
# Unit testing program for the arg_parser.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:"
test/unit/arg_parser/_make_dir.py
test/unit/arg_parser/arg_add_def.py
test/unit/arg_parser/arg_cond_req.py
test/unit/arg_parser/arg_cond_req_or.py
test/unit/arg_parser/arg_default.py
test/unit/arg_parser/arg_dir_chk_crt.py
test/unit/arg_parser/arg_file_chk.py
test/unit/arg_parser/arg_noreq_xor.py
test/unit/arg_parser/arg_parse2.py
test/unit/arg_parser/arg_require.py
test/unit/arg_parser/arg_req_or_lst.py
test/unit/arg_parser/arg_req_xor.py
test/unit/arg_parser/arg_set_path.py
test/unit/arg_parser/arg_validate.py
test/unit/arg_parser/arg_valid_val.py
test/unit/arg_parser/arg_wildcard.py
test/unit/arg_parser/arg_xor_dict.py
test/unit/arg_parser/parse_multi.py
test/unit/arg_parser/parse_single.py
test/unit/arg_parser/file_create.py

