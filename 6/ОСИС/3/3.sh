#!/bin/bash
#[ОСИС][Кузьма][3][csv-to-sql]

file=$(cat /home/grandnougat/OSIS/file.csv)

table_name=$(echo "$file" | sed -n '1p')
column_names=$(echo "$file" | sed -n '2p')

file="$(echo "$file" | sed '1,2d')"

echo "$file" | awk "{ print \"insert into $table_name ($column_names) values (\" \$0 \");\" }"
