# #Python Numeric Data type

# num1 = 5
# print(num1, 'is of type', type(num1))

# num2 = 2.0
# print(num2, 'is of type', type(num2))

# num3 = 1+2j
# print(num3, 'is of type', type(num3))

# #Python List Data Type
# language = ["swift", "java", "python"]
# print(language[0])

# #Python Tuple Data Type
# product = ('microsoft', 'xbox', 499.99)
# print(product[0])

# #python string data type
# name = 'python'
# print(name)

# #Python Set Data Type
# student_id = {112, 114, 116, 118, 115}
# print(student_id)
# print(type(student_id))

# #Python Dictionary Data Type
# capital_city = {'somalia': 'mogadishu', 'italy': 'rome'}
# print(capital_city)
# print(capital_city['somalia'])

#Python Implicit Type Conversion
# integer_number = 123
# float_number = 1.23
# new_number = integer_number + int(float_number)
# print("valuue:", new_number)
# print("data type:", type(new_number))

#Explicit Type Conversion
num_string = '12'
num_integer = 23
print("data type of num_string before type casting:", type(num_string))
# explicit type conversion
num_string = int(num_string)
print("data type of num_string after type casting:", type(num_string))

num_sum = num_integer + num_string
print("sum:", num_sum)
print("data type of num_sum:", type(num_sum))