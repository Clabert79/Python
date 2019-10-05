import turtle
from math import sin, pi

def rombo(t,lungezza,angolo):
	for i in range(4):
		t.fd(lungezza)
		t.lt(90 - angolo)


def quadrato(t,lungezza):
	for i in range(4):
		t.fd(lungezza)
		t.lt(90)

def poligono(t,lungezza,n):
	angolo = 360 / n
	for i in range(n):
		t.fd(lungezza)
		t.lt(angolo)

def cerchio(t,r):
	poligono(t,r,90)

def arco(t,raggio,angolo):
	for i in range(90):
		t.fd(raggio)
		t.lt(angolo/90)

def stella(t):
	for i in range(5):
		t.forward(150)
		t.right(144)
    	t.right(144)

def cuore(size, shape):
    turtle.pensize(10)
    radius = size * sin(shape * pi / 180) / (1 + sin((90 - shape) * pi / 180))
    turtle.right(shape)
    turtle.forward(size)
    turtle.circle(radius, 180 + shape)
    turtle.right(180)
    turtle.circle(radius, 180 + shape)
    turtle.forward(size)
    turtle.left(180 - shape)

bob = turtle.Turtle()

rombo(bob,15,45)
# cuore(60,60)

# quadrato(bob,150)
# poligono(bob,50,10)
# cerchio(bob,10)
# arco(bob,6,270)
print(bob)

turtle.mainloop()