from PIL import Image


def createRotations(folderName, fileToRotate):
    OG = Image.open(fileToRotate).convert("RGBA")
    for i in range(360):
        CurImg = OG.rotate(i, Image.NEAREST, expand=1,fillcolor=(0,0,0,0)).resize((50,50))
        #print(folderName + "\\" + str(i) + ".png")
        CurImg.save(folderName + "\\" + str(i) + ".png",optimize=True)

fileNames=["aggie_spaceship.png","enemy_type_1.png"]
folderNames=["Player","Charger"]
for num,file in enumerate(fileNames):
    createRotations(folderNames[num],file)