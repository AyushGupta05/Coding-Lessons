vegetables=["Potato", "Carrot", "Apple", "Banana"]
vegetable_prices=[15,20,5,20]
# string variable is any variable with double quotes
user_cart=[]
line="=========================================================="


print(line)
print("Welcome to Ayush Grocery Shop")
print(line)




user_continue="yes"

while user_continue == "yes":
    serial_number=1
    print("We have the following vegetables in our shop")
    for item in vegetables:   
        print(f"{serial_number}.{item}:{vegetable_prices[serial_number-1]}")
        serial_number = serial_number+1
    print(line)
    print("Which vegetable do you want?")
    vegetable_id=input("Please enter the vegetable number")
    selected_vegetable=int(vegetable_id)-1
    #read will wait for the user to type
    print("You have selected" , vegetables[selected_vegetable])
    #using if condition
    quantity=int(input("How much Quantity would you like of that vegetable"))
 
    cost_vegetable=vegetable_prices[selected_vegetable]
    expression="Your total is"
    total = int(quantity*cost_vegetable)
    item_info={"vegetable_id":selected_vegetable, "quantity":quantity, "total":total,"price":cost_vegetable}
    user_cart.append(item_info)
    
    user_continue=input("Do you want to continue shopping yes/no")
    
print("-"*30)

print(f"you have {len(user_cart)} items in your cart")

print('Name \t\t\t Quantity \t Unit Cost \t Total')
print('-'*100)
final_amount=0

# Using Counter Variable in the Loop
item_counter=1
for each_item in user_cart:
    vegetable_id = each_item["vegetable_id"]
    final_amount=final_amount + each_item['total']
    tab_code='\t\t\t'
    print ("{sno} {vname} {tab} {v[quantity]} {tab} {v[price]} {tab} {v[total]}".format(sno=item_counter,tab=tab_code,v=each_item,vname=vegetables[vegetable_id]))
    item_counter = item_counter + 1

    #print(f"{vegetables[vegetable_id]} \t\t\t {each_item['quantity']} \t\t\t {each_item['price']} \t\t\t {each_item['total']}")


# Using Range Counter inside the Loop

for item_counter in range(len(user_cart)):
    each_item = user_cart[item_counter]
    vegetable_id = each_item["vegetable_id"]
    final_amount=final_amount + each_item['total']
    tab_code='\t\t\t'
    print ("{sno}. {vname} {tab} {v[quantity]} {tab} {v[price]} {tab} {v[total]}".format(sno=item_counter,tab=tab_code,v=each_item,vname=vegetables[vegetable_id]))
    #print(f"{vegetables[vegetable_id]} \t\t\t {each_item['quantity']} \t\t\t {each_item['price']} \t\t\t {each_item['total']}")


# 
'''
/t gives a space
'''

print('-'*100)  
print(f"\t\t\t\t\t\t\t Total Amount : {final_amount}")
print('-'*100)

# Comment Synatax 
'''

dictionary : key value
array : collection of items

store some properties of an object : You should go for dictionary
if you want to store collectipn of object then array


box1[0][0][0][0]["fruit_name"] => apple
box1[0][0][0][1]["fruit_name"] => orange

box1=[

[
    [
        [
            {"fruit_name":"apple", "qty":10},
            {"fruit_name":"orange", "qty":12},
        ]
    ]
]

]


'''




    






