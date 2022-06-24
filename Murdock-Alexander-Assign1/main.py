import math

mass = 0.065
gravity = 9.8
print("Input the distance to professor")
distance = float(input())
kilometers = 25
print("Now input the value for theta")
theta = float(input())

equation = math.sqrt(mass*gravity*distance/(kilometers*math.sin(2*math.radians(theta))))
print(equation, 'meters')