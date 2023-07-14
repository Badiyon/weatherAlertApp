import configparser

def getCompleteURL():

    config = configparser.ConfigParser()
    config.read('api.env')

    API_KEY = str(config['API']['API_KEY'])
    BASE_URL = str(config['API']['BASE_URL'])
    CITY_NAME = str(config['API']['CITY_NAME'])
    COMPLETE_URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY_NAME

    return COMPLETE_URL