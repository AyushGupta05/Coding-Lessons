    
location="kitchen"
cuboard_count=5
cuboard_size=45.3
total_vegetables_cast=76.500000000000023
total_kitchenboxes=75421321412131
fruits=["apple", "mango", "grapes", "banana", "lichi", "guavas"]
brand_rating={"amazon":8,"flipkart":6,"ebay":5}
print(location)
print(cuboard_count)
print(cuboard_size)
print(total_vegetables_cast)
print(total_kitchenboxes)
print(brand_rating)
print(type(location))
print(type(cuboard_count))
print(type(cuboard_size))
print(type(total_vegetables_cast))
print(type(total_kitchenboxes))
print(type(fruits))
print(type(brand_rating))
class_school={"class eight":["a","b"],"class nine":["b"],"class ten":["b","c","d","e"]}
print(class_school)
student_1={"name":"ayush","age":13,"doj":2016}
student_2={"name":"aarav","age":15,"doj":2011}
student_3={"name":"arjun","age":9,"doj":2019}
student_list=[student_1,student_2,student_3,{"name":"nimral","age":40,"doj":2021}]
print(len(student_list))

ayush={"name":"ayush","weight":45,"boxes":[{"title":"apples","count":10},{"title":"oranges","count":15},{"title":"banana","count":20}]}
abhinav={"name":"Abhinav", "weight":55,"boxes":6}
manisha={"name":"saurabh", "weight":70,"boxes":7}
saurabh={"name":"manisha", "weight":90,"boxes":10}
big_box=[ayush,abhinav,manisha,saurabh]
print(big_box[0]["name"],big_box[0]["weight"])
print(big_box[1]["name"],big_box[1]["weight"])
print(big_box[2]["name"],big_box[2]["weight"])
print(big_box[3]["name"],big_box[3]["weight"])
for it in big_box:
    print(it["name"],it["weight"])
