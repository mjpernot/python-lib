# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [2.6.0] - 2018-09-13
### Removed
- gen_libs.Close_File:  Function was previously deprecated.
- gen_libs.Chk_Crt_File:  Function was previously deprecated.
- gen_libs.Chk_Crt_Dir:  Function was previously deprecated.
- cmds_gen.Add_Cmd:  Function was previously deprecated.
- cmds_gen.Is_Add_Cmd:  Function was previously deprecated.
- cmds_gen.Disconnect:  Function was previously deprecated.
- arg_parser.Arg_Set_Path:  Function was previously deprecated.


## [2.5.0] - 2018-09-10
### Updated
- arg_parser.arg_parse2:  Replaced "gen_libs.Chk_Int" with "gen_libs.chk_int" call.
- system.FGraph.__init__:  Replaced "gen_libs.file_search" with "gen_libs.file_search".
- gen_libs.file_search:  Refactored the code in the function.
- gen_libs.file_2_list:  Remove any newlines from the end of each line.
- test/unit/gen_libs/chk_crt_dir.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_libs/write_file.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_libs/no_std_out.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_libs/month_delta.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_libs/merge_two_dicts.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_libs/merge_data_types.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_libs/get_data.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_libs/get_base_dir.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_libs/file_search_cnt.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_libs/display_data.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_libs/data_multi_out.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_libs/data_multi_out.py:  Added new test to check JSON conversion to write to file.
- test/unit/gen_libs/clear_file.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_libs/chk_crt_file.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_class/Yum_init.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_class/Yum_get_release.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_class/Yum_get_os.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_class/Yum_get_distro.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_class/SingleInstanceException.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_class/ProgressBar_update.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_class/ProgressBar_init.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_class/ProgressBar_calc_and_update.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_class/ProgramLock_init.py:  Updated to use unittest2 under Python 2.7.
- test/unit/gen_class/ProgramLock_del.py:  Updated to use unittest2 under Python 2.7.

### Fixed
- gen_libs.data_multi_out:  If requesting JSON, but unable to convert, do not write to file.
- gen_libs.chk_crt_file:  Replaced "open" with "touch" call to create any missing path directories.
- gen_libs.file_2_list:  Removed "close" as it is incorrect.
- gen_libs.chk_crt_file:  Added "close" file command for the no_print option.

### Added
- gen_libs.cp_file:  Copies a file from source directory to destination directory with exception handling.
- gen_libs.list_dirs:  Returns a list of directories within a directory.
- gen_libs.touch:  Implements the Linux "touch" command.
- gen_libs.is_empty_file:  Checks if a file is empty.
- test/unit/gen_libs/code_coverage.sh: Code coverage run program.
- test/unit/gen_class/code_coverage.sh: Code coverage run program.
- test/unit/gen_libs/cp_file.py:  Unit test for gen_libs.cp_file function.
- test/unit/gen_libs/list_dirs.py:  Unit test for gen_libs.list_dirs function.
- test/unit/gen_libs/touch.py:  Unit test for gen_libs.touch function.
- test/unit/gen_libs/is_empty_file.py:  Unit test for gen_libs.is_empty_file function.
- test/unit/gen_libs/file_search.py:  Unit test for gen_libs.file_search function.
- test/unit/gen_libs/file_2_list.py:  Unit test for gen_libs.file_2_list function.

