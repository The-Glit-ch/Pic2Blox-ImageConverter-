#A *cleaner* version of the prev version (Its always cleaner lol)
#
#
#Original Creator: 0xSENNA#0500
#Re-writer: The_Glit-ch#4859

#This program converts an image into a usuable raw xml file which can be used in roblox studio to convert that data into an image

#This is like the 7th re-write or something lol

import os, time, threading

from PIL import Image
import PIL #Required to load images and get the pixel values

Temp = "{B827E5AD-79A9-4080-85D7-6DCE69D11528}"

def Values(img): #Image goes in the param
    print("Making RGB list")
    ImageList = [] #We first set an empty list so it can be used to append data into it
    
    Load = img.convert("RGB").load() #We convert the image to RGB and then set it as a variable
    
    for ver in range(int(img.size[1])): #Vertical Loop
         ImageList.insert(ver, []) #Inserts the vertical data
         
         for hor in range(int(img.size[0])): #Horizontal loop
             ImageList[ver].insert(hor, [Load[hor, ver]]) #Inserts the horizontal data
    
    print(f"List finished...\nItems in list: {len(ImageList)}")
    return ImageList #Returns the ImageLIst

def Translate(List): #This would be used to translate the Imagelist into an RLua table
    print("Trasnalating list from python to lua!")
    RLua_Table = str(List).replace("[", "{").replace("]", "}").replace("(", "{").replace(")", "}") #Turns the list to a string (Other wise we cant use ".replace()")
    print("Done translating")
    return RLua_Table

def XMLDataFile(Content):
    print("Writing to nice and better data")
    with open("ImageData.rbxmx","w") as DataFile:
        DataFile.write(f"""
<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">
	<Meta name="ExplicitAutoJoints">true</Meta>
	<External>null</External>
	<External>nil</External>
	<Item class="ModuleScript" referent="RBX2395388B926E410B88DAD016EB22A8E9">
		<Properties>
			<BinaryString name="AttributesSerialize"></BinaryString>
			<Content name="LinkedSource"><null></null></Content>
			<string name="Name">Image</string>
			<string name="ScriptGuid">{Temp}</string>
			<ProtectedString name="Source">return {Content}</ProtectedString>
			<BinaryString name="Tags"></BinaryString>
		</Properties>
	</Item>
</roblox>""")
        print("All done")

def Main(FilePathForImage):
    T = time.time()
    XMLDataFile(Translate(Values(Image.open(FilePathForImage))))
    print(f"The whole thing took {time.time() - T}seconds")


def KickStarter(): #Starts the process
    print("Enter in the image name with extension")
    ImgName = input(":")
    FilePath = os.path.abspath(ImgName)
    try:
        Thread = threading.Thread(target=Main, args=(FilePath,)) #We use threading to make things go fast
        Thread.start()
    except FileNotFoundError as err:
        print(err)
        KickStarter()

KickStarter()
