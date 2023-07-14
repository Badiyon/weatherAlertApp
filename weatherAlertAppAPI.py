import requests
import getURL


def callOpenWeatherAPI():
    COMPLETE_URL = getURL.getCompleteURL()

    response = requests.get(COMPLETE_URL)
    info = response.json()

    return info