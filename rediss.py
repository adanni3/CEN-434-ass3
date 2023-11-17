import redis
import time

r = redis.Redis(host="localhost",port=6379)

#create
def create():
    key = input("input key name:")
    if not r.exists(key):
        name = input("input name:")
        l_name = input("input lastname:")
        mat_no = input("input Mat_No:")
        score = input("input class score:")
    else:
        print("key already exist")

    person_info = {
        'name' : name,
        'l_name' : l_name,
        'mat_no' : mat_no,
        'score' : score
    }

    value = str(person_info)

    r.set( key, value)
    print(f"created key: {key}: value: {value}")
    time.sleep(2.5)

#read
def read():
    key = input("Enter key to read: ")
    value = r.get(key)
    if value:
        print(f"Value for key {key}: {value.decode('utf-8')}")
    else:
        print(f"Key {key} not found")
    time.sleep(2.5)
#update
def update():
    key = input("Enter key to update: ")
    firstname = input("Enter updated first name: ")
    lastname = input("Enter updated last name: ")
    matric_no = input("Enter updated matriculation number: ")

    # Create a dictionary to store updated person's information
    person_info = {
        'firstname': firstname,
        'lastname': lastname,
        'matricno': matric_no
    }

    # Convert dictionary to a string for storage in Redis
    new_value = str(person_info)

    if r.exists(key):
        r.set(key, new_value)
        print(f"Updated value for key {key}: {new_value}")
    else:
        print(f"Key {key} not found, cannot update")
    time.sleep(2.5)

#delete
def delete():
    key = input("input key to be deleted:")
    if r.exists(key):
        r.delete(key)
        print("key has been deleted")
    else:
        print("key does not exist")
    time.sleep(2.5)

while True:
    print('\n Options:')
    print('1.create')
    print('2.read')
    print('3.update')
    print('4.delete')
    print('5.exit')
    choice = input("Enter your choice(1-5)")

    if choice == '1':
        create()
    elif choice == '2':
        read()
    elif choice == '3':
        update()
    elif choice == '4':
        delete()
    elif choice == '5':
        print('exitting code')
        break
    else:
         print('invalid response. Enter choice(1-5).')