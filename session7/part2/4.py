n=int(input("side?"))
m = 360/n
from turtle import *
color("orange")
speed(0)
for i in range(n):
    forward(m)
    left(m)

mainloop()