#! /bin/bash
# Md.Saif Niaz
#ID: 100555440
# 1=k, 2=m, 3=gadsby.txt

#echo $1, $2, $3

head -n -$2 $3 | tail -n +$1 

exit 0