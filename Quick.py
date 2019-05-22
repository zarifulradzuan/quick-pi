import qclass
import people_counter
import time
import threading
#quickProcess = qclass.Quick(2)
#quickProcess.start()

#counter = people_counter.PeopleCount("prototxt.prototxt", "model.caffemodel", False, 0.4, 30)
totalIn = 0
totalOut = 0
print("running")
stop_thread = False
#counter = people_counter.PeopleCount("prototxt.prototxt", "model.caffemodel", "videos\example_01.mp4", 0.4, 30)
#counter.start()
quickProcess = qclass.Quick(2)
quickProcess.start()