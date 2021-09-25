##################################################################################################################
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
         #global _count
        # Check if an instance exists:
        if count < 3:
            count += 1
            print(count , " . " , " new instance created")
            if not cls._instance :
            # Create new instance:
                cls._instance = object.__new__(cls)
                instances.append(cls._instance)
            return cls._instance
        else :
            print("Too many instances were created")
        
    
    def release(self):
        global count
        instances.remove(self)
        self._instance = None
        count = count - 1
        print("died")
        pass
    def send(self):
        pass
    
def getCurrentConnections():
        return instances
##############################################################################################################
class http(connection):
    def send(self):
        print("sending my message via http" )
        pass

##############################################################################################################
class scp(connection):
    def send(self):
        print("sending my message via scp ")
        pass
###############################################################################################################
class ssh(connection):
    def send(self):
        print("sending my message via ssh" )
        pass
###############################################################################################################               
class telnet(connection):
    def send(self):
        print("sending my message via telnet ")
        pass
##############################################################################################################
class ftp(connection):
    def send(self):
        print("sending my message via ftp" )
        pass
########################################### MAIN FUNCTION ############################################################
def main():
    print("-------------------------MAIN AND SOME TEST CASES-------------------------------")
    http1 = http()
    http2 = http()
    scp1 = scp()
    # no more three connections
    print("* create new connection - more than three : ")
    telnet1 = telnet()
    print("--------------------------------------------------------")
    #First test case :
    print ( "* http1 == http2 ??? ")
    if http1 == http2 :
        print("true") 
    print("--------------------------------------------------------")
    # send function
    print( "* calling send() method ")
    scp1.send()
    print("--------------------------------------------------------")
    #second test case
    print("* scp1 == http1 ??? ")
    if scp1 == http1:
        print("true")
    else : print("False")
    print("--------------------------------------------------------")
    # object delete
    print("* Delete http object and create new one : ")
    http1.release()
    telnet1 = telnet()
    print("--------------------------------------------------------")
    #print list of current connections 
    print( "* list of our current connections : ")
    x = getCurrentConnections()
    print("["," , ".join([str(i.__class__.__name__ ) for i in x]) , "]")

####################################################################################################################
if __name__ == "__main__":
    main()
