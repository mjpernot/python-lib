# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [2.8.5] - 2021-10-07
### Fixed
- gen_class.Mail.add_2_msg:  Add missing newline between lines.
- gen_libs.crt_file_time:  Change time from 12-hour format to 24-hour format.
- gen_class.Daemon:  Placed the MASK global in the correct section and referenced in Daemon.daemonize method.

### Added
- gen_libs.find_email_addr:  Finds all email addresses in a data string.
- gen_libs.pascalize:  Pascal cases a string.

### Removed
- cmds_gen.disconnect function
- cmds_gen.get_inst function
- cmds_gen.create_cfg_array function
- cmds_gen.run_prog function
- machine.Solaris class


## [2.8.4] - 2021-03-23
### Added
- gen_libs.transpose_dict:  Transpose specified keys in a list of dictionaries to specified data types or None.
- gen_libs.is_add_cmd:  Determine if any additional options need to be added to the command line.
- gen_libs.create_cfg_array:  Parse config file and create array of configurations.
- gen_libs.add_cmd:  Append name of arg and value for arg to command line.

### Changed
- machine.Linux:  Changed defaults_file to /etc/my.cnf.

### Deprecated
- machine.Solaris class.
- cmds_gen.add_cmd function.
- cmds_gen.create_cfg_array function.
- cmds_gen.get_inst function.
- cmds_gen.is_add_cmd function.


## [2.8.3] - 2020-12-24
### Fixed
- gen_libs.chk_crt_file:  Error messages being overwritten if multiple errors encountered.
- gen_libs.prt_dict:  Print keys for nested dictionaries in the value.
- arg_parser.arg_file_chk:  Fixed problem with mutable default arguments issue.

### Added
- gen_libs.perm_check:  Check for permission settings on an object.
- gen_libs.print_list:  Prints each item in a list on a seperate line to either a file or standard out.
- gen_libs.sec_2_hr:  Change seconds to hours with hours out to 2 decimal points.
- gen_libs.rm_key:  Remove a key from a dictionary if it exists and return a copy of the modified dictionary.
- gen_libs.is_pos_int:  Returns True|False if number is an integer and positive.
- gen_libs.is_file_text:  Returns True|False on whether the file is a text file.
- gen_libs.rm_whitespace:  Remove white space from a data string.
- gen_libs.has_whitespace:  Returns True|False on whether a string has a white space.
- gen_class.Mail.send_mailx:  Emails message out using mailx.

### Changed
- gen_libs.list_files:  Added "include_path" option to include directory path with the file name.
- gen_libs.in_list, gen_libs.make_md5_hash, gen_libs.not_in_list, gen_libs.openfile, gen_libs.root_run, gen_libs.filename_search, gen_libs.dir_file_match:  Refactored function.
- gen_class.LogFile.get_marker:  Refactored method.
- gen_class:  Changed a number of variable names to standard naming convention.
- gen_class.Logger.\_\_init\_\_:  Added "mode" keyword argument to allow append or write modes to log files.
- cmds_gen, arg_parser, gen_class:  Removed unneccessary \*\*kwargs from arguments lists.
- gen_class.Mail.create_subject:  Added argument to set the subject line delimiter if using a list.
- gen_class.Mail.\_\_init\_\_:  Set "from address" to default of current user and hostname if none is provided.
- gen_libs.chk_crt_dir:  Added option to see if directory is executable.
- gen_libs.chk_crt_dir, gen_libs.chk_crt_file:  Replaced section of code on permission checks with call to perm_check.
- gen_libs.chk_crt_file:  Added option to see if file is executable.
- gen_class.Mail.send_mail:  Add a keyword argument option to allow the send_mailx method to be called.
- gen_libs.print_dict:  Added ability to add the dictionary to an email instance message.
- gen_libs.del_not_and_list:  Replaced try/except with an intersect of two sets to capture items to be removed.
- arg_parser.arg_wildcard:  Refactored the function for better functionality.
- gen_libs.milli_2_readadble, gen_libs.make_md5_hash, gen_libs.list_2_dict, gen_libs.prt_dict:  Changed variable name to standard naming convention.
- Documentation update.

