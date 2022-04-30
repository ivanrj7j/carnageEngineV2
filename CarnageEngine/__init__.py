from uuid import uuid4
import pickle

class Entity:
    def __init__(self, name, children:object =[]):
        self.id = str(uuid4().hex)
        self.name = name
        if name == "":
            self.name = id
        # assigning the name and id of the object 

        self.OnAwakeFunctions = []
        self.OnUpdateFunctions = []
        self.OnExitFunctions = []
        
        self.EventDictionary = {"OnAwake": self.OnAwakeFunctions, "OnUpdate": self.OnUpdateFunctions, "OnExit":self.OnExitFunctions}
        # creating the list of event functions 

        self.ChildrenList = []

        if len(children) > 0:
            for child in children:
                self.AppendChild(child)

        for awakeFunction in self.OnAwakeFunctions:
            awakeFunction()

    
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
        """
        with open(destination+"/"+self.name + "_"+ self.id+".carng", "wb") as saveFile:
            pickle.dump(self.__dict__, saveFile)

    @classmethod
    def InitiateFromFile(cls, file:str):
        with open(file, "rb") as saveFile:
            attributes = pickle.load(saveFile)
        for attribute in attributes:
            setattr(cls, attribute, attributes[attribute])
        return cls

    def Update(self,window,camera):
        """
        Runs Every time whenever there is an update to the frame
        """
        for updateFunction in self.OnUpdateFunctions:
            updateFunction(window, camera,self)

    def Exit(self):
        """
        Runs just before the applications closes and returns a summary of the object
        """
        for exitFunction in self.OnExitFunctions:
            exitFunction()

        return self.GetString()
