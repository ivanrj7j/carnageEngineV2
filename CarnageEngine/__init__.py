from uuid import uuid4
import pickle

class Entity:
    def __init__(self, name, children:object =[]):
        self.id = str(uuid4().hex)
        self.name = name
        if name == "":
            self.name = id

        self.ChildrenList = []

        if len(children) > 0:
            for child in children:
                self.AppendChild(child)
                #append every child

        for child in self.ChildrenList:
            if "OnAwake" in dir(child):
                child.OnAwake()
                # calling the OnAwake function of all children 

    
    def AppendChild(self, child:object):
        """
        Appends a child to the class in runtime
        """
        setattr(self, type(child).__name__, child)
        self.ChildrenList.append(child)

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

    def Update(self,window,camera):
        """
        Runs Every time whenever there is an update to the frame
        """
        for child in self.ChildrenList:
            if "OnUpdate" in dir(child):
                child.OnUpdate(window, camera, self)

    def Exit(self):
        """
        Runs just before the applications closes and returns a summary of the object
        """
        for child in self.ChildrenList:
            if "OnExit" in dir(child):
                child.OnExit()

        return self.GetString()
