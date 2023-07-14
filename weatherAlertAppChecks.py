

def checkTemp(temp):
    if(temp > 90.0 or temp <= 0.0):
        return True
    else:
        return False

def checkWeather(weatherID):
    #see weather ID codes at: https://openweathermap.org/weather-conditions

    if(checkThunderStorm(weatherID) or checkRain(weatherID) or checkSnow(weatherID)):
        return True
    else:
        return False

def checkThunderStorm(ID):
    if(ID == 201 or ID == 212 or ID == 221 or ID == 232):
        return True
    else:
        return False

def checkRain(ID):
    if(ID == 502 or ID == 503 or ID == 504 or ID == 504 or ID == 511 or ID == 522):
        return True
    else:
        return False

def checkSnow(ID):
    if(ID == 602 or ID == 613 or ID == 616 or ID == 621 or ID == 622):
        return True
    else:
        return False


def checkWind(wind):

    if(wind > 35.0):
        return True
    else:
        return False