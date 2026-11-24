#!/bin/bash
set -e
cd /home/user/Fac-app/livre-treso
for i in 1 2 3; do build/make.sh >/dev/null; python3 build/pagemap.py > build/pagemap.log; head -1 build/pagemap.log; done
build/make.sh
