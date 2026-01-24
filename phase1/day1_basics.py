# Python variables

# Declaring variables
x = 7
y = "Carmen"
yY = False

# Showing them
print(x)
print(y)

# In Python, variables don't need to be declared in a specific type. You can change them their type anytime
# (Basically, Python expects us to be responsible adults that know of best practices)
z = 5       
z = "Marcus" 
print(x)

# Casting
a = str(4)    # '4'
b = int(4)    # 4
c = float(4)  # 4.0

# How to get the type of a variable?
d = 9
e = "Kayle"
print(type(d))
print(type(e))

# Case-Sensitive
f = 12
F = "Troy"
#F will not overwrite f

#Data types
# Text Type:	str 
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# input in Python
print('Enter your name:')
g = input()
print('Hello, ' + g)
# Another way
h = input('Enter your country: ')
print('You live in ' + h)

# Operators
i = 5 + 4
j = 12 - 5
k = 4 * 3
l = 10 / 2
m = 7 % 2
n = 4**2

# to do comparisons (the result is a boolean)
o = 2 == 2
p = 5 != 4
q = 4 > 6 
r = 10 < 20
s = 5 >= 5
t = 6 <= 5

# Some exercises

# Ask the user their name and age
name = input("Please, enter your name: ")
age = input("Now, please, enter your age: ")
print("Name: " + name + ", Age: " + age)

# How old will you be in 5 years?
age2 = int(input("Please, enter your age: "))
fiveYears = age2 + 5
print("In five years, you'll be ", fiveYears, " years old.")
print(f"In five years, you'll be {fiveYears} years old.") #Another way, using f-string