### Deprecated
- cmds_gen.run_prog
- cmds_gen.disconnect


## [2.8.2] - 2020-07-15
### Added
- arg_parser.\_make_dir:  Tries to create a directory and capture any exceptions.

### Fixed
- arg_parser.arg_dir_chk_crt:  Never checks for write access unless directory is in dir_crt_list.
- arg_parser.arg_dir_chk_crt:  Does not create directory if dir_crt_list is not subset of dir_chk_list.
- gen_libs.crt_file_time:  Fixed where no trailing slash in path gives incorrect results.
- arg_parser.arg_set_path:  Fixed where a second trailing slash was added if one was already present.

### Changed
- arg_parser.\_make_dir:  Replaced bare exception with catching specific exception cases.
- gen_class.SingleInstanceException:  Changed exception class from BaseException to Exception.
- gen_libs:  Changed in numerous functions the variable names to standard naming convention.
- arg_parser.\_file_create:  Changed print errors to distingish between different exceptions.
- arg_parser.arg_set_path:  Removed non-required else clause.
- arg_parser.arg_dir_chk_crt:  Call to \_make_dir to reduce complexity rating.
- gen_class:  Changed in numerous methods in multiple classes the variable names to standard naming convention.
- cmds_gen:  Changed in numerous functions the variable names to standard naming convention.
- arg_parser:  Changed in numerous functions the variable names to standard naming convention.
- gen_class.Mail.create_subject:  Changed delimiter to a space for lists passed to method.
- gen_libs.crt_file_time:  Made ext argument an optional argument.
- gen_libs.crt_file_time:  Add period (.) seperator between filename and extension.


## [2.8.1] - 2020-03-25
### Fixed
- gen_libs.compress, cmds_gen.run_prog, gen_libs.make_md5_hash:  Fixed subprocess instance from SonarQube scan finding.
- gen_class.Daemon.stop:  Fixed signal instance from SonarQube scan finding.
- gen_class.Mail.read_stdin:  Fixed sys instance from SonarQube scan finding.
- gen_class.Mail.send_mail:  Fixed smtplib instance from SonarQube scan finding.
- gen_class.Daemon.\_\_init\_\_:  Fixed critical finding from SonarQube scan finding.

### Added
- gen_libs.date_range:  Generators a list of year-month-01 combinations between two dates.
- gen_libs.month_days:  Return the number of days in the month for a date.
- gen_libs.filename_search:  Return list of file names that contain search string in the file name.
- gen_class.get_inst, gen_libs.get_inst, cmds_gen.get_inst:  Returns the module instance header.

### Changed
- gen_libs.dir_file_match:  Added argument to allow full paths with names to be returned.
- arg_parser.arg_cond_req_or, arg_parser.arg_cond_req, arg_parser.arg_req_or_lst:  Changed "y" variable to throwaway variable "\_".
- gen_class.Logger.\_\_init\_\_:  Removed non-used variable and code.
- gen_libs.dict_2_std, gen_libs.print_data, gen_libs.print_dict:  Added file mode option writing to file.


## [2.8.0] - 2019-12-03
### Changed
- gen_class.LogFile (Field Release):  Class and methods that stores and manipulates log entries files or standard in.

### Fixed
- gen_class.LogFile.filter_keyword:  Converted search entries to lowercase to be case-insensitive searches.


## [2.7.7] - 2019-11-29
### Removed
- gen_libs.data_multi_out

### Added
- gen_class.LogFile (Beta Release):  Class and methods that stores and manipulates log entries files or standard in.


## [2.7.6] - 2019-09-23
### Fixed
- gen_libs.dict_2_list:  Added check to only process dictionaries where that key exists in the dictionary.

