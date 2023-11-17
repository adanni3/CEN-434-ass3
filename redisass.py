import redis

r = redis.Redis(host='localhost', port=6379)
#write
g = r.mset({"name":"carl" , "class": "pry2 gold"})
#read
names= r.get("name")
class_name = r.get("class")

print(names)
print(class_name)

#update

r.mset({"name":"Nell"})
r.mset({"age":"12yrs"})

print(r.get("name"))
print(class_name)
print(r.get("age"))

#delete
r.delete("name")

print(r.get("name") )

