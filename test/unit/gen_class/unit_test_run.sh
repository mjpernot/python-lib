#!/bin/bash
# Unit testing program for the gen_class module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file 
#   is located at.

echo ""
echo "Unit test:  ProgressBar.__init__"
test/unit/gen_class/ProgressBar_init.py

echo ""
echo "Unit test:  ProgressBar.update"
test/unit/gen_class/ProgressBar_update.py

echo ""
echo "Unit test:  ProgressBar.calc_and_update"
test/unit/gen_class/ProgressBar_calc_and_update.py

echo ""
echo "Unit test:  SingleInstanceException"
test/unit/gen_class/SingleInstanceException.py

echo ""
echo "Unit test:  ProgramLock.__init__"
test/unit/gen_class/ProgramLock_init.py

echo ""
echo "Unit test:  ProgramLock.del"
test/unit/gen_class/ProgramLock_del.py

echo ""
echo "Unit test:  Yum.__init__"
test/unit/gen_class/Yum_init.py

echo ""
echo "Unit test:  Yum.get_os"
test/unit/gen_class/Yum_get_os.py

echo ""
echo "Unit test:  Yum.get_distro"
test/unit/gen_class/Yum_get_distro.py

echo ""
echo "Unit test:  Yum.get_release"
test/unit/gen_class/Yum_get_release.py

echo ""
echo "Unit test:  Mail.__init__"
test/unit/gen_class/Mail_init.py

echo ""
echo "Unit test:  Mail.add_2_msg"
test/unit/gen_class/Mail_add_2_msg.py

echo ""
echo "Unit test:  Mail.create_body"
test/unit/gen_class/Mail_create_body.py

