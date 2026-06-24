print(10 + 10)
print('my height is:', 1.75)
print('complex number', 2 - 1j)
a = float(input('enter base:' ))
b = float(input('enter height:' ))
print('the area is:', 0.5 * a * b) 
a = float(input('enter side a:' ))
b = float(input('enter side b:' ))
c = float(input('enter side c:' ))
print('the perimetre of the trianle:', a + b + c)
a = float(input('enter lenght:' ))
b = float(input('enter width:' ))
print('the area of the rectangle:', a * b)
print('the perimeter of the rectangle:', 2 * (a + b))
x = float(input('enter the radius of the circle' ))
print('the area of the circle is', 3.14 * (x**2))
print('the circumference of the circle is', 2 * 3.14 * x)
#equation = y = 2x - 2
slope1 = 2
x_intercept = 1
y_intercept = -2
print("the slope1 is:", slope1) 
print("x-intercept is:", x_intercept) 
print("y-intercept is:", y_intercept) 
y2, y1 = 2, 2
x2, x1 = 6, 10
slope2 = (y2 - y1) / (x2 - x1)
euclidean_distance = ((y2 - x2)**2 + (y1 - x1)**2)**0.5 
print("the slop2 is:", slope2) 
print("the euclidean distance is:", euclidean_distance)
print(slope1 > slope2) 
print(slope1 == slope2) 
print(slope1 < slope2) 
a = 1
b = 6
c = 9
discriminant = b**2 - 4*a*c
if discriminant > 0: print(((-b - discriminant**0.5)/(2*a)), ((-b + discriminant**0.5)/(2*a)))
elif discriminant == 0: print(-b/(2*a))
else: print("cette équation n'a pas de racines") 
print(len('python') <= len('dragon')) 
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in ' I hope this course is not full of jargon')
print('on' in 'dragon' and 'on' in 'python')
print(float(len('python')), str(len('python')))
x = int(float(input('enter number' )))
if x % 2 == 0:
    print('x is even')
else: print('x is not even')
print(7//3 == int(2.7)) 
print(type(10) == type('10'))
print(int(float(9.8)) == 10)
x = float(input('enter your worked hours' ))
y = float(input('enter your rate per hour' ))
print('Your weekly earning is:', x * y)
z = int(input('enter number of years you have lived:' ))
print('You have lived for', z*60*60*24*365, 'seconds')
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125) 