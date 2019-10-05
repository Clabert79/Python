import turtle
from math import sin, pi

def arco(t,raggio,angolo):
	for i in range(90):
		t.fd(raggio)
		t.lt(angolo/90)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


bob = turtle.Turtle()
petal(bob,6,27)
print(bob)

turtle.mainloop()