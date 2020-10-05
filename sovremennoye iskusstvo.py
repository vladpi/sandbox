from random import *
from turtle import *
width(5)
a = [['spring green', 'light sky blue', 'wheat'],['navy', 'lime', 'dark orange'],['maroon', 'purple', 'aquamarine']]
l = 0
b = choice(a)
color(choice(b))
n = int(input('Сколько линий? '))
x = choice(list(range(-300, 300)))
y = choice(list(range(-300, 300)))
while l < n:
    goto(x, y)
    color(choice(b))
    width(randint(1, 15))
    x = choice(list(range(-300, 300)))
    y = choice(list(range(-300, 300)))
    l += 1
exitonclick()