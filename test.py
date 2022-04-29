from math import degrees
import time
from CarnageEngine import Entity
from CarnageEngine.Camera import Camera
from CarnageEngine.Scene import Scene
from CarnageEngine.Vector import Vector
from CarnageEngine.Window import Window
from CarnageEngine.Transform import Transform
"""This File is just for testing purpose, I am not ignoring this because it would be helpful"""

class Test:
    def __init__(self) -> None:
        self.n = "meow"
    
    def noobda(self):
        print("noobda")

    def OnExit(self):
        print("bye")
    
    def OnUpdate(self, window, camera, parent):
        parent.position.x += 10

subject = Test()
t = Transform(Vector(5,5,2), angle=Vector(0,0,0), scale=Vector(4,4,4), anchor=Vector(5,5,2))
a = Entity("hah", [t,subject])
a.noobda()

cam = Camera(position = Vector(4,3,10))
scene = Scene(name="Default", children=[a], Camera=cam)
window = Window((500,500), {'a':scene}, 'a')

while window.running:
    window.Update()

# a = Vector(0,0,0)
# b = Vector(5, 5, 0)

# print(a.dot(b))
# print(a.distance(b))
# print(degrees(a.angle(b)))

# cam = Camera(Vector(4,3,10))
# print(cam.convertCordinates(t))