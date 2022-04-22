import sensor, image, pyb, uos

RED_LED_PIN = 1
BLUE_LED_PIN = 3

#setting up the button pins
butOne = pyb.Pin("PI0", pyb.Pin.IN, pyb.Pin.PULL_UP)
butTwo = pyb.Pin("PC3", pyb.Pin.IN, pyb.Pin.PULL_UP)
butThree = pyb.Pin("PI1", pyb.Pin.IN, pyb.Pin.PULL_UP)

#just initalizing the motor pins so that they are not used
motorPin1 = pyb.Pin("PA8", pyb.Pin.OUT_PP)
motorPin2 = pyb.Pin("PC6", pyb.Pin.OUT_PP)
motorPin3 = pyb.Pin("PG7", pyb.Pin.OUT_PP)

#weirdly named varibles for the buttons
leftFirst = True
rightFirst = True
straightFirst = True

#what directory to save the files to YOU MUST CREATE THIS ON THE SD CARD
direc = '/Machine_Learning/RC_Car'

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.B320X320)
sensor.skip_frames(time = 2000) # Let new settings take affect.



def pic(name, directory):
    pyb.LED(RED_LED_PIN).on()

    uos.chdir(directory)
    #print(uos.getcwd())
    #print(uos.listdir())

    curDir = uos.listdir(directory)
    numFiles = len(curDir)

    #print('curDirectories '+str(curDir)+' number of files '+str(numFiles))

    sensor.snapshot().save(name+str(numFiles+1)+'.jpg') # or '.bmp' (or others)

    pyb.LED(RED_LED_PIN).off()

loop = True

while(loop):

    if(butOne.value() == 0):
        if(leftFirst):
            print('Left')
            pic('Left', direc)
            leftFirst = False
    else:
        leftFirst = True

    if(butTwo.value() == 0):
        if(straightFirst):
            print('Straight')
            pic('Straight', direc)
            straightFirst = False
    else:
        straightFirst = True

    if(butThree.value() == 0):
        if(rightFirst):
            print('Right')
            pic('Right', direc)
            rightFirst = False
    else:
        rightFirst = True

    #loop = False
