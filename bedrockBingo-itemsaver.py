import py_mcws
from MinecraftWS import MinecraftWebSocket, Event
import json
with open("icons.json","r") as file:
    items=json.load(file)

class MyWsClient(py_mcws.WsClient):
    def event_ready(self):
        print(f"Ready {self.host}:{self.port}")

        self.events = ["PlayerMessage", "PlayerDied","ItemAcquired"]
    
    async def event_connect(self):
        print("Connected!")

        await self.command("say Hello")
    
    async def event_disconnect(self):
        print("disconnect!")

    async def event_PlayerMessage(self, event):
        print(event)
    async def event_ItemAcquired(self, event):
        
        for ev in event:
            item=ev["body"]["properties"]["Type"]
            index=ev["body"]["properties"]["AuxType"]
            
            if type(item) is str:
                print(item)
                print(index)
                if item in items.keys():
                    if len(items[item])> index:
                        if len(items[item][index])==0:
                            items[item][index]=input("png name: ")
                        else:
                            print("item already entered")
                    else:
                        while len(items[item])<index:
                            items[item].append("")
                        items[item][index]=input("png name: ")
                else:
                    items[item]=[""]
                    while len(items[item])<index:
                        items[item].append("")
                    items[item][index]=input("png name: ")

        
            with open("icons.json","w+") as file:
                json.dump(items,file,indent=2)
        
    async def event_PlayerDied(self, event):
        print(event)
        
val=dir(Event)
for ev in val:
    print(ev)

MyWsClient().start(host="localhost", port=1234)


