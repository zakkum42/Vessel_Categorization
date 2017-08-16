#needed libraries

import os
from PIL import Image

#we define a list for current folders
category_types= [ "Attack_Submarine", "Ballistic_Missile_Submarine", "Nuclear_Submarine",
                  "Research_submarine", "Submarine_Pigboat", "Submersile", "aircraft_ship", "dredger_ship", "guard_ship",
                  "ironclad_ship", "p_battleship", "surface_ship", "tug",
                  "barge", "drednought_ship", "hospital_ship", "lc_ship", "pilot_boat", "tbd_ship", 
                  "bc_ship", "ferry", "Houseboat", "man_of_war_ship", "ps_ship", "tender", "whaler_ship", 
                  "capital_ship", "fire_boat", "hovercraft", "mine_layer_ship", "pt_ship", "Tender_Supply", 
                  "cargo_ship", "fish_boat", "hydrofoil", "Oil_Tanker", "Racing_Yacht", "Trawler",
                  "Container_Boat", "frigate_ship", "ice_breaker_ship", "passenger_ship","school_ship", "Trawler_Dragger",
                  "destroyer_escort_ship", "gmc_ship", "Ice_Yacht", "patrol_ship", "Super_Tanker",]


#we want to observe the total number of failures
number_of_failures = 0

#for each category we go through the list
for category in category_types:


    #we now initiate the category name as another string
    catName = category

    #we also want to see the local number of failures
    localNOF = 0

    #we change our current path to the category directory
    #user should provide path to the directory where category directories belong
    os.chdir("/data/u/oguzhancan/no-png-or-html/" + catName )
    
    print("We are now inside " + catName)

    #we get the total number of files
    # -2 is for non jpeg files
    ourLength = len(os.listdir('.')) - 2
    
    print("Our length is " + str(ourLength))

    #another loop for opening the images
    #if program cannot open the image, then it is not an image
    #in the except part we increase failure number and then delete the so called picture
    for i in range(ourLength):
        try:
            im = Image.open(catName + str(i+1) + '.jpg')
            name = im.format
            if (name=='JPEG'):
                pass
            else:
                #uncomment if you need to see which files are broken
                #print (i+1)
                #comment if you don't want to delete the files
                os.remove(catName + str(i+1) + '.jpg')
                localNOF += 1
                number_of_failures += 1
            
        except Exception as e:
            #uncomment if you need to see which files are broken
            #print (i+1)
            #comment if you don't want to delete the files
            os.remove(catName + str(i+1) + '.jpg')
            localNOF += 1
            number_of_failures += 1
    print ("Failures in " + catName + " " + str(localNOF) )
    
print ("Total failures " + str(number_of_failures))
