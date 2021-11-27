from PIL import Image
import numpy as np
from os import path
from json import load
import random

class bingoCard:
    def __init__(self,background="map_background.png",save="overlay.png",icons="icons"):
        self.card = Image.open(background)
        self.card = self.card.convert("RGBA")
        self.location=save
        self.icons=icons
        with open("icons.json","r") as file:
            items=load(file)
        self.lookup=items
        self.items={}
        self.found=np.zeros((5,5))
        
    def addSquare(self,name,x,y,index=0):
        self.items[name]=[x,y,index]
        imName=self.lookup[name][index]
        self.markSquare(x,y,name=imName)
    def markSquare(self,x,y,name="cross.png"):
        icon=Image.open(path.join(self.icons,name))
        icon=icon.convert("RGBA")
        icon=icon.resize((16,16,))
        offset=(16+x*19,16+y*19,)
        self.card.paste(icon,offset,icon)
        self.card.save(self.location)
    def foundItem(self,item,index=0):
        found=False
        if item in self.items:
            
            if index == self.items[item][2]:
                self.markSquare(self.items[item][0],self.items[item][1])
                self.found[x,y]=1
                found=True
        
    def checkBingo(self):
        sums=[]
        for i in range(5):
            sums.append(self.found[:,i].sum())
            sums.append(self.found[i,:].sum())
        sums.append(sum([self.found[0,0],self.found[1,1],self.found[2,2],self.found[3,3],self.found[4,4]]))
        sums.append(sum([self.found[4,0],self.found[3,1],self.found[2,2],self.found[1,3],self.found[0,4]]))
        print(sums)
        return max(sums)==5
            
    def makeCard(self):
        choices=list(self.lookup.keys())
        choices.remove("emerald")
        chosen=random.sample(choices,25)
        chosen[12]="emerald"
        for x in range(5):
            for y in range(5):
                item=chosen[y+x*5]
                imgname=random.choice(self.lookup[item])
                idx=self.lookup[item].index(imgname)
                self.addSquare(item,x,y,index=idx)
        
