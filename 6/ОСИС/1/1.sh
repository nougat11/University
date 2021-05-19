#!/bin/sh

# Author: Vlad Kuzma
# Copyright (c) MIT-License
# Laba 1, Varik 5
# Статистика текущего сеанса: имя пользователя, текущее время, дата, текущий каталог,
# число процессов в системе, время работы.

echo "Имя пользователя $USER"
now="`date +%T`"
echo "Текущее время: $now"
date="`date +%D`"
echo "Дата: $date"
echo "Текущий каталог: $PWD"
echo "Число процессов в системе :" 
ps -e | wc -l
echo "Время работы:"
uptime -p