### Changed
- gen_class.Mail.add_2_msg:  Added ability to convert non-string arguments to strings.
- gen_libs.normalize:  Changed "pass" to "continue" to prevent confusion on processing flow.
- arg_parser.arg_req_xor:  Changed "opt_xor_list" to "opt_xor" due to confusing datatype association.
- arg_parser.arg_req_or_lst:  Changed "opt_or_dict_list" to "opt_or_dict" due to confusing datatype association.
- arg_parser.arg_noreq_xor:  Changed "xor_noreq_list" to "xor_noreq" due to confusing datatype association.
- arg_parser.arg_cond_req:  Changed "opt_con_req_list" to "opt_con_req" due to confusing datatype association.
- arg_parser.arg_validate, arg_parser.arg_set_path, arg_parser.arg_req_xor, arg_parser.arg_req_or_lst, arg_parser.arg_require, arg_parser.arg_noreq_xor, arg_parser.arg_file_chk, arg_parser.arg_dir_chk_crt, arg_parser.arg_cond_req_or, arg_parser.arg_cond_req, arg_parser.arg_xor_dict:  Added \*\*kwargs to argument list.
- arg_parser.arg_parse2:  Documentation update.
- arg_parser.arg_file_chk, arg_parser.arg_dir_chk_crt, arg_parser.arg_require, arg_parser.\_file_create:  Changed "exit_flag" to "status" and updated documentation.
- arg_parser.arg_noreq_xor, arg_parser.arg_xor_dict:  Changed "xor_flag" to "status" and updated documentation.
- arg_parser.arg_validate, arg_parser.arg_req_xor, arg_parser.arg_valid_val:  Changed "status_flag" to "status" and updated documentation.
- arg_parser.arg_cond_req_or, arg_parser.arg_req_or_lst:  Changed "or_flag" to "status" and updated documentation.
- arg_parser.arg_cond_req:  Changed "exit_flag" to "status" and updated documentation.
- gen_class.Logger:  Changed "self.logger" to "self.log" to avoid confusion with class name.
- gen_class.Logger.\_\_init\_\_:  Moved "mode" argument to \*\*kwargs.
- gen_class.Logger.\_\_init\_\_:  Removed check for "INFO" and let the "else" clause catch it.

### Added
- gen_class.setup_mail:  Initialize a mail instance.
- gen_libs.cp_dir:  Copies a directory from source to destination with exception handling.


## [2.7.5] - 2019-07-22
### Change
- gen_libs.str_2_list, gen_libs.list_files:  Refactored function.

### Fixed
- gen_class.ProgramLock.\_\_init\_\_:  Fixed problem with mutable default arguments issue.
- cmds_gen.is_add_cmd, cmds_gen.run_prog, cmds_gen.add_cmd:  Fixed problem with mutable default arguments issue.
- arg_parser:  Fixed in numerous functions the problem with mutable default arguments issue.
- gen_libs.data_multi_out:  Fixed in numerous functions the problem with mutable default arguments issue.
- gen_class.Mail.create_subject:  Fixed so the subject line can be a string or list.
- gen_class.Mail.\_\_init\_\_:  Fixed it where a subject can handle a list.

### Added
- gen_libs.list_2_str:  Convert a list to a string.

### Deprecated
- gen_libs.data_multi_out:  No longer required.


## [2.7.4] - 2019-06-17
### Added
- gen_libs.openfile:  Opens a normal or compressed file based on filename extension.

### Removed
- system:  Removed deprecated system module.


## [2.7.3] - 2019-05-02
### Changed
- gen_libs.rotate_files:  Refactored code in function to be more stream-line.
- arg_parser.arg_parse2:  Replaced multi-list code section with call to \_parse_multi function.
- arg_parser.arg_parse2:  Replaced single-list code section with call to \_parse_single function.
- arg_parser.arg_file_chk:  Replaced exception code with call to \_create_file function.

### Added
- arg_parser.\_parse_single:  Private function for use by arg_parser2 function.
- arg_parser.\_file_create:  Private function for use by arg_file_chk function.
- arg_parser.\_parse_multi:  Private function for use by arg_parser2 function.

### Removed
- gen_libs.copy_tree:  Function replaced by shutil.copytree.


## [2.7.2] - 2019-03-06
### Changed
- gen_class.Yum.fetch_install_pkgs, gen_class.Yum.fetch_update_pkgs:  Changed output to camelCase.


## [2.7.1] - 2018-12-11
### Fixed
- gen_libs.prt_msg:  Changed prt_lvl variable to lvl, due to naming conflict within function.


