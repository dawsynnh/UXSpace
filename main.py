import os
from httpserver import httpsserver

def generateRequiredHttpsDirectories():
    sPath = "sec/"
    iPath = "index/"
    cgiPath = "cgi-bin/"
    pyBinPath = "index/php/"

    isExist = os.path.exists(sPath)
    insExist = os.path.exists(iPath)
    cgiExist = os.path.exists(cgiPath)
    pyExist = os.path.exists(pyBinPath)

    if not isExist:
        os.makedirs(sPath)
        print("Generated security folder. Please Input your key and cert files as .pem !")

    if not insExist:
        os.makedirs(iPath)
        print("Generated index folder. Please place HTML/ CSS/ JS files within folder!")

    if not cgiExist:
        os.makedirs(cgiPath)
        print("Generated PHP cgi-bin folder. Please place PHP files in this folder & start service with PHP")

    if not pyExist:
        os.makedirs(pyBinPath)
        print("Generated Python CGI binary path, place python web applications in this folder!")

def startService(host, port):
    HOST = host
    PORT = port

    generateRequiredHttpsDirectories()

    usePHP = input("Would you like to use php (y/N)? ")

    if usePHP == "y":
        httpsserver.start_Server_PHP(HOST, PORT)
    else:
        httpsserver.start_Server(HOST, PORT)


if __name__ == '__main__':
    startWithArgs = input ("Would you like to use default settings for this service (y/N)? ")
    defaults = True

    if startWithArgs == "N":
        defaults = False
    else:
        defaults = True

    if not defaults:
        Host = input("Please enter a host IP to bind on... ")
        Port = input("Please enter a port to bind to host on...")

        print ("Passing arguments and starting service!")
        startService(Host, Port)
    else:
        startService("127.0.0.1", 8080)




