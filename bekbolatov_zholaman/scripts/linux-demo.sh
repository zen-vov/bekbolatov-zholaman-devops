#!/usr/bin/env bash
set -euxo pipefail
cd "$(dirname "$0")/.."
pwd
ls -la
mkdir -p backup logs
# Generate reproducible sample log; runtime logs remain ignored by Git.
printf '%s\n' 'INFO Application started' 'INFO User logged in' 'WARNING Configuration file missing' 'INFO Configuration loaded' 'ERROR Connection failed' 'INFO Application restarted' 'WARNING Memory usage is high' 'INFO Request received' 'ERROR Request failed' 'INFO Application stopped' > logs/application.log
touch backup/demo.txt
cp Bekbolatov_Zholaman_info.txt backup/info-copy.txt
mv backup/demo.txt backup/moved.txt
rm backup/moved.txt
cat Bekbolatov_Zholaman_info.txt
head -n 3 logs/application.log
tail -n 5 logs/application.log
find . -name application.log
grep ERROR logs/application.log
grep WARNING logs/application.log
test "$(grep -c ERROR logs/application.log)" = 2
chmod 600 private.txt
chmod 644 public.txt
chmod +x scripts/Bekbolatov_Zholaman_system.sh
ls -l private.txt public.txt scripts/Bekbolatov_Zholaman_system.sh
./scripts/Bekbolatov_Zholaman_system.sh
# Check the absent-file branch against a temporary independent copy.
mkdir -p backup/missing/scripts
cp scripts/Bekbolatov_Zholaman_system.sh backup/missing/scripts/
backup/missing/scripts/Bekbolatov_Zholaman_system.sh | grep 'Student information file does not exist.'
ps
ps aux
ps -eo pid,user,pcpu,pmem,args
top -b -n 1 | head -n 20
