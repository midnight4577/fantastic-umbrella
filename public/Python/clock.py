import time, pygame, requests, json, io

dispWidth = 480
dispHeight = 320

pygame.init()

font = pygame.font.Font('Excluded.ttf',100)
subFont = pygame.font.Font('Excluded.ttf',40)
weatherFont = pygame.font.Font('Excluded.ttf',20)

clock = pygame.time.Clock()
win = pygame.display.set_mode([dispWidth, dispHeight])#, pygame.FULLSCREEN)
pygame.display.set_caption('Pi Time')

def blit_fm(x, y, image):
    nothing, nothing2, width, height = image.get_rect()
    win.blit(image,(x-width/2,y-height/2))

def getWeather():
    api_key = "b4297b6a5fa655aaed5e069ebf9a0eb4"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name
    city_name = "Chilliwack, CA"

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidiy = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "icon" key at
        # the 0th index of z
        current_icon = z[0]["icon"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # temp is in kelvin pressure is in hPa and humidity is a percentage
        weather = [current_temperature, current_pressure, current_humidiy, weather_description, current_icon]
        return weather
    else:
        return False

def getIcon():
    print("nothing here")

colour = (0, 255, 0)
backgroundColour = (0, 0, 0)
weatherColour = (150, 150, 255)
weatherTimer = 0
weather = getWeather()
#weatherIcon = getIcon(weather[4])
frameRate = 30


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            run = False

        if event.type == pygame.KEYDOWN:
            run = False

    clock.tick(frameRate)
    win.fill(backgroundColour)
    theTime = time.strftime("%H:%M:%S", time.localtime())
    timeText = font.render(str(theTime), True,colour)

    dateStr = time.strftime("%a, %d %b %Y", time.localtime())
    dateText = subFont.render(str(dateStr), True,colour)

    if weatherTimer >= 60*frameRate:
        weather = getWeather()
        weatherTimer = 0
    elif weatherTimer < 60*frameRate:
        weatherTimer += 1

    if weather:
        tempText = weatherFont.render(str(round(weather[0]-273.15, 2))+' Deg', False, weatherColour)
        presText = weatherFont.render(str(weather[1])+' hPa', False, weatherColour)
        humdText = weatherFont.render(str(weather[2])+' Perc', False, weatherColour)
        descText = weatherFont.render(str(weather[3]), False, weatherColour)

        blit_fm(dispWidth/2-150, dispHeight/2+80, tempText)
        blit_fm(dispWidth/2, dispHeight/2+80, presText)
        blit_fm(dispWidth/2+150, dispHeight/2+80, humdText)
        blit_fm(dispWidth/2, dispHeight/2+120, descText)
        #win.blit(weatherIcon, dispWidth/2, dispHeight/2)


    blit_fm(dispWidth/2, dispHeight/2, timeText)
    blit_fm(dispWidth/2, dispHeight/2-100, dateText)
    pygame.display.update()
