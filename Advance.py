instances = []
count = 0 
class connection(object):
    #create a new object if there is no object created
    #for this given type, else return the current object for the given protocol.
    # Static instance variable:
    _instance = None
    # it's same implemantition for getInstance but we have __new__ method in python 
    def __new__(cls):
        global count
     #   global _count
        # Check if an instance exists:
        if count < 3:
            count += 1
            if not cls._instance :
            # Create new instance:
                cls._instance = object.__new__(cls)
                instances.append(cls)
            return cls._instance
        else :
            print("Too many instances were created")
        
    
    def release(self):
        pass
    def send(self):
        pass
    
def getCurrentConnections():
        return instances
    
class http(connection):
    def send(self):
        print("sending my message via http" )
        pass
        #do smthing unique for this class
        # in this or other abstract method
        # also pearent method can be called with help of super
    def release(self) : 
        print(self._instance)
        del connection._instance
        print("died")

class scp(connection):
    def send(self):
        print("sending my message via scp ")
        pass
        
    def release(self) :
        del connection._instance
        
        print("died")
class ssh(connection):
    def send(self):
        print("sending my message via ssh" )
        pass
    
    def release(self) :
        del connection._instance
        print("died")
class telnet(connection):
    def send(self):
        print("sending my message via telnet ")
        pass

    def release(self) :
        del connection._instance
        print("died")    
class ftp(connection):
    def send(self):
        print("sending my message via ftp" )
        pass
        #do smthing unique for this class
        # in this or other abstract method
        # also pearent method can be called with help of super
    def release(self) :
        del connection._instance
        print("died")



def main():
    a1 = http()
    a2 = http()
    b1 = scp()
    b2 = scp()
    c1 = telnet()
    if a1 == a2 :
        print("true")     
    a1.release()
    b1.send()
    if a1 == a2 :
        print("true")
    if b1 == a1:
        print("truuue")
    else : print("not")
    print(getCurrentConnections())



if __name__ == "__main__":
    main()
