#!/bin/bash
# Unit test code coverage for gen_dnf module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#       that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_init.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_capture_pkgs.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_capture_repos.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_fetch_install_pkgs.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_fetch_update_pkgs.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_fetch_repos.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_get_distro.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_get_all_repos.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_get_enabled_repos.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_get_hostname.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_get_install_pkgs.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_get_installed.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_get_os.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_get_release.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_get_update_pkgs.py
coverage run -a --source=gen_dnf test/unit/gen_dnf/dnf_get_updates.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m

