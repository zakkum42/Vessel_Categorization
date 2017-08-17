#needed libraries

from PIL import Image
import os
import cv2

#we define a list for current folders
category_types= [ "aircraft_ship", "Attack_Submarine", "Ballistic_Missile_Submarine", "fish_boat",
		  "barge", "bc_ship", "capital_ship", "cargo_ship", "Container_Boat", "destroyer_escort_ship",
		  "dredger_ship", "drednought_ship", "ferry", "fire_boat", "frigate_ship", "gmc_ship",
		  "guard_ship", "hospital_ship", "Houseboat", "hovercraft", "hydrofoil", "ice_breaker_ship",
		  "Ice_Yacht", "ironclad_ship", "lc_ship", "man_of_war_ship", "mine_layer_ship", "Nuclear_Submarine",
		  "Oil_Tanker", "passenger_ship", "patrol_ship", "p_battleship", "pilot_boat", "ps_ship", "pt_ship",
		  "Racing_Yacht", "Research_submarine", "school_ship", "Submarine_Pigboat", "Submersile", "Super_Tanker",
		  "surface_ship", "tbd_ship", "tender", "Tender_Supply", "Trawler", "Trawler_Dragger", "tug", "whaler_ship"]

#for each category we go through the list
for category in category_types:


    #we now initiate the category name as another string
    catName = category

    #we change our current path to the category directory
    #user should provide path to the directory where category directories belong
    os.chdir("/data/u/oguzhancan/check-delete/" + catName )
    
    print("We are now inside " + catName)

    #we get the total number of files
    ourLength = len(os.listdir('.'))
    
    print("Our length is " + str(ourLength))

    #another loop for opening the images
    #if program cannot open the image, then just pass
    #in the except part we increase failure number and then delete the so called picture
    for i in range(ourLength):
        try:
            im = Image.open(catName + str(i+1) + '.jpg')
            name = im.format
            
            #if iamge is not broken then shape it
            if (name=='JPEG'):
                img = cv2.imread(catName + str(i+1) + '.jpg')
                grImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                rsImg = cv2.resize(grImg, (160,120))
                ourName = catName + str(i+1) + '.jpg'
                niceNumber += 1
                cv2.imwrite(ourName, rsImg)
            
            else:
                #uncomment if you need to see which files are broken
                #print ("opened" + str(i+1)+", but it is not a JPEG")
                #comment if you don't want to delete the files
                os.remove(catName + str(i+1) + '.jpg')
            
        except Exception as e:
            print ("image"+catName+str(i+1)+" cannot be opened!")
            #uncomment if you need to see which files are broken
            #print (i+1)
            #comment if you don't want to delete the files
            os.remove(catName + str(i+1) + '.jpg')