### Remove
- gen_libs.Milli_2_Readadble:  Function was previously deprecated.
- gen_libs.File_Search:  Function was previously deprecated.
- gen_libs.Chk_Int:  Function was previously deprecated.
- arg_parser.Arg_Wildcard:  Function was previously deprecated.
- arg_parser.Arg_Add_Def:  Function was previously deprecated.
- arg_parser.Arg_Valid_Val:  Function was previously deprecated.
- arg_parser.Arg_Default:  Function was previously deprecated.
- arg_parser.Arg_Parse2:  Function was previously deprecated.
- arg_parser.Arg_Xor_Dict:  Function was previously deprecated.
- arg_parser.Arg_Validate:  Function was previously deprecated.
- arg_parser.Arg_Cond_Req:  Function was previously deprecated.
- arg_parser.Arg_Cond_Req_Or:  Function was previously deprecated.
- arg_parser.Arg_Req_Or_Lst:  Function was previously deprecated.
- arg_parser.Arg_NoReq_Xor:  Function was previously deprecated.
- arg_parser.Arg_Req_Xor:  Function was previously deprecated.
- arg_parser.Arg_Dir_Chk_Crt:  Function was previously deprecated.
- arg_parser.Arg_File_Chk:  Function was previously deprecated.
- arg_parser.Arg_Parse:  Function was previously deprecated.
- arg_parser.Arg_Require:  Function was previously deprecated.
- system.Yum:  Class was previously deprecated.
- system.F_Graph:  Class was previously deprecated.
- system.Mail:  Class was previously deprecated.
- cmds_gen.Run_Prog:  Function was previously deprecated.
- cmds_gen.Create_Cfg_Array:  Function was previously deprecated.
- gen_libs.Validate_Int:  Function was previously deprecated.
- gen_libs.Validate_Date:  Function was previously deprecated.
- gen_libs.Str_2_Type:  Function was previously deprecated.
- gen_libs.Str_2_List:  Function was previously deprecated.
- gen_libs.Help_Func:  Function was previously deprecated.
- gen_libs.Rm_Newline_List:  Function was previously deprecated.
- gen_libs.Rm_File:  Function was previously deprecated.
- gen_libs.Rm_Dup_List:  Function was previously deprecated.
- gen_libs.Rotate_Files:  Function was previously deprecated.
- gen_libs.Root_Run:  Function was previously deprecated.
- gen_libs.Normalize:  Function was previously deprecated.
- gen_libs.Make_Zip:  Function was previously deprecated.
- gen_libs.List_Files:  Function was previously deprecated.
- gen_libs.List_2_Dict:  Function was previously deprecated.
- gen_libs.Key_Cleaner:  Function was previously deprecated.
- gen_libs.Is_True:  Function was previously deprecated.
- gen_libs.Is_Missing_Lists:  Function was previously deprecated.
- gen_libs.Not_In_List:  Function was previously deprecated.
- gen_libs.In_List:  Function was previously deprecated.
- gen_libs.Get_Time:  Function was previously deprecated.
- gen_libs.Get_Secs:  Function was previously deprecated.
- gen_libs.Get_Date:  Function was previously deprecated.
- gen_libs.Float_Div:  Function was previously deprecated.
- gen_libs.Pct_Int:  Function was previously deprecated.
- gen_libs.File_Cleanup:  Function was previously deprecated.
- gen_libs.Disk_Usage:  Function was previously deprecated.
- gen_libs.Dir_File_Match:  Function was previously deprecated.
- gen_libs.Prt_Dict:  Function was previously deprecated.
- gen_libs.Dict_2_Std:  Function was previously deprecated.
- gen_libs.Print_Dict:  Function was previously deprecated.
- gen_libs.Dict_2_List:  Function was previously deprecated.
- gen_libs.Del_Not_In_List:  Function was previously deprecated.
- gen_libs.Del_Not_And_List:  Function was previously deprecated.
- gen_libs.Crt_File_Time:  Function was previously deprecated.
- gen_libs.Write_File2:  Function was previously deprecated.
- gen_libs.Make_MD5_Hash:  Function was previously deprecated.
- gen_libs.Write_2_Log:  Function was previously deprecated.
- gen_libs.Rename_File:  Function was previously deprecated.
- gen_libs.Rename_File2:  Function was previously deprecated.
- gen_libs.Mv_File2:  Function was previously deprecated.
- gen_libs.Mv_File:  Function was previously deprecated.
- gen_libs.Cp_File:  Function was previously deprecated.
- gen_libs.Cp_File2:  Function was previously deprecated.
- gen_libs.Copy_Tree:  Function was previously deprecated.
- gen_libs.Compress:  Function was previously deprecated.
- gen_libs.File_2_List:  Function was previously deprecated.
- gen_libs.Chmod:  Function was previously deprecated.
- gen_libs.Bytes_2_Readable:  Function was previously deprecated.
- gen_libs.And_Is_True:  Function was previously deprecated.
- gen_libs.Merge_2_Dicts:  Function was previously deprecated.
- gen_libs.Display_Data:  Function was previously deprecated.
- gen_libs.Empty_File:  Function was previously deprecated.
- gen_libs.Chown:  Function was previously deprecated.


## [2.4.0] - 2018-05-28
### Changed
- gen_class.Yum.__init__:  Added self.distro attribute to class.
- test/unit/gen_class/Yum_init.py:  Updated with platform.linux_distribution attribute.
- test/unit/gen_class/Yum_get_release.py:  Updated with platform.linux_distribution attribute.
- test/unit/gen_class/Yum_get_os.py:  Updated with platform.linux_distribution attribute.
- requirements.txt:  Removed psutil as not required.

### Added
- gen_class.Yum.get_disto:  Method - Return class linux_distribution.
- test/unit/gen_class/Yum_get_distro.py:  Test returning Linux distribution data.

### Removed
- gen_class.Program_Lock:  Removed class and associated methods.
- gen_class.Single_Instance_Exception:  Removed class and associated methods.


## [2.3.0] - 2018-05-25
### Added
- gen_libs.mv_file2:  Move a file from current location to a new location.


## [2.2.1] - 2018-05-21
### Fixed
- gen_class.Daemon.start:  Fixed message variable format.


## [2.2.0] - 2018-04-06
### Added
- gen_libs.milli_2_readadble:  Replaces Milli_2_Readadble function.

### Deprecated
- gen_libs.Milli_2_Readadble:  Replace by milli_2_readadble function.


## [2.1.0] - 2018-04-04
### Added
- gen_class.Yum.get_os:  Return the class OS platform.
- gen_class.Yum.get_release:  Return the class OS release version.
- test/unit/gen_class/Yum_init.py:  Unit test of gen_class.Yum.__init__ method.
- test/unit/gen_class/Yum_get_os.py:  Unit test of gen_class.Yum.get_os method.
- test/unit/gen_class/Yum_get_release.py:  Unit test of gen_class.Yum.get_release method.

### Changed
- gen_class.Yum.__init__:  Added new attributes for OS version information.

### Removed
- gen_class.Progress_Bar:  Been replaced by ProgressBar class.


## [2.0.0] - 2018-04-02
Breaking Change

