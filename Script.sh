line="____________________________________"

echo "Hello"
echo $line
echo "In this game you must choose a number between 1-15 until you choose the correct number"
echo $line
read -p "Choose a number between 1-15   :" number_input

while [ $number_input -ge 16 ];
do 
read -p "Please enter a lower number" number_input
done

while [ $number_input -ne 11 ];
do 
read -p "Incorrect, Please choose another number" number_input
done



if [ $number_input -eq 11 ]; then 

read -p "You have won"


fi