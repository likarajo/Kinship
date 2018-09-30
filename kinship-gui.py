from tkinter import *
import os
from lib.operations import kinships

#create and setup the root window
root = Tk()
root.title("Kinship")
root.geometry("300x100")

#create Frame to hold widgets
app = Frame(root).grid()

#create Widgets
labelWord = Label(app, text = "Enter word").grid(row=0, column=0)
textWord = StringVar()
entryWord = Entry(app, textvariable=textWord).grid(row=0, column=1)
labelKins = Label(app, text = "Enter no. of kins").grid(row=2, column=0)
textKins = IntVar()
entryKins = Entry(app, textvariable=textKins).grid(row=2, column=1)
labelTweetCount = Label(app, text = "Enter tweet count").grid(row=1, column=0)
textTweetCount = IntVar()
entryTweetCount = Entry(app, textvariable=textTweetCount).grid(row=1, column=1)
def getKin():
    kinships(
        ACCESS_TOKEN = os.environ['2390269165-bTMxMFUrJma8etDMHoB6uTOl8WElxLMPp3WDRFE'],
        ACCESS_SECRET = os.environ['yEhAL19G3sgOAtzioBYyV1CLrx93GtZYhowWsLJARZwmA'],
        CONSUMER_KEY = os.environ['jz0ikcqx7F4VH7haLxn16rOH4'],
        CONSUMER_SECRET = os.environ['Y5jHZdHguM3YtDcH2RED1KZcepjkenNMOtGZF1XMZ9RG9oddUc'],
        word = textWord.get(),
        kins = textKins.get(),
        tweet_count = textTweetCount.get()
        )
buttonGetKins = Button(app, text = "Get kins", command=getKin).grid(row=3, column=0, columnspan=2)
buttonQuit = Button(app, text = "Quit", command=quit).grid(row=3, column=1, columnspan=2)
                       
#start eventloop to display the window
root.mainloop()