### Added
- gen_libs.validate_int:  Replaced Validate_Int function.
- gen_libs.validate_date:  Replaced Validate_Date function.
- gen_libs.str_2_type:  Replaced Str_2_Type function.
- gen_libs.str_2_list:  Replaced Str_2_List function.
- gen_libs.load_module:  Replaced Load_Module function.
- gen_libs.help_func:  Replaced Help_Func function.
- gen_libs.rm_newline_list:  Replaced Rm_Newline_List function.
- gen_libs.rm_file:  Replaced Rm_File function.
- gen_libs.rm_dup_list:  Replaced Rm_Dup_List function.
- gen_libs.rotate_files:  Replaced Rotate_Files function.
- gen_libs.root_run:  Replaced Root_Run function.
- gen_libs.prt_msg:  Replaced Prt_Msg function.
- gen_libs.prt_lvl:  Replaced Prt_Lvl function.
- gen_libs.not_in_list:  Replaced Not_In_List function.
- gen_libs.normalize:  Replaced Normalize function.
- gen_libs.make_zip:  Replaced Make_Zip function.
- gen_libs.list_filter_files:  Replaced List_Filter_Files function.
- gen_libs.list_files:  Replaced List_Files function.
- gen_libs.list_2_dict:  Replaced List_2_Dict function.
- gen_libs.key_cleaner:  Replaced Key_Cleaner function.
- gen_libs.is_true:  Replaced Is_True function.
- gen_libs.is_missing_list:  Replaced Is_Missing_List function.
- gen_libs.in_list:  Replaced In_List function.
- gen_libs.get_time:  Replaced Get_Time function.
- gen_libs.get_secs:  Replaced Get_Secs function.
- gen_libs.get_date:  Replaced Get_Date function.
- gen_libs.pct_int:  Replaced Pct_Int function.
- gen_libs.float_div:  Replaced Float_Div function.
- gen_libs.file_cleanup:  Replaced File_Cleanup function.
- gen_libs.disk_usage:  Replaced Disk_Usage function.
- gen_libs.dir_file_match:  Replaced Dir_File_Match function.
- gen_libs.print_dict:  Replaced Print_Dict function.
- gen_libs.print_data:  Replaced Print_Data function.
- gen_libs.prt_dict:  Replaced Prt_Dict function.
- gen_libs.dict_2_std:  Replaced Dict_2_Std function.
- gen_libs.dict_2_list:  Replaced Dict_2_List function.
- gen_libs.del_not_in_list:  Replaced Del_Not_In_List function.
- gen_libs.del_not_and_list:  Replaced Del_Not_And_List function.
- gen_libs.crt_file_time:  Replaced Crt_File_Time function.
- gen_libs.make_md5_hash:  Replaced Make_MD5_Hash function.
- gen_libs.write_to_log:  Replaced Write_To_Log function.
- gen_libs.write_file2:  Replaced Write_File function.
- gen_libs.rename_file:  Replaced Rename_File2 function.
- gen_libs.mv_file:  Replaced Mv_File function.
- gen_libs.cp_file2:  Replaced Cp_File2 function.
- gen_libs.copy_tree:  Replaced Copy_Tree function.
- gen_libs.compress:  Replaced Compress function.
- gen_libs.file_2_list:  Replaced File_2_List function.
- gen_libs.file_search:  Replaced File_Search function.
- gen_libs.chk_int:  Replaced Chk_Int function.
- gen_libs.bytes_2_readable:  Replaced Bytes_2_Readable function.
- gen_libs.and_is_true:  Replaced And_Is_True function.
- arg_parser.arg_wildcard:  Replaced Arg_Wildcard function.
- arg_parser.arg_add_def:  Replaced Arg_Add_Def function.
- arg_parser.arg_valid_val:  Replaced Arg_Valid_Val function.
- arg_parser.arg_parse2:  Replaced Arg_Parse2 function.
- arg_parser.arg_default:  Replaced Arg_Default function.
- arg_parser.arg_xor_dict:  Replaced Arg_Xor_Dict function.
- arg_parser.arg_validate:  Replaced Arg_Validate function.
- arg_parser.arg_cond_req_or:  Replaced Arg_Cond_Req_Or function.
- arg_parser.arg_req_or_lst:  Replaced Arg_Req_Or_Lst function.
- arg_parser.arg_cond_req:  Replaced Arg_Cond_Req function.
- arg_parser.arg_noreq_xor:  Replaced Arg_NoReq_Xor function.
- arg_parser.arg_req_xor:  Replaced Arg_Req_Xor function.
- arg_parser.arg_set_path:  Replaced Arg_Set_Path function.
- arg_parser.arg_dir_chk_crt:  Replaced Arg_Dir_Chk_Crt function.
- arg_parser.arg_file_chk:  Replaced Arg_File_Chk function.
- arg_parser.arg_require:  Replaced Arg_Require function.
- gen_class.Yum:  Replaced system.Yum class.
- system.FGraph:  Replaced F_Graph class.
- cmds_gen.run_prog:  Replaced Run_Prog function.
- cmds_gen.add_cmd:  Replaced Add_Cmd function.
- cmds_gen.create_cfg_array:  Replaces Create_Cfg_Array function.
- cmds_gen.disconnect:  Replaces Disconnect function.
- cmds_gen.is_add_cmd:  Replaces Is_Add_Cmd function.

