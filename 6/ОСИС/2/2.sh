#!/bin/bash

#[ОСИС][Кузьма][2][Крестики-нолики]
declare -A a
n=3
m=3

function output(){
   for ((i=0; i<n; i++ )) do
       echo
       for (( j=0; j<m; j++ )) do
	   if [ "${a[$i,$j]}" = "1" ]; then
		   printf "%5s" "x"
	   elif [ "${a[$i,$j]}" = "0" ]; then
		   printf "%5s" "o"
           else
           	   printf "%5s" "*"
           fi
       done
   done
   echo
}
function win_condition(){

   flag=0
   for((i=0; i<n; i++)){
        if [[ ${a[$i,0]} != -1 && ${a[$i,0]} == ${a[$i,1]} && ${a[$i,0]} == ${a[$i,2]} ]]; then
		flag=1
	fi
   }
   
   for((j=0; j<m; j++)){
        if [[ ${a[0,$j]} != -1 && ${a[0,$j]} == ${a[1,$j]} && ${a[0,$j]} == ${a[2,$j]} ]]; then
                flag=1
        fi	
   }

   if [[ ${a[0,0]} != -1 && ${a[0,0]} == ${a[1,1]} && ${a[0,0]} == ${a[2,2]} ]]; then
	flag=1
   fi

   if [[ ${a[0,2]} != -1 && ${a[0,2]} == ${a[1,1]} && ${a[0,2]} == ${a[2,0]} ]]; then
        flag=1
   fi

   if [ "$flag" == "1" ]; then
	echo "Игра окончена. Кто-то победил, а кто-то проиграл."
	exit 0
   fi

   draw=1
   for ((i=0; i<n; i++ )) do
      for (( j=0; j<m; j++ )) do
         if [ ${a[$i,$j]} == -1 ]; then
             draw=0
         fi
      done
   done

   if [ "$draw" == "1" ]; then
       echo "Священная ничья."
       exit 0
   fi

}

echo "Здравствуйте, крестики-нолики приветствуют вас, кто-то выйграет, кого-то выйграют"
for ((i=0; i<n; i++ )) do
   for (( j=0; j<m; j++ )) do
      a[$i,$j]=-1
   done
done
echo "Поле чудес:"
output
echo "Запускаем игру"
echo

while true;
do
    while true;
    do
	echo "Первый игрок, назовите координаты: "
	read x y

        if [ ${a[$x,$y]} == -1 ]; then 
	    a[$x,$y]=1 
            break 
        fi
    
        echo "Вы указали неверные координаты, пожалуйста укажите верные)"
    done
    output
    win_condition

    while true;
    do

    	echo "Второй игрок, назовите координаты: "
    	read x y

    	if [ ${a[$x,$y]} == -1 ]; then
            a[$x,$y]=0
            break
    	fi

    	echo "Вы указали неверные координаты, пожалуйста укажите верные"
    done

    output
    echo
    win_condition

done
