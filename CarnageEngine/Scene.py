import pickle
from uuid import uuid4
from CarnageEngine import Entity
from CarnageEngine.Camera import Camera


class Scene:
    def __init__(self, name="", children=[], Camera=Camera()) -> None:
        """
        The parent Object of all the Entity in a particular Scene This Helps for dynamic scene changing.

        :param str name: The name of the Scene (default "")
        :param list children: The list of all children in the scene (default [])
        :param Camera Camera: The camera used in the scene (default Camera())
        """
        self.id = str(uuid4().hex)
        self.name = name
        if name == "":
            self.name = id
        self.children = children
        self.camera = Camera

    def AppendChild(self, child:Entity):
        """
        Appends a child entity

        :param Entity child: The child which to append
        """
        self.children.append(child)

    def Update(self, parent):
        """
        Runs every time the frame is refreshed
        :param Window parent: The window object on which the scene is running on
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

        :param str destination: The file path to where the file should be saved
        """
        with open(destination+"/"+self.name + "_"+ self.id+".carng", "wb") as saveFile:
            pickle.dump(self.__dict__, saveFile)

    @classmethod
    def InitiateFromFile(cls, file:str):
        """
        Reads the File and creates itself with the given attributes in the files

        :param str file: The path to the file
        """
        with open(file, "rb") as saveFile:
            attributes = pickle.load(saveFile)
        for attribute in attributes:
            setattr(cls, attribute, attributes[attribute])
        return cls