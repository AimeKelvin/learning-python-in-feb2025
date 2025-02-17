import math

a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
#let us call our hypothenus var 'c'
c = round(math.sqrt(pow(a,2) + pow(b,2)), 2)

print(f"The hypothenus of your triangle is {c}")