### Changed
- gen_list.prt_msg:  Changed Prt_Lvl to prt_lvl call.
- gen_list.dir_file_match:  Changed List_Files to list_files call.
- gen_list.write_to_log:  Changed Get_Time to get_time call.
- gen_list.write_to_log:  Changed Get_Date to get_date call.
- gen_list.pct_int:  Changed Float_Div to float_div call.
- gen_list.print_dict:  Changed Print_Data to print_data and Dict_2_Std to dict_2_std calls.
- gen_list.dict_2_std:  Changed Prt_Dict to prt_dict call.
- gen_libs.make_md5_hash:  Changed Write_File2 to write_file call.
- gen_libs.write_to_log:  Changed Write_File to write_file2 call.
- gen_libs.Load_Module:  Qualified all calls using sys module.
- gen_libs.file_2_list:  Replaced Close_File call with close command.
- gen_libs.file_search:  Replaced Close_File call with close command.
- gen_libs.file_search:  Replaced Open_File call with open command.
- gen_libs.py:  Changed "from subprocess" to "import subprocess".
- gen_libs.py:  Qualified all calls to functions in subprocess module.
- arg_parser.py:  Setup single-source version control.
- arg_parser.py:  Made program PEP-8 compliant.
- test/unit/gen_class/SingleInstanceException.py:  Made program PEP-8 compliant.
- test/unit/gen_class/ProgressBar_update.py:  Made program PEP-8 compliant.
- test/unit/gen_class/ProgressBar_init.py:  Made program PEP-8 compliant.
- test/unit/gen_class/ProgressBar_calc_and_update.py:  Made program PEP-8 compliant.
- test/unit/gen_class/ProgramLock_init.py:  Made program PEP-8 compliant.
- test/unit/gen_class/ProgramLock_del.py:  Made program PEP-8 compliant.
- gen_class.py:  Made program PEP-8 compliant.
- system.py:  Setup single-source version control.
- system.py:  Made program PEP-8 compliant.
- cmds_gen.is_add_cmd:  Replaced Add_Cmd with add_cmd function call.
- cmds_gen.py:  Setup single-source version control.
- cmds_gen.py:  Made program PEP-8 compliant.
- machine.py:  Setup single-source version control.
- machine.py:  Made program PEP-8 compliant.
- errors.py:  Setup single-source version control.
- errors.py:  Made program PEP-8 compliant.

### Deprecated
- gen_libs.Validate_Int:  Replaced by validate_int function.
- gen_libs.Validate_Date:  Replaced by validate_date function.
- gen_libs.Str_2_Type:  Replaced by str_2_type function.
- gen_libs.Str_2_List:  Replaced by str_2_list function.
- gen_libs.Load_Module:  Replaced by load_module function.
- gen_libs.Help_Func:  Replaced by help_func function.
- gen_libs.Rm_Newline_List:  Replaced by rm_newline_list function.
- gen_libs.Rm_File:  Replaced by rm_file function.
- gen_libs.Rm_Dup_List:  Replaced by rm_dup_list function.
- gen_libs.Rotate_Run:  Replaced by rotate_run function.
- gen_libs.Root_Run:  Replaced by root_run function.
- gen_libs.Prt_Msg:  Replaced by prt_msg function.
- gen_libs.Prt_Lvl:  Replaced by prt_lvl function.
- gen_libs.Not_In_List:  Replaced by not_in_list function.
- gen_libs.Normalize:  Replaced by normalize function.
- gen_libs.Make_Zip:  Replaced by make_zip function.
- gen_libs.List_Filter_Files:  Replaced by list_filter_files function.
- gen_libs.List_Files:  Replaced by list_files function.
- gen_libs.List_2_Dict:  Replaced by list_2_dict function.
- gen_libs.Key_Cleaner:  Replaced by key_cleaner function.
- gen_libs.Is_True:  Replaced by is_true function.
- gen_libs.Is_Missing_List:  Replaced by is_missing_list function.
- gen_libs.In_List:  Replaced by in_list function.
- gen_libs.Get_Time:  Replaced by get_time function.
- gen_libs.Get_Secs:  Replaced by get_secs function.
- gen_libs.Get_Date:  Replaced by get_date function.
- gen_libs.Pct_Int:  Replaced by pct_int function.
- gen_libs.Float_Div:  Replaced by float_div function.
- gen_libs.File_Cleanup:  Replaced by file_cleanup function.
- gen_libs.Disk_Usage:  Replaced by disk_usage function.
- gen_libs.Dir_File_Match:  Replaced by dir_file_match function.
- gen_libs.Print_Dict:  Replaced by print_dict function.
- gen_libs.Print_Data:  Replaced by print_data function.
- gen_libs.Prt_Dict:  Replaced by prt_dict function.
- gen_libs.Dict_2_Std:  Replaced by dict_2_std function.
- gen_libs.Dict_2_List:  Replaced by dict_2_list function.
- gen_libs.Del_Not_In_List:  Replaced del_not_in_list function.
- gen_libs.Del_Not_And_List:  Replaced del_not_and_list function.
- gen_libs.Crt_File_Time:  Replaced crt_file_time function.
- gen_libs.Make_MD5_Hash:  Replaced by make_md5_hash function.
- gen_libs.Write_To_Log:  Replaced by write_to_log function.
- gen_libs.Write_File:  Replaced by write_file2 function.
- gen_libs.Rename_File:  Replaced by rename_file function.
- gen_libs.Rename_File2:  Replaced by rename_file function.
- gen_libs.Mv_File2:  Replaced mv_file function.
- gen_libs.Mv_File:  Replaced mv_file function.
- gen_libs.Cp_File2:  Replaced by cp_file2 function.
- gen_libs.Cp_File:  Replaced by cp_file2 function.
- gen_libs.Copy_Tree:  Replaced by copy_tree function.
- gen_libs.Compress:  Replaced by compress function.
- gen_libs.Open_File:  No longer required.
- gen_libs.Close_File:  No longer required.
- gen_libs.File_2_List:  Replaced by file_2_list function.
- gen_libs.File_Search:  Replaced by file_search function.
- gen_libs.Chown:  No longer required.
- gen_libs.Chmod:  No longer required.
- gen_libs.Chk_Int:  Replaced by chk_int function.
- gen_libs.Bytes_2_Readable:  Replaced by bytes_2_readable function.
- gen_libs.And_Is_True:  Replaced by and_is_true function.
- arg_parser.Arg_Wildcard:  Replaced by arg_wildcard function.
- arg_parser.Arg_Add_Def:  Replaced by arg_add_def function.
- arg_parser.Arg_Valid_Val:  Replaced by arg_valid_val function.
- arg_parser.Arg_Parse2:  Replaced by arg_parse2 function.
- arg_parser.Arg_Default:  Replaced by arg_default function.
- arg_parser.Arg_Xor_Dict:  Replaced by arg_xor_dict function.
- arg_parser.Arg_Validate:  Replaced by arg_validate function.
- arg_parser.Arg_Cond_Req_Or:  Replaced by arg_cond_req_or function.
- arg_parser.Arg_Req_Or_Lst:  Replaced by arg_req_or_lst function.
- arg_parser.Arg_Cond_Req:  Replaced by arg_cond_req function.
- arg_parser.Arg_NoReq_Xor:  Replaced by arg_noreq_xor function.
- arg_parser.Arg_Set_Path:  Replaced by arg_set_path function.
- arg_parser.Arg_Req_Xor:  Replaced by arg_req_xor function.
- arg_parser.Arg_Dir_Chk_Crt:  Replaced by arg_dir_chk_crt function.
- arg_parser.Arg_File_Chk:  Replaced by arg_file_chk function.
- arg_parser.Arg_Require:  Replaced by arg_require function.
- arg_parser.Arg_Parse:  Replaced by arg_parse2 function.
- system.Yum: Replaced by gen_class.Yum class.
- system.F_Graph:  Replaced by FGraph class.
- system.Mail:  Replaced by gen_class.Mail class.
- cmds_gen.Run_Prog:  Replaced by run_prog function.
- cmds_gen.Add_Cmd:  Replaced by add_cmd function.
- cmds_gen.Is_Add_Cmd:  Replaced by is_add_cmd function.
- cmds_gen.Disconnect:  Replaced by disconnect function.
- cmds_gen.Create_Cfg_Array:  Replaced by create_cfg_array function.

