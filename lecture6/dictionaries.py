# key-value pairs


# starting a dictionary
student = {'name': 'k77', 'age': '31', 'courses': ['Math', 'CS']}

# can retrieve the value using the key
name = student['name']
print(name)

# keys can also be integers
key_times_2 = {1: 2, 2: 4}
print(key_times_2[1])

# trying to access a key that doesnt exist gives an KeyError
# uncoment below to test
# print(student["wont_work"])

# but if we use get if returns None or we can pass a second argument as the default return of a not found key
print(student.get('wont_work', 'default return'))

# we can asign a new key-value as shown below
student['phone'] = '555-5555'
print(student['phone'])

# we can also update a value of a key the same way
student['age'] = '21'
print(student['age'])

# we can use update() to update multiple keys
student.update({'name': '77k', 'courses': ['Math', 'CS', 'YouTube']})
print(student)

# we can use del to delete a key
# uncomment below to test
# del student['age']
# print('student after del:', student)

# we can also use pop same as lists
age = student.pop('age')
print(student)
print(age)

# we can get the length of a dictionary
print(len(student))

# we can get only the keys
print(student.keys())

# we can get only the values
print(student.values())

# we can get both
print(student.items())

# we can iterate through the dictionary
for key in student:
    print(key)

# to get both key and value we must plug items
for key, value in student.items():
    print('key:', key, '- value:',  value)
