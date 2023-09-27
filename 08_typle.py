x = (12, 232, 323, 656)
y = list(x)
print(type(y))
y[1] = 122
print("Before clear()",y)
y.clear()
print("After clear()",y)


# Copy Methods

z = y.copy()
print(z)
