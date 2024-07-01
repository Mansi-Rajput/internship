class SingletonMeta(object):
  def __init__(self,ftype):
      self.ftype =ftype #Storing the provided type("Doubleton" in this case)

  def getFtype(self):
      return self.ftype #Return the stored type

def mainz():
    fType = SingletonMeta(ftype = "Doubleton") #Create a SingletonMeta instance
    print(fType.getFtype())

main()
