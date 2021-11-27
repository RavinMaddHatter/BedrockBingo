# BedrockBingo
 
Bingo has been all the rage in Java edition the last few weeks, This is a method of making it work on the windows 10 (bedrock) version. Note this likely will work as a server if you modify the code, however that was outside of the scope of this version.

## Game concept
The goal of this game is to get 5 items in a row. Typically this is played with more than 1 player as a psuedo speed run, each player gets a unique card, you collect the items as you go. If you have everything set up properly it will automatically track your progress.

## setup
 1: Download the release package, (note you may need to tell the browser you trust the source), 
 2: extract all the files into one folder, 
 3: run the bedrockBingo.exe.
 4: launch minecraft
 5: in a creative world run the command "/wsserver localhost:1234"
 6: leave the creative world and go where you want to play bingo
 
## Streamers
If you want to use this while streaming, the cleanest method is to add the "overlay.png" file created by this program as an image source. OBS will automatically update it, it has transparentcy so you dont have to do chroma keying. If you want a different map background, feel free to replace map_background.png with a different 128x128 pixel image.

