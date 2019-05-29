
import json
import requests
import time
import threading
import os
import people_counter

class Quick(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_thread= False
        self.counter = people_counter.PeopleCount("prototxt.prototxt", "model.caffemodel", 0.4, 30)
        self.currentDiff = 0
        if(os.path.isfile("config.txt")):
            print("Config file found, loading from file..")
            config = json.load(open("config.txt", "r"))
            config = config[0] #json is in array, get first array
            self.idPlace = config['idPlace']
            print("Place id is: " +self.idPlace)
        else:
            print("Creating new config..")
            file = open("config.txt", 'w')
            self.idPlace = raw_input("Enter id of place: ")
            config = []
            config.append({'idPlace' : self.idPlace})
            json.dump(config, file)

    def run(self):
        self.counter.start()
        self.startUpdater()

    def stop(self):
        self.stop_thread = True
        self.counter.stop()

    def startUpdater(self):
        while not self.stop_thread:
            time.sleep(10)
            self.currentDiff = self.counter.getIn() - self.counter.getOut()
            self.counter.resetInOut()
            params = {'valueToAdd':self.currentDiff,'placeId':self.idPlace}
            print(self.makeRequest(params))

    def makeRequest(self, params):
        httpRequest = requests.post('https://aesuneus.000webhostapp.com/qservice.php', params)
        return httpRequest