## [2.7.0] - 2018-11-27
### Updated
- gen_libs.display_data:  Refactored function to reduce complexity rating.
- gen_libs.data_multi_out:  Changed "MAIL" to "mail" - code convention change.

### Added
- gen_libs.display_data.print_level:  Print the number of levels (i.e. tabs) required for line.
- gen_class.Mail.create_subject:  Set the subject line of the email.

### Fixed
- arg_parser.arg_parse2:  Shallow copied assignments of "multi_val" and "opt_val".
- arg_parser.arg_dir_chk_crt, arg_parser.arg_file_chk, arg_parser.arg_parse2:  Changed function parameter mutable argument default to immutable argument default.
- gen_class.Mail.\_\_init\_\_:  Shallow copied assignment of "to" to "self.to" if it is a list.
- gen_class.Daemon.\_\_init\_\_:  Shallow copied assignment of "argv_list" list to "self.argv_list".
- gen_class.Daemon.\_\_init\_\_:  Changed function parameter mutable argument default to immutable argument default.

### Deprecated
- system.py:  Module has been deprecated.


## [2.6.0] - 2018-09-13
### Removed
- gen_libs.Prt_Msg
- gen_libs.Prt_Lvl
- gen_libs.Print_Data
- gen_libs.Open_File
- gen_libs.Load_Module
- gen_libs.List_Filter_Files
- gen_libs.Close_File
- gen_libs.Chk_Crt_File
- gen_libs.Chk_Crt_Dir
- cmds_gen.Add_Cmd
- cmds_gen.Is_Add_Cmd
- cmds_gen.Disconnect
- arg_parser.Arg_Set_Path


## [2.5.0] - 2018-09-10
### Changed
- arg_parser.arg_parse2:  Replaced "gen_libs.Chk_Int" with "gen_libs.chk_int" call.
- system.FGraph.\_\_init\_\_:  Replaced "gen_libs.file_search" with "gen_libs.file_search".
- gen_libs.file_search:  Refactored the code in the function.
- gen_libs.file_2_list:  Remove any newlines from the end of each line.

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

### Removed
- gen_libs.Milli_2_Readadble
- gen_libs.File_Search
- gen_libs.Chk_Int
- arg_parser.Arg_Wildcard
- arg_parser.Arg_Add_Def
- arg_parser.Arg_Valid_Val
- arg_parser.Arg_Default
- arg_parser.Arg_Parse2
- arg_parser.Arg_Xor_Dict
- arg_parser.Arg_Validate
- arg_parser.Arg_Cond_Req
- arg_parser.Arg_Cond_Req_Or
- arg_parser.Arg_Req_Or_Lst
- arg_parser.Arg_NoReq_Xor
- arg_parser.Arg_Req_Xor
- arg_parser.Arg_Dir_Chk_Crt
- arg_parser.Arg_File_Chk
- arg_parser.Arg_Parse
- arg_parser.Arg_Require
- system.Yum
- system.F_Graph
- system.Mail
- cmds_gen.Run_Prog
- cmds_gen.Create_Cfg_Array
- gen_libs.Validate_Int
- gen_libs.Validate_Date
- gen_libs.Str_2_Type
- gen_libs.Str_2_List
- gen_libs.Help_Func
- gen_libs.Rm_Newline_List
- gen_libs.Rm_File
- gen_libs.Rm_Dup_List
- gen_libs.Rotate_Files
- gen_libs.Root_Run
- gen_libs.Normalize
- gen_libs.Make_Zip
- gen_libs.List_Files
- gen_libs.List_2_Dict
- gen_libs.Key_Cleaner
- gen_libs.Is_True
- gen_libs.Is_Missing_Lists
- gen_libs.Not_In_List
- gen_libs.In_List
- gen_libs.Get_Time
- gen_libs.Get_Secs
- gen_libs.Get_Date
- gen_libs.Float_Div
- gen_libs.Pct_Int
- gen_libs.File_Cleanup
- gen_libs.Disk_Usage
- gen_libs.Dir_File_Match
- gen_libs.Prt_Dict
- gen_libs.Dict_2_Std
- gen_libs.Print_Dict
- gen_libs.Dict_2_List
- gen_libs.Del_Not_In_List
- gen_libs.Del_Not_And_List
- gen_libs.Crt_File_Time
- gen_libs.Write_File2
- gen_libs.Make_MD5_Hash
- gen_libs.Write_2_Log
- gen_libs.Rename_File
- gen_libs.Rename_File2
- gen_libs.Mv_File2
- gen_libs.Mv_File
- gen_libs.Cp_File
- gen_libs.Cp_File2
- gen_libs.Copy_Tree
- gen_libs.Compress
- gen_libs.File_2_List
- gen_libs.Chmod
- gen_libs.Bytes_2_Readable
- gen_libs.And_Is_True
- gen_libs.Merge_2_Dicts
- gen_libs.Display_Data
- gen_libs.Empty_File
- gen_libs.Chown