### Removed
- gen_libs.py:  Removed "from sys import *", already have "import sys" in place.


## [1.36.0] - 2018-03-09
### Added
- gen_libs.data_multi_out:  Send data to multiple outputs options.
- test/unit/gen_libs/data_multi_out.py:  Unit testing of data_multi_out function.


## [1.35.1] - 2018-02-15
### Fixed
- gen_class.Daemon.start:  File handler had incorrect name.


## [1.35.0] - 2018-02-13
### Added
- gen_class.Daemon:  Added class to run a program as a daemon/service.


## [1.34.0] - 2018-02-09
### Added
- gen_libs.chk_crt_dir:  Check directory permission and create directory if requested.
- gen_libs.chk_crt_file:  Check file permission and create file if requested.
- test/unit/gen_libs/chk_crt_dir.py:  Unit testing of chk_crt_dir function.
- test/unit/gen_libs/chk_crt_file.py:  Unit testing of chk_crt_file function.

### Changed
- gen_libs.py:  Setup single-source version control.

### Deprecated
- gen_libs.Chk_Crt_Dir:  Replaced by gen_libs.chk_crt_dir.
- gen_libs.Chk_Crt_File:  Replaced by gen_libs.chk_crt_file.


## [1.33.2] - 2018-01-26
### Fixed
- Error:  Pip is unable to install/upgrade the python-lib package.
- setup.py:  Removed encoding option from the open command reading a file.
- setup.py:  Removed install_requires setting as it errors out during pip installs.


## [1.33.1] - 2018-01-25
### Added
- test/unit/gen_class/SingleInstanceException.py:  Unit test of SingleInstanceException class.
- test/unit/gen_class/ProgramLock_init.py:  Unit test of ProgramLock.__init__ method.
- test/unit/gen_class/ProgramLock_del.py:  Unit test of ProgramLock.__del__ method.

### Changed
- gen_class/ProgressBar_calc_and_update.py:  Changed format of mock.patch statements.


## [1.33.0] - 2018-01-22
### Added
- gen_class.ProgressBar: Displays and updates a progress bar for an ongoing operation.
- gen_class.SingleInstanceException:  Class exception for the ProgramLock class.
- gen_class.ProgramLock:  Creates a file lock instance for a program.
- gen_class.System:  Class which is a representation of a Linux server.
- gen_class.Mail:  Class which is a representation of an email.
- test/unit/gen_class/ProgressBar_init.py:  Unit test of ProgressBar.__init__ method.
- test/unit/gen_class/ProgressBar_update.py:  Unit test of ProgressBar.update method.
- test/unit/gen_class/ProgressBar_calc_and_update.py:  Unit test of ProgressBar.calc_and_update method.

### Changed
- gen_class.py:  Moved internal version control to CHANGELOG file.
- gen_class.py:  Made program PEP-8 compliant.
- gen_class.py:  Setup single-source version control.

### Deprecated
- gen_class.Progress_Bar:  Replaced by gen_class.ProgressBar.
- gen_class.Single_Instance_Exception:  Replaced by gen_class.SingleInstanceException.
- gen_class.Program_Lock:  Replaced by gen_class.ProgramLock.


## [1.32.0] - 2018-01-18
### Added
- gen_libs.write_file:  Write/append data to a file.
- gen_libs.display_data:  Print dictionary in readable format.
- gen_libs.get_data:  Read a file into a list.
- gen_libs.clear_file:  Clear contents of an existing file.
- test/unit/gen_libs/write_file.py:  Unit testing of write_file function.
- test/unit/gen_libs/display_data.py:  Unit testing of display_data function.
- test/unit/gen_libs/get_data.py:  Unit testing of get_data function.
- test/unit/gen_libs/clear_file.py:  Unit testing of clear_file function.

