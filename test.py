from math import degrees
import time
from CarnageEngine import Entity
from CarnageEngine.Camera import Camera
from CarnageEngine.Scene import Scene
from CarnageEngine.Vector import Vector
from CarnageEngine.Window import Window
from CarnageEngine.Transform import Transform
from CarnageEngine.Sprite import Sprite
"""This File is just for testing purpose, I am not ignoring this because it would be helpful"""

class Test:
    def __init__(self) -> None:
        self.n = "meow"
    
    def noobda(self):
        pass

    def OnExit(self):
        pass
    
    def OnUpdate(self, window, camera, this):
        # newPosition = Vector(this.Transform.position.x + 1, this.Transform.position.y+3, this.Transform.position.z+1)
        this.Transform.position.x+=1

subject = Test()
t = Transform(position=Vector(0,5,2), angle=Vector(50,230,122), scale=Vector(4,4,4), anchor=Vector(-5,5,2))
sprite = Sprite("test/bird.png", (50,50))
a = Entity("hah", [subject,t, sprite])

cam = Camera(position = Vector(0,0,0), angle=(Vector(0, 0, 0)))
scene = Scene(name="Default", children=[a], Camera=cam)
window = Window((500,500), {'a':scene}, 'a')

while window.running:
    window.Update()
