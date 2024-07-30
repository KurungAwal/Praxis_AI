a = 5 
b = 3

# a+= 3 is same as a=a+3

# before
print(a)
print("First modulus: ", a % b)

a += 3

# after

print(a)
print("Second modulus: ", a % b)