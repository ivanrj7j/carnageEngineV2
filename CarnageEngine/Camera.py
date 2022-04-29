from CarnageEngine.Transform import Transform
from CarnageEngine.Vector import Vector


class Camera:
    def __init__(self, position=Vector(0,0,0), fov=45) -> None:
        self.position = position
        self.fov = fov

    def convertCordinates(self, targetObj:Transform):
        w = self.position.distance(targetObj.position)
        # distance between object and camera
        return (targetObj.multiViewProjection[0]*(self.fov/w), targetObj.multiViewProjection[1]*(self.fov/w))
