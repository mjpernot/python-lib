# Unit testing program for the gen_dnf module.
# # This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo "Unit test: gen_dnf module"  
/usr/bin/python ./test/unit/gen_dnf/dnf_init.py
/usr/bin/python ./test/unit/gen_dnf/dnf_capture_pkgs.py
/usr/bin/python ./test/unit/gen_dnf/dnf_capture_repos.py
/usr/bin/python ./test/unit/gen_dnf/dnf_fetch_install_pkgs.py
/usr/bin/python ./test/unit/gen_dnf/dnf_fetch_repos.py
/usr/bin/python ./test/unit/gen_dnf/dnf_fetch_update_pkgs.py
/usr/bin/python ./test/unit/gen_dnf/dnf_get_all_repos.py
/usr/bin/python ./test/unit/gen_dnf/dnf_get_distro.py
/usr/bin/python ./test/unit/gen_dnf/dnf_get_enabled_repos.py
/usr/bin/python ./test/unit/gen_dnf/dnf_get_hostname.py
/usr/bin/python ./test/unit/gen_dnf/dnf_get_installed.py
/usr/bin/python ./test/unit/gen_dnf/dnf_get_install_pkgs.py
/usr/bin/python ./test/unit/gen_dnf/dnf_get_os.py
/usr/bin/python ./test/unit/gen_dnf/dnf_get_release.py
/usr/bin/python ./test/unit/gen_dnf/dnf_get_update_pkgs.py
/usr/bin/python ./test/unit/gen_dnf/dnf_get_updates.py
