Genres=(Action Adventure Mystery Horror Fantasy )
book_prices=(10 20 30 40 50)
flat_discount=10

# Lesson : Bash Scripting doesn;t supports decimal points

line="=========================================================="

echo $line
echo "Welcome to the Sunshine Book shop"
echo $line
echo "In this shop you may choose a genre of the book you want"
echo "You will then choose a quantity, and we will randomly give you books based on that genre"
echo $line
echo "The genre of the books we have are written below"
echo $line

line_number=1
for item in "${Genres[@]}"
do

    position=$((line_number - 1))
    echo "${line_number}. ${item} : ${book_prices[${position}]} "
    line_number=$((line_number+1))
done

echo $line



user_continue="yes"
total=0
while [ "$user_continue" = "yes" ] 
do
    echo "Which Genre would you like to purchase"
    read -p  "enter the number of the genre :  " book_id 

    echo "You have selected $book_id "
    read -p "How many books of that Genre would you like?" book_quantity
    position=$(($book_id - 1))

    cost=$(( $book_quantity * ${book_prices[${position}]} )) 

    total=$((total + cost))
    echo "So far the total price of the $book_quantity books is $total"
    read -p "Do you want to continue shopping yes/no ?" user_continue
    
    
done

echo "As you have come during christmas, we have a 10% discount"

final=$(($total - $flat_discount))
echo "The bill amount is $total"
echo "The discounted amount is $flat_discount"
echo "Amount to be paid is $final"

echo $line

read -p "Please enter your adrress" ad_number

echo Youre address is: 
$ad_number 

echo "Your books will be delivered to you within 2-3 days"

echo $line
echo "Please consider using sunshine bookshop  again"

