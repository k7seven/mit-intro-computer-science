'''
Tuples -> Sequence of something
       -> Collection of any data type
       -> Immutable
       -> Created with ()
'''

# usage
t = (2, "mit", 3)
print("tuple example:", t)

# can retrieve data with index
first_element = t[0]
last_element = t[-1]
print("first element:", first_element)
print("last_element", last_element)

# can concatenate
t += (9, 10, "k77", 2.0)
print("concatenated tuple:", t)

# can be sliced
second_and_last_element = t[1:3]
print("sliced tuple:", second_and_last_element)

# can get length with len
print("length of t:", len(t))

# cant modify, the example below gives an error
# t[1] = "new data"

# can be used to swap values
value1 = 0
value2 = 1
print("***before swap***")
print("value1:", value1)
print("value2:", value2)
swapped_tuple = (value2, value1) = (value1, value2)
print("***after swap***")
print("value1:", value1)
print("value2:", value2)

# can be used to return multiple valies within one object return from function
def power_of_two_numbers(x, y):
    result_x = x ** x
    result_y = y ** y
    tuple_result = (result_x, result_y)
    return tuple_result

tuple_return = power_of_two_numbers(2, 5)

print("two values in the same return of function:", tuple_return)
print("first element:", tuple_return[0])
print("second element:", tuple_return[1])

# tuples can contain other tuples
# this data has the date a person was hired at google and their names
data_tuple = ((2010, "k77"), (2001, "Jane"), (2016, "Bill"), (2012, "Steve"))

# this fuction is going to retrieve the names of employees from one year to year another
def get_employees_from_to(year1, year2, data):
    years = ()
    employees = ()
    for t in data:
        if(t[0] > year1 and t[0] < year2):
            years += (t[0],)
            employees += (t[1],)

    return (years, employees)

(years, employees) = get_employees_from_to(2010, 2020, data_tuple)
print(years)
print(employees)
