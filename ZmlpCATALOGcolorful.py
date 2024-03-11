#HI! What this program does is it grabs a picture of a character from My Little Pony and makes an ASCII text of the character, colors it, and saves it. Cool right? :D.

#WARNING! Works properly only on bash terminals.
#HI! This project was made in python 3.10.12, so you're probably gonna need the interpreter for that. To execute it, you'll need to have all the pictures saved on the directory, and then just run it! If any errors occur, try messaging me or something, my discord is average_n00bie :D. By the way, the code saves the ASCII text in a file on the directory it's placed on. 

#----------------------------------------------------------------------------------------------------
import PIL.Image
import os
from platform import system

print("Specially made for: 'Mexerica', with <3")

dirPath = os.path.dirname(os.path.realpath(__file__))

ASCIIchars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

nWidth = 100

if system == "Windows":
    slash = "\\"
else:
    slash = "/"

characters = [
    "Applejack",
    "Cadence",
    "Fluttershy",
    "Luna",
    "Pinkie Pie",
    "Rainbow Dash",
    "Rarity",
    "Spike",
    "Twilight Sparkle",
]

colors = [
    "\033[38;2;251;186;97m",
    "\033[38;2;238;195;221m",
    "\033[38;2;243;185;216m",
    "\033[38;2;14;73;178m",
    "\033[38;2;241;67;140m",
    "\033[38;2;157;271;248m",
    "\033[38;2;94;79;162m",
    "\033[38;2;82;196;88m",
    "\033[38;2;209;159;227m",
]

#directories
charactersDir = [
    dirPath + slash + "applejack.png",
    dirPath + slash + "cadence.png",
    dirPath + slash + "fluttershy.png",
    dirPath + slash + "luna.png",
    dirPath + slash + "pinkiePie.png",
    dirPath + slash + "rainbowDash.png",
    dirPath + slash + "rarity.png",
    dirPath + slash + "spike.png",
    dirPath + slash + "twilightSparkle.png",
]

#max width is 100
def resize_img(img):
    width, height = img.size
    ratio = height/width/2
    nHeight = int(nWidth * ratio)
    resizedImg = img.resize((nWidth, nHeight))
    return(resizedImg)

def grayify(img):
    grayscaleImg = img.convert("L")
    return(grayscaleImg)

#Trasformation O_o
def pixelToASCII(img):
    pixels = img.getdata()
    chars = "".join([ASCIIchars[pixel//25] for pixel in pixels])
    return(chars)    

while True:
    char = int(input(f"""Choose a character to show
    [0] {characters[0]}
    [1] {characters[1]}
    [2] {characters[2]} *
    [3] {characters[3]}
    [4] {characters[4]}
    [5] {characters[5]}
    [6] {characters[6]}
    [7] {characters[7]}
    [8] {characters[8]}
    : """))
    
    img = PIL.Image.open(charactersDir[char])
        
    nImgData = pixelToASCII(grayify(resize_img(img)))
        
    pixelCount = len(nImgData)  
    asciiImg = "\n".join([nImgData[i:(i+nWidth)] for i in range(0, pixelCount, nWidth)])
        
    print(colors[char], asciiImg, "\033[49;2;0;0;0m")
        
    with open(characters[char] +".txt", "w") as f:
        f.write(asciiImg)
#END.------------------------------------------------------------------------------------------------
#Obs: I know this code is not following any writting norms and might be hard to read, but I ain't doing nothing about that lol :P