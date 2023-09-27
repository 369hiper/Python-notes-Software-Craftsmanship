# This is a program for declarative programming paradigm for finding out the sum of squares of even numbers in our list
# 1-10
sum_of_squares = sum(x**2 for x in range(11) if x % 2 == 0)
print(sum_of_squares)