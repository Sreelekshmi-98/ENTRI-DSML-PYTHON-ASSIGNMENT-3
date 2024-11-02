import random
my_list = [random.randint(1, 100) for _ in range(5)]
print("List of 5 random numbers:", my_list)

my_list.extend([random.randint(1, 100) for _ in range(3)])
print("Updated list with 3 new values:", my_list)

for element in my_list:
    print(element)

    my_dict = {
        'name': 'John',
        'age': 25,
        'address': 'New York'
    }
    print("Dictionary:", my_dict)

    my_dict['phone'] = '1234567890'
    print("Updated dictionary with phone:", my_dict)
my_dict['phone'] = '1234567890'
print("Updated dictionary with phone:", my_dict)


my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

my_set.add(6)
print("Set after adding 6:", my_set)

my_set.discard(3)
print("Set after removing 3:", my_set)

my_tuple = (1, 2, 3, 4)
print("Tuple:", my_tuple)

print("Length of the tuple:", len(my_tuple))









