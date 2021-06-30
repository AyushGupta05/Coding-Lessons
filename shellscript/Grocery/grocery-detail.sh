vegetables=(potato carrot apple banana taproot)
vegetable_prices=(15 5 20 15 30)
# position=$((4-1))
# echo "${vegetable_prices[${position}]}"
# exit




line="=========================================================="

echo $line
echo "Welcome to Ayush Grocery Shop"
echo $line
echo "We have the following vegetables in our shop"
line_number=1
for item in "${vegetables[@]}"
do

    position=$((line_number - 1))
    echo "${line_number}. ${item} : ${vegetable_prices[${position}]} "
    line_number=$((line_number+1))
done

echo $line



user_continue="yes"
total=0
while [ "$user_continue" = "yes" ] 
do
    echo "Which vegetable do you want?"
    read -p  "enter the vegetable number :  " vegetable_id 
    #read will wait for the user to type
    echo "You have selected $vegetable_id "
    read -p "how much Quantity do you want" veg_quantity
    position=$(($vegetable_id - 1))

    cost=$(( $veg_quantity * ${vegetable_prices[${position}]} ))
    total=$((total + cost))
    echo "So far the total price is $total"
    read -p "Do you want to continue shopping yes/no ?" user_continue
    
    
done

echo " To the total bill amount is $total"

echo $line

echo "Please consider shopping with us again"