## [2.4.0] - 2018-05-28
### Changed
- gen_class.Yum.\_\_init\_\_:  Added self.distro attribute to class.

### Added
- gen_class.Yum.get_disto:  Method - Return class linux_distribution.

### Removed
- gen_class.Program_Lock
- gen_class.Single_Instance_Exception


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

### Changed
- gen_class.Yum.\_\_init\_\_:  Added new attributes for OS version information.

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
- gen_libs.file_search, gen_libs.file_2_list:  Replaced Close_File call with close command.
- gen_libs.file_search:  Replaced Open_File call with open command.
- gen_libs.py:  Changed "from subprocess" to "import subprocess".
- gen_libs.py:  Qualified all calls to functions in subprocess module.
- cmds_gen.is_add_cmd:  Replaced Add_Cmd with add_cmd function call.
- system.py, cmds_gen.py, machine.py, errors.py, arg_parser.py:  Setup single-source version control.

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
- gen_libs.py:  Removed "from sys import \*", already have "import sys" in place.


## [1.36.0] - 2018-03-09
### Added
- gen_libs.data_multi_out:  Send data to multiple outputs options.


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

### Changed
- gen_libs.py:  Setup single-source version control.

### Deprecated
- gen_libs.Chk_Crt_Dir:  Replaced by gen_libs.chk_crt_dir.
- gen_libs.Chk_Crt_File:  Replaced by gen_libs.chk_crt_file.


## [1.33.2] - 2018-01-26
### Changed
- Documentation update.


## [1.33.1] - 2018-01-25
### Changed
- gen_class.ProgressBar_calc_and_update.py:  Changed format of mock.patch statements.


## [1.33.0] - 2018-01-22
### Added
- gen_class.ProgressBar: Displays and updates a progress bar for an ongoing operation.
- gen_class.SingleInstanceException:  Class exception for the ProgramLock class.
- gen_class.ProgramLock:  Creates a file lock instance for a program.
- gen_class.System:  Class which is a representation of a Linux server.
- gen_class.Mail:  Class which is a representation of an email.

### Changed
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

### Changed
- gen_libs.get_base_dir:  Added \*\*kwargs to argument list for future use.

### Deprecated
- gen_libs.Write_File2:  Replaced by gen_libs.write_file.
- gen_libs.Display_Data:  Replace by gen_libs.display_data.
- gen_libs.Empty_file:  Replaced by gen_libs.clear_file.

 
## [1.31.0] - 2018-01-12
### Added
- gen_libs.merge_data_types:  Merge two similar data types (e.g. string, dictionary, list, tuple).
- gen_libs.merge_two_dicts:  Merge two dictionaries.
- gen_libs.no_std_out:  Suppresses standard output of a function.

### Deprecated
- gen_libs.Merge_2_Dicts:  Replaced by gen_libs.merge_two_dicts.


## [1.30.0] - 2017-12-22
### Added
- gen_libs.month_delta:  Produces a month delta based on date passed to function.
- gen_libs.file_search_cnt:  Find number of lines in a file that match a pattern.
- gen_libs.get_base_dir:  Return the base directory path of the file name.


## [1.29.1] - 2017-12-13
### Changed
- Documentation update.


