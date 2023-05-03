#this problem will need to read integers from an input (we need to produce an integer from a string)
#challenge is to calculate the volume of a right circular cone
#input will consist of two lines of text
#line one will be r for radius of the cone
#line two will be h for height of the cone
#values for both will be between 1 and 100
#we need the output to be the volume of the right circular cone with r and h       formula is (pi,rsquared,h)/3
#use 3.141592653589793 for pi
#since we don't want the value of pi to change we'll make it a constant, to do this in python we can
#use all caps in naming the variable (PI instead of pi)
# to create an exponent use the ** operator
PI = 3.141592653589793
# r = input()
# h = input()
#input ALWAYS returns a string, so we need to convert this to an int
#we can use the int function instead and combine int and input into one line like below

radius = int(input())
height = int(input())
volume = (PI * radius ** 2 * height)/3
print(volume)

#in summary we created a variable called pi for an approximation of the pi value, 
# read the radius and height from an input and converted the string to an int, 
# then used the formula for the volume of a right circular cone to calculate the volume, 
# and output the volume