print('Bismillah')

# How the veriable work
x = 21
name = 'Ziual Haque'

## We are printing the output
print(x)
print(name)

""""this is a multi line comment 
in the Pythone Programm
But you can also use the Conjugative pound (#) sign
"""
print(type(x))
print(type(name))

FirstName = 'Ziaul'
Lastname = 'Haque'
print(Lastname +" " + Lastname)
fullName = FirstName +" "+ Lastname
print("Hello " + fullName)

# Is it possible that number could be String and int both
# at the same time?

age = 21
age1 = "21"

print(type(age))
print(type(age1 ))

age = age +1
print(age)

age += 1
print(age)

age1 += age1
print(age1)

#You can't show the veriable as a string comment as well
#print("Your age is : " + age)

# You have to do
# You have to add teh data type before the veriable then
print("Your age is : " + str(age))
print()

# FLoat data type
height = 134.5
print("your height is : " + str(height))

# Boolean data type
human = False
print(human)
print(type(human))