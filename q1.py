'''
Question 1
Crmeate a fully comented program to:
Ask a user for a number of degrees between 0 and 360.
The program should output the value of the sine, cosine and tangent of the angle.
(Hint: you might need to convert degrees to radians first!!)
'''
import math

num = (int(input("Choose the number of degrees between 0 and 360? \n")))
print("Your number Degrees is equal to Radians : ", end="")
print(math.radians(num))
print("The value of sine is : ", end="")
print(math.sin(num))
print("The value of cosine is : ", end="")
print(math.cos(num))
print("The value of tangent is : ", end="")
print(math.tan(num))

