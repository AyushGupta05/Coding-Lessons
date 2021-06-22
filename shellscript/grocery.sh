# Ayush Grocery supermarket shop bill
# The aim of the program is to generate a bill for the purchased grocery products
# The user will enter what they want and how much they want and we need to calculate the total cost and show it to them
# use read command to get the grocery name and then check what ever the user has entered 
# if the user entered tomato then the price is 10rs
# if the user entered potato, the price is 15rs
# if the user entered carrot the price is 5rs
# if the user entered apple the price is 20rs
# if the user entered banana the price is 15rs
# ask the user how much they want and them multiply the cost into the quantity

vegetable_1="Potato"
# string variable is any variable with double quotes
vegetable_1_price=15
#because their are no double quotes it is called integer variable

vegetable_2="Carrot"
vegetable_2_price=5

vegetable_3="Apple"
vegetable_3_price=20

vegetable_4="Banana"
vegetable_4_price=15

line="=========================================================="

echo $line
echo "Welcome to Ayush Grocery Shop"
echo $line
echo "We have the following vegetables in our shop"
echo 1. $vegetable_1 :$vegetable_1_price rs
echo 2. $vegetable_2 :$vegetable_2_price rs
echo 3. $vegetable_3 :$vegetable_3_price rs
echo 4. $vegetable_4 :$vegetable_4_price rs
echo $line
echo "Which vegetable do you want?"
read -p  "enter the vegetable number :  " vegetable_id 
#read will wait for the user to type
echo $vegetable_id
#using if condition
if [ $vegetable_id -eq 1 ]; then 
echo "You have selected potato"
read -p "how much Quantity do you want" veg1_quantity
echo "the total amount is : " $(( $veg1_quantity * $vegetable_1_price )) rs
# if is a condidition. line number 45 ends if (fi)
fi
if [ $vegetable_id -eq 2 ]; then 
echo "You have selected carrot"
fi
if [ $vegetable_id -eq 3 ]; then 
echo "You have selected apple"
fi