## [1.29.0] - 2017-10-06
### Added
- gen_libs.\_ntuple_diskusage
- gen_libs.Disk_Usage


## [1.28.1] - 2017-09-26
### Fixed
- gen_libs.Make_MD5_Hash:  It's overwriting hash files if file names are same, but extensions are different.
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
- system.py:  Change single quotes to double quotes.

### Deprecated
- gen_libs.Dict_Out

## Removed
- gen_libs: Dependency of the cmds_mongo library.


## [1.22.0] - 2017-08-03
### Changed
- arg_parser.py:  Convert comments/documentation to docstrings.
- arg_parser.py:  Change single quotes to double quotes.
- cmds_gen.py:  Change single quotes to double quotes.
- machine.py:  Convert comments/documentation to docstrings.
- errors.py:  Convert comments/documentation to docstrings.
- errors.Error:  Remove version information and replaced with pass.
- gen_libs:  Convert comments/documentation to docstrings.
- gen_libs:  Change single quotes to double quotes.

### Removed
- cmds_gen.Key_Cleaner:  Moved to gen_libs.py module.


## [1.21.5] - 2017-08-03
### Fixed
- gen_libs:  List_Files function listed twice.
- gen_libs:  Rename List_Files created on 2017-07-17 to List_Filter_Files due to naming conflict.


## [1.21.4] - 2017-08-02
### Changed
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
- gen_libs:  Updated docstrings to display programs usage/help message.
- gen_libs.Help_Func:  Call func_name to print programs docstring.

### Deprecated
- gen_libs.normalize


## [1.17.1] - 2017-04-25
### Added
- gen_class.Program_Lock:  Allow a program to create a lock instance of the program.  This will allow other programs to know if an instance of the program is running.
- gen_class.Single_Instance_Exception:  Class exception for the Program_Lock class.  Used when an instance lock has been detected.


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
- arg_parser.Arg_Parse, arg_parser.Arg_Parse2:  Change from String type to Boolean type.


## [1.15.0] - 2016-12-06
### Added
- arg_parser.Arg_Wildcard
- gen_libs.Str_2_Type
- gen_libs.Rm_Newline_List
- gen_libs.File_2_List
- gen_libs:  ast library

### Changed
- arg_parser.Arg_Cond_Req, arg_parser.Arg_Xor_Dict: Combine 'for' and 'if' into a intersect 'for' statments or complement 'for' statement.  Added break after first false.
- arg_parser.Arg_Validate, arg_parser.Arg_Cond_Req_Or, arg_parser.Arg_Req_Or_Lst, arg_parser.Arg_Dir_Chk_Crt, arg_parser.Arg_Require: Combine 'for' and 'if' into a intersect 'for' statments or complement 'for' statement.
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
- gen_libs:   #!/usr/bin/python line.


## [1.13.0] - 2016-08-09
### Added
- system.Serverset_host_name
- system.Graph
- system.F_Graph
- cmds_gen.Is_Add_Cmd
- cmds_gen.Add_Cmd
- cmds_gen.Run_Prog
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
- cmds_gen.Create_Cfg_Array:  Added in \*\*kwargs to allow passing of cfg_path and allow a path to be added to the config file name if the config file does not exist at the current directory.

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

### Changed
- arg_parser.Arg_Parse2:  Modified the function to handle options that can have multiple values assigned to the option.  Also replaced code with calls to Arg_Default function.
- arg_parser.Arg_File_Chk:  Changed the first for and if statments into for loop intersect.  Modified function to handle multiple files for an option.
- system.Mail:  Documentation update.

### Deprecated
- arg_parser.Arg_NoReq_Xor:  Replaced by Arg_Xor_Dict function.


## [1.11.0] - 2016-03-15
### Added
- system.py:  Initial creation.
- gen_libs.Print_Data
- gen_libs:  sys module

### Changed
- arg_parser.py:  Libraries - Replaced "from sys import \*" with "import sys".


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


## [1.6.0] - 2015-12-09
### Added
- gen_libs.Is_Missing_Lists

### Deprecated
- gen_libs.Missing_Files
- gen_libs.Zip_File

### Changed
- gen_libs.Rename_File


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

