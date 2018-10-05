from turtle import*
colormode(255)
for i in range (20):
    color(255,i*100,0)
    print(i)
    for j in range(4):
        forward(100)
        left(90)

    left(30)



mainloop()