### Changed
- gen_libs:  Updated to be PEP-8 compliant.  Ignored E722 in gen_libs.Chk_Crt_Dir function
- gen_libs.get_base_dir:  Added **kwargs to argument list for future use.
- test/unit/gen_libs/month_delta.py:  Updated to be PEP-8 compliant.
- test/unit/gen_libs/file_search_cnt.py:  Updated to be PEP-8 compliant.
- test/unit/gen_libs/merge_two_dicts.py:  Updated to be PEP-8 compliant.
- test/unit/gen_libs/merge_data_types.py:  Updated to be PEP-8 compliant.
- test/unit/gen_libs/no_std_out.py:  Updated to be PEP-8 compliant.

### Deprecated
- gen_libs.Write_File2:  Replaced by gen_libs.write_file.
- gen_libs.Display_Data:  Replace by gen_libs.display_data.
- gen_libs.Empty_file:  Replaced by gen_libs.clear_file.

 
## [1.31.0] - 2018-01-12
### Added
- gen_libs.merge_data_types:  Merge two similar data types (e.g. string, dictionary, list, tuple).
- gen_libs.merge_two_dicts:  Merge two dictionaries.
- gen_libs.no_std_out:  Suppresses standard output of a function.
- test/unit/gen_libs/merge_data_types.py:  Unit testing of merge_data_types function.
- test/unit/gen_libs/merge_two_dicts.py:  Unit testing of merge_two_dicts function.
- test/unit/gen_libs/no_std_out.py:  Unit testing of no_std_out function.

### Deprecated
- gen_libs.Merge_2_Dicts:  Replaced by gen_libs.merge_two_dicts.


## [1.30.0] - 2017-12-22
### Added
- gen_libs.month_delta:  Produces a month delta based on date passed to function.
- gen_libs.file_search_cnt:  Find number of lines in a file that match a pattern.
- gen_libs.get_base_dir:  Return the base directory path of the file name.
- test/unit/gen_libs/month_delta.py:  Unit testing of month_delta function.
- test/unit/gen_libs/file_search_cnt.py:  Unit testing of file_search_cnt function.
- test/unit/gen_libs/get_base_dir.py: Unit testing of get_base_dir function.
- test/unit/gen_libs/unit_test_run.sh:  Full unit testing of gen_libs module.


## [1.29.1] - 2017-12-13
### Added
- version.py:  Created single-source version control program.
- setup.py:  To allow Python general libraries to be installed via pip.


## [1.29.0] - 2017-10-06
### Added
- gen_libs._ntuple_diskusage
- gen_libs.Disk_Usage


## [1.28.1] - 2017-09-26
### Error
- gen_libs.Make_MD5_Hash:  Is overwriting hash files if file names are same, but extensions are different.

### Fixed
- gen_libs.Make_MD5_Hash:  Retain extension in hash file name to prevent overwriting.


## [1.28.0] - 2017-09-22
### Added
- gen_libs.Merge_2_Dicts


## [1.27.0] - 2017-09-20
### Added
- gen_libs.Bytes_2_Readable
- gen_libs.Milli_2_Readadble

### Changed
- arg_parser.Arg_Parse2:  Add ability for an option to have 0 or 1 value and add named argument opt_val to function.


## [1.26.0] - 2017-08-28
### Added
- gen_libs.Display_Data


## [1.25.0] - 2017-08-24
### Added
- gen_libs.Empty_File

### Removed
- gen_libs.normalize


## [1.24.0] - 2017-08-15
### Removed
- gen_libs.Dict_Out
- gen_libs:  Removed references to cmds_mongo library.


## [1.23.0] - 2017-08-14
### Added
- gen_libs.Print_Dict

### Changed
- system.py:  Convert comments/documentation to docstrings.
- system.py:  Change order of library sequence to be PEP-8 compliant.
- system.py:  Change versioning information to be PEP-440 compliant.
- system.py:  Add classification line for Sunspear use.
- system.py:  Change single quotes to double quotes to be PEP-8 compliant.

### Deprecated
- gen_libs.Dict_Out

## Removed
- gen_libs: Dependency of the cmds_mongo library.


## [1.22.0] - 2017-08-03
### Changed
- arg_parser.py:  Convert comments/documentation to docstrings.
- arg_parser.py:  Change order of library sequence to be PEP-8 compliant.
- arg_parser.py:  Change versioning information to be PEP-440 compliant.
- arg_parser.py:  Add classification line for Sunspear use.
- arg_parser.py:  Change single quotes to double quotes to be PEP-8 compliant.
- arg_parser.py:  Convert comments/documentation to docstrings.
- cmds_gen.py:  Change order of library sequence to be PEP-8 compliant.
- cmds_gen.py:  Change versioning information to be PEP-440 compliant.
- cmds_gen.py:  Add classification line for Sunspear use.
- cmds_gen.py:  Change single quotes to double quotes to be PEP-8 compliant.
- machine.py:  Convert comments/documentation to docstrings.
- machine.py:  Change order of library sequence to be PEP-8 compliant.
- machine.py:  Change versioning information to be PEP-440 compliant.
- machine.py:  Add classification line for Sunspear use.
- errors.py:  Convert comments/documentation to docstrings.
- errors.py:  Change order of library sequence to be PEP-8 compliant.
- errors.py:  Change versioning information to be PEP-440 compliant.
- errors.py:  Add classification line for Sunspear use.
- errors.Error:  Remove version information and replaced with pass.
- gen_libs:  Convert comments/documentation to docstrings.
- gen_libs:  Change order of library sequence to be PEP-8 compliant.
- gen_libs:  Change versioning information to be PEP-440 compliant.
- gen_libs:  Change single quotes to double quotes to be PEP-8 compliant.
- gen_libs.Help_Func:  Change verion print command to be PEP-440 compliant.

