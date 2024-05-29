#HI! What this program does is it grabs a picture of a character from My Little Pony and makes an ASCII text of the character, colors it, and saves it. Cool right? :D.

#WARNING! Works properly only on bash terminals (because of colors).

#----------------------------------------------------------------------------------------------------
import PIL.Image
import os
from platform import system

dirPath = os.path.dirname(os.path.realpath(__file__))

ASCIIchars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

nWidth = 100

#compatibility!!!
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
    "Flurry Heart",
    "Thorax",
    "Nightmare Moon",
    "Queen Chrysalis",
    "Lord Tirek",
    "Cozy Glow",
    "Grogar",
    "Trixie",
    "Discord",
    "Sunset Shimmer",
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
dirPath += slash
charactersDir = [
    dirPath + "applejack.png",
    dirPath + "cadence.png",
    dirPath + "fluttershy.png",
    dirPath + "luna.png",
    dirPath + "pinkiePie.png",
    dirPath + "rainbowDash.png",
    dirPath + "rarity.png",
    dirPath + "spike.png",
    dirPath + "sparkle.png",
    dirPath + "heart.png",
    dirPath + "thorax.png",
    dirPath + "moon.png",
    dirPath + "chrysalis.png",
    dirPath + "tirek.png",
    dirPath + "glow.png",
    dirPath + "grogar.png",
    dirPath + "trixie.png",
    dirPath + "discord.png",
    dirPath + "shimmer.png",
]

#max width is 100
def resize_img(img):
    width, height = img.size
    ratio = height/width/2
    nHeight = int(nWidth * ratio)
    resizedImg = img.resize((nWidth, nHeight))
    return resizedImg

#the image needs to be grayscale cuz the text won't be like pixels
def grayify(img):
    grayscaleImg = img.convert("L")
    return grayscaleImg

#trasformation O_o
def pixelToASCII(img):
    pixels = img.getdata()
    chars = "".join([ASCIIchars[pixel//25] for pixel in pixels])
    return chars   

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
    [9] {characters[9]}
    [10] {characters[10]}
    [11] {characters[11]} 
    [12] {characters[12]}
    [13] {characters[13]}
    [14] {characters[14]}
    [15] {characters[15]}
    [16] {characters[16]}
    [17] {characters[17]}
    [18] {characters[18]}
    : """))
    
    img = PIL.Image.open(charactersDir[char])
        
    nImgData = pixelToASCII(grayify(resize_img(img)))
        
    pixelCount = len(nImgData)  
    asciiImg = "\n".join([nImgData[i:(i+nWidth)] for i in range(0, pixelCount, nWidth)])
    
    if char < 9 and system != "Windows":
        print(colors[char], asciiImg, "\033[49;2;0;0;0m")
    else:
        print(asciiImg)
        
    with open(characters[char] +".txt", "w") as f:
        f.write(asciiImg)
#END.------------------------------------------------------------------------------------------------
#Obs: I know this code is not following any writting norms and might be hard to read, but I ain't doing nothing about that lol :P