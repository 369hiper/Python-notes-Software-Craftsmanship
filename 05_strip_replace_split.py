# Removing White and Trailing spaces

text = "..............grtrereerererer.Banana..............grtrereerererer."
print(text)

x = text.strip(".gert")

# print("Out of all the fruits", x, "is my favoritee")

print("This is my actual string",x)
y = x.lower()
print("This is my y variable, which is in lower case",y)
z = y.upper()
print("This is my z variable, which is in Upper case",z)

# Let's say that I will want to replace bananas with apples
a = z.replace("BANANA", "Apples")
print("Bananas have been replaed with ",a)

# Understanding the Split function
listoffruits = "Apple#oranges#bananas#pears"

c = listoffruits.split("#",10)
print("This is my split",c)
