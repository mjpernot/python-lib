#!/bin/bash
# Unit testing program for the arg_parser.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:"
/usr/bin/python3 ./test/unit/arg_parser/_make_dir.py
/usr/bin/python3 ./test/unit/arg_parser/arg_add_def.py
/usr/bin/python3 ./test/unit/arg_parser/arg_cond_req.py
/usr/bin/python3 ./test/unit/arg_parser/arg_cond_req_or.py
/usr/bin/python3 ./test/unit/arg_parser/arg_default.py
/usr/bin/python3 ./test/unit/arg_parser/arg_dir_chk.py
/usr/bin/python3 ./test/unit/arg_parser/arg_dir_chk_crt.py
/usr/bin/python3 ./test/unit/arg_parser/arg_file_chk.py
/usr/bin/python3 ./test/unit/arg_parser/arg_noreq_xor.py
/usr/bin/python3 ./test/unit/arg_parser/arg_parse2.py
/usr/bin/python3 ./test/unit/arg_parser/arg_require.py
/usr/bin/python3 ./test/unit/arg_parser/arg_req_or_lst.py
/usr/bin/python3 ./test/unit/arg_parser/arg_req_xor.py
/usr/bin/python3 ./test/unit/arg_parser/arg_set_path.py
/usr/bin/python3 ./test/unit/arg_parser/arg_validate.py
/usr/bin/python3 ./test/unit/arg_parser/arg_valid_val.py
/usr/bin/python3 ./test/unit/arg_parser/arg_wildcard.py
/usr/bin/python3 ./test/unit/arg_parser/arg_xor_dict.py
/usr/bin/python3 ./test/unit/arg_parser/parse_multi.py
/usr/bin/python3 ./test/unit/arg_parser/parse_single.py
/usr/bin/python3 ./test/unit/arg_parser/file_create.py

