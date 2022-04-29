from math import degrees
import time
from CarnageEngine import Entity
from CarnageEngine.Camera import Camera
from CarnageEngine.Scene import Scene
from CarnageEngine.Vector import Vector
# from CarnageEngine.Window import Window
from CarnageEngine.Transform import Transform
"""This File is just for testing purpose, I am not ignoring this because it would be helpful"""

# class Test:
#     def __init__(self) -> None:
#         self.n = "meow"
    
#     def noobda(self):
#         print("noobda")

#     def OnExit(self):
#         print("bye")
    
#     def OnUpdate(self):
#         pass

# subject = Test()
# a = Entity("hah", [subject])
# a.noobda()

# scene = Scene(name="Default", children=[a])
# window = Window((500,500), {'a':scene}, 'a')

# while window.running:
#     window.Update()

# a = Vector(0,0,0)
# b = Vector(5, 5, 0)

# print(a.dot(b))
# print(a.distance(b))
# print(degrees(a.angle(b)))

t = Transform(Vector(5,5,2), angle=Vector(0,0,0), scale=Vector(4,4,4), anchor=Vector(5,5,2))
cam = Camera(Vector(4,3,10))
print(cam.convertCordinates(t))