### Removed
- cmds_gen.Key_Cleaner:  Moved to gen_libs.py module.


## [1.21.5] - 2017-08-03
### Error
- gen_libs:  List_Files function listed twice.

### Fixed
- gen_libs:  Rename List_Files created on 2017-07-17 to List_Filter_Files.


## [1.21.4] - 2017-08-02
### Changed
- gen_class.py:  Made program PEP-440 and PEP-8 compliant and added classification line.
- gen_class.py:  Converted comments and documentation to docstrings.


## [1.21.3] - 2017-07-21
### Added
- gen_class.Logger:  To log messages to a file using a standard formatting.


## [1.21.2] - 2017-07-20
### Fixed
- gen_libs:  Corrected incorrect documentation dates.


## [1.21.1] - 2017-07-20
### Fixed
- gen_libs.Rm_File: Correct error on setting err_flag in exception.


## [1.21.0] - 2017-07-17
### Added
- gen_libs.Make_Zip
- gen_libs.List_Files
- gen_libs.Make_MD5_Hash
- gen_libs.Rm_File
- gen_libs.Mv_File2


## [1.20.0] - 2017-07-17
### Changed
- gen_libs.Write_To_Log:  Changed format of output to include ZULU time symbol.


## [1.19.0] - 2017-06-30
### Added
- gen_libs.Get_Date
- gen_libs.Get_Time
- gen_libs.Write_To_Log


## [1.18.0] - 2017-06-26
### Added
- gen_libs.Normalize
- gen_libs.Key_Cleaner

### Changed
- gen_libs:  Change to meet Python PEP 257 requirement - using docstrings to display programs usage/help message.
- gen_libs:  Change to meet Python PEP 8 requirement - import library order of sequence.
- gen_libs:  Import Library section:  Change import order sequence.
- gen_libs:  Add classification line for Sunspear use.
- gen_libs:  Standardize function naming convention.
- gen_libs.Help_Func:  Call func_name to print programs docstring.

### Deprecated
- gen_libs.normalize


## [1.17.1] - 2017-04-25
### Added
- gen_class.Program_Lock:  Allow a program to create a lock instance of the program.
-   This will allow other programs to know if an instance of the program is running.
- gen_class.Single_Instance_Exception:  Class exception for the Program_Lock class.
-   Used when an instance lock has been detected.


## [1.17.0] - 2017-04-07
### Added
- gen_libs.Dir_File_Match
- gen_libs.re library

### Changed
- gen_libs.Is_Missing_Lists:  Rewrote the function to use a list comphrension loop.


## [1.16.1] - 2017-03-14
### Added
- gen_class.py:  Class that has class definitions for general use.


## [1.16.1] - 2017-01-20
### Fixed
- cmds_gen.Is_Add_Cmd:  Added check to see if args_array[x] is of type boolean.


## [1.16.0] - 2017-01-03
### Added
- gen_libs.normalize

### Fixed
- arg_parser.Arg_Parse2:  Change from String type to Boolean type.
- arg_parser.Arg_Parse:  Change from String type to Boolean type.


## [1.15.0] - 2016-12-06
### Added
- arg_parser.Arg_Wildcard
- arg_parser.py:  Library section:  Added glob library.
- gen_libs.Str_2_Type
- gen_libs.Rm_Newline_List
- gen_libs.File_2_List
- gen_libs:  ast library

### Changed
- arg_parser.Arg_Xor_Dict: Combine 'for' and 'if' into a intersect 'for' statments or complement 'for' statement.  Added break after first false.
- arg_parser.Arg_Require: Combine 'for' and 'if' into a intersect 'for' statments or complement 'for' statement.
- arg_parser.Arg_Validate: Combine 'for' and 'if' into a intersect 'for' statments or complement 'for' statement.
- arg_parser.Arg_Cond_Req_Or: Combine 'for' and 'if' into a intersect 'for' statments or complement 'for' statement.
- arg_parser.Arg_Req_Or_Lst: Combine 'for' and 'if' into a intersect 'for' statments or complement 'for' statement.
- arg_parser.Arg_Cond_Req: Combine 'for' and 'if' into a intersect 'for' statments or complement 'for' statement.  Added break after first false.
- arg_parser.Arg_Dir_Chk_Crt: Combine 'for' and 'if' into a intersect 'for' statments or complement 'for' statement.
- cmds_gen.Is_Add_Cmd:  Changed args_array[x] from a String type check to a Boolean type check.

### Removed
- cmds_gen.Find_Name
- cmds_gen.Fetch_Slv


## [1.14.0] - 2016-11-22
### Changed
- system.Graph:  Changed naming schema for JSON document to include datetime and process id.
- system.Graph:  Added additional attributes to handle web non-processed files.
- cmds_gen.Is_Add_Cmd:  Allow multiple options to be added to the command line with a single argument.  Check to see if the option is a list and add each item in the option list to the command line.
- gen_libs.Dict_2_List:  Replaced for loop with in-line loop.

### Removed
- gen_libs.Zip_File
- gen_libs.Missing_Files
- gen_libs.Del_Or_List
- gen_libs:   #!/usr/bin/python line, not required for library


## [1.13.0] - 2016-08-09
### Added
- system.Server:  Added method: set_host_name.
- system.py:  Added Graph class.
- system.py:  Added F_Graph class.
- system.py:  Added new module libraries.
- cmds_gen.py:  Added os and subprocess libraries.
- cmds_gen.py:  Is_Add_Cmd function.
- cmds_gen.py:  Add_Cmd function.
- cmds_gen.py:  Run_Prog function.
- gen_libs.Root_Run
- gen_libs.File_Cleanup
- gen_libs.Mv_File
- gen_libs.Chown
- gen_libs.Chmod
- gen_libs.File_Search
- gen_libs.Write_File2
- gen_libs.Write_File
- gen_libs.Close_File
- gen_libs.Open_File
- gen_libs.Rotate_Files
- gen_libs.Chk_Crt_File
- gen_libs.Chk_Crt_Dir
- gen_libs.Cp_File2
- gen_libs.Rename_File2

