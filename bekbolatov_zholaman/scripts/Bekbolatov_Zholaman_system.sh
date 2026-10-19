#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
printf '==============================
Student Information
==============================
'
printf 'Name: %s
Surname: %s
Group: %s
Student ID: %s
' "${STUDENT_NAME:-Zholaman}" "${STUDENT_SURNAME:-Bekbolatov}" "${STUDENT_GROUP:-IT2-2314}" "${STUDENT_ID:-37614}"
printf '
==============================
System Information
==============================
'
printf 'Username: '; whoami
printf 'Hostname: '; hostname
printf 'Current Date: '; date -Is
printf 'Operating System: '; uname -a
printf 'Disk Usage:
'; df -h / 
printf 'Memory Usage:
'; free -h
if [[ -f "$root/Bekbolatov_Zholaman_info.txt" ]]; then
 echo 'Student information file exists.'
else
 echo 'Student information file does not exist.'
fi
