# Slicing the String / toString

# The process of Slicing
# Indexing[] or slice()
# first index inclusive and last index is exclusive
# [start : stop : step]


name = "Ziaul Haque"
firstname = name[0]
firstName = name[0:5]
lastname = name[6: ]
funkyname = name[0:len(name):2]
reversedname = name[::-1]
website = "https://google.com"

slice = slice(8,-4)



print(firstname)
print(firstName)
print(lastname)
print(funkyname)
print(reversedname)
print(website[slice])