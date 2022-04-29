import pickle
from uuid import uuid4
from CarnageEngine import Entity
from CarnageEngine.Camera import Camera


class Scene:
    def __init__(self, name="", children=[], Camera=Camera()) -> None:
        self.id = str(uuid4().hex)
        self.name = name
        if name == "":
            self.name = id
        self.children = children
        self.camera = Camera

    def AppendChild(self, child:Entity):
        """
        Appends a child entity
        """
        self.children.append(child)

    def Update(self, parent):
        """
        Runs every time the frame is refreshed
        """
        self.camera.Update(self.children, parent)
    
    def Exit(self):
        """
        Runs just before the applications closes and returns a summary of the object 
        """
        if len(self.children) > 0:
            for child in self.children:
                child.Exit()
        return self.GetString()

    def GetString(self):
        """
        Returns every information of the class in a string
        """
        return pickle.dumps(self.__dict__)

    def CreateSave(self, destination:str):
        """
        Saves itself in the given destination
        """
        with open(destination+"/"+self.name + "_"+ self.id+".carng", "wb") as saveFile:
            pickle.dump(self.__dict__, saveFile)
