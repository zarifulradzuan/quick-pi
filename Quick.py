import qclass
import people_counter
import time
import threading
import requests
totalIn = 0
totalOut = 0
quickProcess = qclass.Quick()
quickProcess.start()
userInput = 1
params = {'valueToAdd':2,'placeId':'mcdonald-mitc'}
httpRequest = requests.post('https://aesuneus.000webhostapp.com/qservice.php', params)
while(userInput!=0):
    print("Counter is now running\n")
    print("Enter 0 to end processes\n")
    userInput = input("Enter option: ")
    if(userInput==0):
        print("Ending process..")
        quickProcess.stop()
