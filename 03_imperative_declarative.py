# Finding out squares of a given number, given the fact that it's even, We sum the square we found out

# Using IMPERATIVE Paradigm trying to achieve this goal.

# Declaraing an empty list
x = [1,3,6,12,15,18,21]

even_numbers = []


# Checking if a number is even
for i in x:
    print("I am in for Condition and I value is ",i)
    print(i)
    if i % 2 == 0:
        even_numbers.append(i)
        print("This is the current even number I have found ",i)
        
print(even_numbers)


# Finding out the square of these numbers appended.

# Let's initialize a variable to store the sum of squared values
sum_of_squares = 0

# Loop over the even_numbers and sum the  squares of those values

for num in even_numbers:
    sum_of_squares += num ** 2
    print("This is the current sitation ",sum_of_squares)

print(sum_of_squares)
y= "Hello"
print("This is the length of x list",len(x))
print("This is the length of y list",len(y))



