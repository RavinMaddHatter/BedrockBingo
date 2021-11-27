import py_mcws
from threading import Thread
import bingoCard
from  asyncio import new_event_loop, set_event_loop
from time import sleep
from queue import Queue
from tkinter import Canvas, Tk, Button
from PIL import Image, ImageTk


card=bingoCard.bingoCard()
card.makeCard()

class MyWsClient(py_mcws.WsClient):
    def event_ready(self):
        print(f"Ready {self.host}:{self.port}")

        self.events = ["ItemAcquired"]
    
    async def event_connect(self):
        print("Connected!")
        await self.command("/w @s Connected to Bingo")
    async def event_PlayerMessage(self, event):
        event
    async def event_disconnect(self):
        print("disconnect!")
    async def event_PlayerDied(self, event):
        event
    async def event_ItemAcquired(self, event):
        
        for ev in event:
            item=ev["body"]["properties"]["Type"]
            index=ev["body"]["properties"]["AuxType"]
            
            if type(item) is str:
                print(item)
                updateGui.put("refresh")
                res=card.foundItem(item)
                print("results")
                print(res)
                if card.checkBingo():
                    await self.command("/w @s BINGO")
        #await self.command("say Hello")

class gui:
    def __init__(self,que):
        self.que=que
        self.root = Tk()
        
        self.c = Canvas(self.root, bg='white', width=512, height=512)
        
        img=Image.open("overlay.png")
        img = img.resize([512, 512], Image.NEAREST)
        image=ImageTk.PhotoImage(img)
        self.image_on_canvas=self.c.create_image(0,0,anchor='nw',image=image)
        self.wt=Thread(target=self.watchQueue)
        
        self.wt.start()
        self.newGame=Button(self.root,text ="New Card",command = self.newCard)
        self.newGame.pack()
        self.c.pack()
        
        self.root.mainloop()
    def newCard(self):
        global card
        card=bingoCard.bingoCard()
        card.makeCard()
        img=Image.open("overlay.png")
        img = img.resize([512, 512], Image.NEAREST)
        self.img=ImageTk.PhotoImage(img)
        self.c.itemconfig(self.image_on_canvas,image=self.img)
        
    def watchQueue(self):
        print("starting watcher")
        while True:
            if not(self.que.empty()):
                img=Image.open("overlay.png")
                img = img.resize([512, 512], Image.NEAREST)
                self.img=ImageTk.PhotoImage(img)
                self.c.itemconfig(self.image_on_canvas,image=self.img)
                self.que.get()
                
            else:
                sleep(0.1)
def startWatcher():
    print("hi")
    loop = new_event_loop()
    set_event_loop(loop)
    MyWsClient().start(host="localhost", port=1234)

watcher = Thread(target=startWatcher)
watcher.start()

updateGui=Queue()
test=gui(updateGui)





