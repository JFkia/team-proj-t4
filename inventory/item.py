class item():
    def __init__(self,assertTag,description):
        self._assertTag = assertTag
        self._description = description
        self._dueDate = ""
        self._isAvailable = True
    
    def getAssertTag(self):
        return self._assertTag
    
    def getDescription(self):
        return self._description
    
    def getDueDate(self):
        return self._dueDate
    
    def getIsAvailable(self):
        if self._isAvailable:
            return "Yes"
        else:
            return "No"
    def setDueDate(self, dueDate):
        self._dueDate =dueDate
    
    def setIsAvailable(self,isAvailable):
        self._isAvailable = isAvailable
    
    def _str_ (self):
        return "{:<10}{:<30}{:<10}{:<12}".format(
            self.getAssertTag(),self.getDescription(),
            self.getIsAvailable(), self.getDueDate()
        )