### Changed
- cmds_gen.Create_Cfg_Array:   - Added in **kwargs to allow passing of cfg_path and allow a path to be added to the config file name if the config file does not exist at the current directory.

### Deprecated
- cmds_gen.Find_Name
- cmds_gen.Fetch_Slv


## [1.12.0] - 2016-05-23
### Added
- arg_parser.Arg_Valid_Val
- arg_parser.Arg_Add_Def
- arg_parser.Arg_Default
- system.Yum:  Added class
- cmds_gen.Key_Cleaner:  Added function.
- gen_libs.Pct_Int
- gen_libs.Float_Div
- gen_libs.Dict_Out
- gen_libs.Dict_2_Std
- gen_libs.Prt_Dict
- gen_libs:  Added a number of modules.

### Changed
- arg_parser.Arg_Parse2:  Modified the function to handle options that can have multiple values assigned to the option.  Also replaced code with calls to Arg_Default function.
- arg_parser.Arg_File_Chk:  Changed the first for and if statments into for loop intersect.  Modified function to handle multiple files for an option.
- system.Mail:  Change to documentation header.

### Deprecated
- arg_parser.Arg_NoReq_Xor:  Replaced by Arg_Xor_Dict function.


## [1.11.0] - 2016-03-15
### Added
- system.py:  Initial creation.
- gen_libs.Print_Data
- gen_libs:  sys module

### Changed
- arg_parser.py:  Libraries - Replaced 'from sys import *' with 'import sys'.


## [1.10.0] - 2016-02-19
### Added
- arg_parser.Arg_Parse2:  Replaces Arg_Parse function.
- gen_libs.Get_Secs
- gen_libs.Chk_Int
- gen_libs.Prt_Msg
- gen_libs.Prt_Lvl
- gen_libs:  import for future print functions.

### Deprecated
- arg_parser.Arg_Parse:  Replaced by Arg_Parse2 function.


## [1.9.0] - 2016-02-09
### Added
- cmds_gen.py:  Initial creation.
- gen_libs.Copy_Tree


## [1.8.0] - 2016-01-07
### Added
- arg_parser.Arg_Xor_Dict
- arg_parser.Arg_Validate
- arg_parser.py:  Added gen_libs library module.
- arg_parser.py:  Added version information code to header.
- gen_libs.Validate_Date
- gen_libs.Validate_Int
- gen_libs:  datetime module
- gen_libs:  version information code to header.
- gen_libs:  added comments to explain some of the more unclear code.

### Changed
- arg_parser.Arg_Reg_Xor:  Fixed incorrect documentation.
- arg_parser.Arg_Req_Xor:  Converted function to using the operator.xor function to check xor operations.

### Fixed
- arg_parser.Arg_Req_Xor:  Fixed an error in the function which will allow to check for multiple xor pairs.


## [1.7.0] - 2015-12-11
### Added
- gen_libs.Str_2_List
- gen_libs.Del_Not_In_List
- gen_libs.Dict_2_List

### Deprecated
- gen_libs.Del_Or_List

### Changed
- gen_libs:  Modified documentation for Del_Not_And_List function.


## [1.6.0] - 2015-12-09
### Added
- gen_libs.Is_Missing_Lists

### Deprecated
- gen_libs.Missing_Files
- gen_libs.Zip_File

### Changed
- gen_libs.Rename_File
- gen_libs:  Updated documentation to include class & library dependencies.


## [1.5.0] - 2015-12-04
### Added
- gen_libs.Crt_File_Time
- gen_libs.Compress


## [1.4.0] - 2015-11-20
### Added
- errors.NotYetImplementedError: Added new class.
- gen_libs.Help_Func
- gen_libs.Is_True

### Changed
- arg_parser.Arg_Parse:  To allow any arguments to be processed if certain criteria are met.
- arg_parser.Arg_Parse:  Also corrected an error in which a valid option without a value raises an incorrect error message.
- arg_parser.Arg_Dir_Chk_Crt:  Set dir_crt_list to have a default value in the argument list.


## [1.3.0] - 2015-11-13
### Added
- machine.py:  Initial creation.
- errors.py:  Initial creation.
- gen_libs.And_Is_True


## [1.2.0] - 2015-10-29
### Added
- arg_parser.Arg_Cond_Req_Or
- arg_parser.Arg_Req_Or_Lst
- gen_libs.Not_In_List
- gen_libs.In_List
- gen_libs.Del_Or_List
- gen_libs.List_2_Dict
- gen_libs.Del_Not_And_List


## [1.1.0] - 2015-10-16
### Added
- arg_parser.Arg_Dir_Chk_Crt
- arg_parser.Arg_Req_Xor
- arg_parser.Arg_Set_Path
- arg_parser.Arg_NoReq_Xor
- arg_parser.Arg_Cond_Req
- gen_libs.Cp_File
- gen_libs.List_Files
- gen_libs.Missing_Files
- gen_libs.Rename_File

### Changed
- arg_parser.Arg_Parse:  Added a check to ensure a "-" option is not considered a value to another option.


## [1.0.0] - 2015-10-01
### Added
- arg_parser:  Initial creation.
- gen_libs:  Initial creation of library module.

