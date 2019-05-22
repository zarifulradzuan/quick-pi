
import json
import requests
import time
import threading
import os
import people_counter

class Quick(threading.Thread):
    def __init__(self, idPlace):
        threading.Thread.__init__(self)
        self.counter = people_counter.PeopleCount("prototxt.prototxt", "model.caffemodel", "videos\example_01.mp4", 0.4, 30)
        self.currentDiff = 0
        if(os.path.isfile("config.txt")):
            print("Config file found, loading from file..")
            config = json.load(open("config.txt", "r"))
            config = config[0] #json is in array, get first array
            self.url = config['url']
            print("Server url is: " +self.url)
            self.idPlace = config['idPlace']
            print("Place id is: " +self.idPlace)
        else:
            print("Creating new config..")
            file = open("config.txt", "x")
            self.url = input("Enter url: ")
            self.idPlace = input("Enter id of place: ")
            config = []
            config.append({   'url' : url,
                                        'idPlace' : idPlace})
            json.dump(config, file)

    def run(self):
        self.counter.start()
        self.startUpdater()
        print("\nRunning..")

    def startUpdater(self):
        while(True):
            time.sleep(10)
            self.currentDiff = self.counter.getIn() - self.counter.getOut()
            self.counter.resetInOut()
            print (self.currentDiff)
            params = {'selectFn':'insertDiff','idPlace':self.idPlace, 'currentDiff': self.currentDiff}

    def makeRequest(self, params):
        httpRequest = requests.json(url, params)
        return httpRequest.json()