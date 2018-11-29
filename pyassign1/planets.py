#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import math

Sun = turtle.Turtle()
Sun.shape("circle")
Sun.color("yellow")

Mercury = turtle.Turtle()
a1 = 70
b1 = 68
c1 = (a1**2-b1**2)**0.5
Mercury.shape("circle")
Mercury.speed(0)
Mercury.color('blue')
Mercury.penup()
Mercury.goto ((a1-c1),0)
Mercury.pendown()

Venus = turtle.Turtle()
a2 = 110
b2 = 105
c2 = (a2**2-b2**2)**0.5
Venus.shape("circle")
Venus.speed(0)
Venus.color('orange')
Venus.penup()
Venus.goto (a2-c2,0)
Venus.pendown()

Earth = turtle.Turtle()
a3 = 140
b3 = 135
c3 = (a3**2-b3**2)**0.5
Earth.shape("circle")
Earth.speed(0)
Earth.color('sea green')
Earth.penup()
Earth.goto (a3-c3,0)
Earth.pendown()

Mars = turtle.Turtle()
a4 = 170
b4 = 165
c4 = (a4**2-b4**2)**0.5
Mars.shape("circle")
Mars.speed(0)
Mars.color('red')
Mars.penup()
Mars.goto (a4-c4,0)
Mars.pendown()

Jupiter = turtle.Turtle()
a5 = 200
b5 = 195
c5 = (a5**2-b5**2)**0.5
Jupiter.shape("circle")
Jupiter.speed(0)
Jupiter.color('purple')
Jupiter.penup()
Jupiter.goto (a5-c5,0)
Jupiter.pendown()

Saturn = turtle.Turtle()
a6 = 230
b6 = 225
c6 = (a6**2-b6**2)**0.5
Saturn.shape("circle")
Saturn.speed(0)
Saturn.color('brown')
Saturn.penup()
Saturn.goto (a6-c6,0)
Saturn.pendown()

for angle in range(3600):
    
    x1 = a1*math.cos(math.radians(angle))-c1
    y1 = b1*math.sin(math.radians(angle))
    Mercury.goto (x1,y1)
    
    x2 = a2*math.cos(math.radians(angle*0.85))-c2
    y2 = b2*math.sin(math.radians(angle*0.85))
    Venus.goto (x2,y2)
    
    x3 = a3*math.cos(math.radians(angle*0.7))-c3
    y3 = b3*math.sin(math.radians(angle*0.7))
    Earth.goto (x3,y3)
    
    x4 = a4*math.cos(math.radians(angle*0.5))-c4
    y4 = b4*math.sin(math.radians(angle*0.5))
    Mars.goto (x4,y4)
    
    x5 = a5*math.cos(math.radians(angle*0.35))-c5
    y5 = b5*math.sin(math.radians(angle*0.35))
    Jupiter.goto (x5,y5)
    
    x6 = a6*math.cos(math.radians(angle*0.2))-c6
    y6 = b6*math.sin(math.radians(angle*0.2))
    Saturn.goto (x6,y6)


# In[1]:


import turtle

Sun = turtle.Turtle()
Sun.shape("circle")
Sun.color("yellow")

for x in range(2):
    planets=['Mercury','Venus','Earth','Mars','Jupiter','Saturn']
    colors=['blue','orange','sea green','red','purple','brown']
    planet = planets[x]
    planetcolor = colors[x]
    a = 100*x+100
    b = 30*x+30
    c = (a**2-b**2)**0.5
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(planetcolor)
    planet.penup()
    planet.goto (a,0)
    planet.pendown()


# In[4]:


for x in range(5):
    planets=['Venus','Earth','Mars','Jupiter','Saturn']
    colors=['orange','sea green','red','purple','brown']
    planet = planets[x]
    planetcolor = colors[x]
    print(planet,planetcolor)


# In[1]:


import turtle
import math

i = turtle.Turtle()

def drawoval(planet,a,b,):
    for angle in range(3600):
        x = 100*math.cos(math.radians(angle))-(100**2-50**2)**0.5/2
        y = 50*math.sin(math.radians(angle))
        planet.goto (x,y)

i = drawoval(i.100.50)


# In[15]:


import math
print(math.tan(math.radians(45)))


# In[22]:


import turtle
i=turtle.Turtle
i.goto(100,100)


# In[ ]:


import turtle
import math

Sun = turtle.Turtle()
Sun.shape("circle")
Sun.color("yellow")

def planetsetting(a,b,color)
    

