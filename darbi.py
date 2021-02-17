canvas = 1000                       #set inital canvas size

rect(0, 0, canvas, canvas)          #postioned in lower left hand corner with dimensions of canvas

fill(None)                          #default background colour
stroke(1)                           #set stroke colour for background bars
strokeWidth(10)                     #set size of stroke for inital background bars

y = 0;
while(y < 1000):                    #Go through the whole canvas vertically adding white bars across
    #print(y)
    line((0, y), (canvas, y))       #draw the actual stripe across canvas all the way across at varying heights
    y = y + 24                      #increment the height
   
stroke(0)                           #setup for the circle in the centre 
strokeWidth(0)                      #stroke size to 0 to make no line visible
oval(300, 300, 400, 400)            #Create a circle with the bottom right coord at 300,300 that has a radius of 400 

path = oval(300, 300, 400, 400)     #use it as a savedState
with savedState():
   
    fill(None)                      #Fill of nothing
    stroke(1)                       #Colour white
    strokeWidth(0)                  #size 0 to have no border
   
    clipPath(path)
    oval(300, 300, 400, 400)        #redraw circle
    y = 0;                      
    strokeWidth(10)                 #set size of bars, identical to above
    while(y < 1000):                #go back through and invert colours of bars within the oval
        #print(y)
        stroke(0)                   #Set colour to black
        line((200, y), (800, y))    #draw new black bar
        y = y + 12                  #increment for HALF as much as previously since we only drew white bars on the black background
        stroke(1)                   #set colour to white
        line((200,y),(800,y))       #draw the next bar over the previously white one
        y = y + 12                  #increment for the remainder to be back at the +24 like in the first loop
