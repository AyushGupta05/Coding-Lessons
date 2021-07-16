ayush={"name":"ayush","weight":45,"boxes":[{"title":"apples","count":10},{"title":"oranges","count":15},{"title":"banana","count":20}]}
abhinav={"name":"Abhinav", "weight":55,"boxes":[{"title":"potato","count":10},{"title":"tomato","count":15},{"title":"onion","count":20}]}
manisha={"name":"saurabh", "weight":70,"boxes":[{"title":"dairy milk","count":10},{"title":"cadbury","count":15},{"title":"star","count":20}]}
saurabh={"name":"manisha", "weight":90,"boxes":[{"title":"tennis racket","count":1},{"title":"tennis ball","count":15},{"title":"tennis shoes","count":2}]}
big_box=[ayush,abhinav,manisha,saurabh]
print(big_box[0]["name"],big_box[0]["weight"])
print(big_box[1]["name"],big_box[1]["weight"])
print(big_box[2]["name"],big_box[2]["weight"])
print(big_box[3]["name"],big_box[3]["weight"])
for it in big_box:
    print("="*25)
    box_name=it["name"]
    print(box_name.upper(),it["weight"])
    print("="*25)
    for mini_box in it["boxes"]:
        print(mini_box["title"])