Mercury = turtle.Turtle()
a1 = 70
b1 = 68
c1 = (a1**2-b1**2)**0.5
Mercury.shape("circle")
Mercury.speed(0)
Mercury.color('blue')
Mercury.penup()
Mercury.goto ((a1-c1),0)
Mercury.pendown()


for angle in range(3600):
    
    x1 = a1*math.cos(math.radians(angle))-c1
    y1 = b1*math.sin(math.radians(angle))
    Mercury.goto (x1,y1)
    
    x2 = a2*math.cos(math.radians(angle*0.85))-c2
    y2 = b2*math.sin(math.radians(angle*0.85))
    Venus.goto (x2,y2)
    
    x3 = a3*math.cos(math.radians(angle*0.7))-c3
    y3 = b3*math.sin(math.radians(angle*0.7))
    Earth.goto (x3,y3)
    
    x4 = a4*math.cos(math.radians(angle*0.5))-c4
    y4 = b4*math.sin(math.radians(angle*0.5))
    Mars.goto (x4,y4)
    
    x5 = a5*math.cos(math.radians(angle*0.35))-c5
    y5 = b5*math.sin(math.radians(angle*0.35))
    Jupiter.goto (x5,y5)
    
    x6 = a6*math.cos(math.radians(angle*0.2))-c6
    y6 = b6*math.sin(math.radians(angle*0.2))
    Saturn.goto (x6,y6)


# In[ ]:


import turtle
import math

Sun = turtle.Turtle()
Sun.shape("circle")
Sun.color("yellow")

def planetparameter(planetname,a,b,color)



Mercury = turtle.Turtle()
a1 = 70
b1 = 68
c1 = (a1**2-b1**2)**0.5
Mercury.shape("circle")
Mercury.speed(0)
Mercury.color('blue')
Mercury.penup()
Mercury.goto ((a1-c1),0)
Mercury.pendown()

Venus = turtle.Turtle()
a2 = 110
b2 = 105
c2 = (a2**2-b2**2)**0.5
Venus.shape("circle")
Venus.speed(0)
Venus.color('orange')
Venus.penup()
Venus.goto (a2-c2,0)
Venus.pendown()

Earth = turtle.Turtle()
a3 = 140
b3 = 135
c3 = (a3**2-b3**2)**0.5
Earth.shape("circle")
Earth.speed(0)
Earth.color('sea green')
Earth.penup()
Earth.goto (a3-c3,0)
Earth.pendown()

Mars = turtle.Turtle()
a4 = 170
b4 = 165
c4 = (a4**2-b4**2)**0.5
Mars.shape("circle")
Mars.speed(0)
Mars.color('red')
Mars.penup()
Mars.goto (a4-c4,0)
Mars.pendown()

Jupiter = turtle.Turtle()
a5 = 200
b5 = 195
c5 = (a5**2-b5**2)**0.5
Jupiter.shape("circle")
Jupiter.speed(0)
Jupiter.color('purple')
Jupiter.penup()
Jupiter.goto (a5-c5,0)
Jupiter.pendown()

Saturn = turtle.Turtle()
a6 = 230
b6 = 225
c6 = (a6**2-b6**2)**0.5
Saturn.shape("circle")
Saturn.speed(0)
Saturn.color('brown')
Saturn.penup()
Saturn.goto (a6-c6,0)
Saturn.pendown()

for angle in range(3600):
    
    x1 = a1*math.cos(math.radians(angle))-c1
    y1 = b1*math.sin(math.radians(angle))
    Mercury.goto (x1,y1)
    
    x2 = a2*math.cos(math.radians(angle*0.85))-c2
    y2 = b2*math.sin(math.radians(angle*0.85))
    Venus.goto (x2,y2)
    
    x3 = a3*math.cos(math.radians(angle*0.7))-c3
    y3 = b3*math.sin(math.radians(angle*0.7))
    Earth.goto (x3,y3)
    
    x4 = a4*math.cos(math.radians(angle*0.5))-c4
    y4 = b4*math.sin(math.radians(angle*0.5))
    Mars.goto (x4,y4)
    
    x5 = a5*math.cos(math.radians(angle*0.35))-c5
    y5 = b5*math.sin(math.radians(angle*0.35))
    Jupiter.goto (x5,y5)
    
    x6 = a6*math.cos(math.radians(angle*0.2))-c6
    y6 = b6*math.sin(math.radians(angle*0.2))
    Saturn.goto (x6,y6)

