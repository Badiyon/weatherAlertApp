import weatherAlertAppAPI
import weatherAlertAppEmail
import weatherAlertAppChecks
import getConversion
import time



def main():
    while(True):
        API_INFO = weatherAlertAppAPI.callOpenWeatherAPI()


        temp = getConversion.fahrTemp(API_INFO['main']['temp'])
        weatherID = int(API_INFO['weather'][0]['id'])
        wind = getConversion.mphWind(API_INFO['wind']['speed'])

        if(weatherAlertAppChecks.checkTemp(temp)
                or weatherAlertAppChecks.checkWeather(weatherID)
                or weatherAlertAppChecks.checkWind(wind)):
            weatherAlertAppEmail.sendMail()
            time.sleep(28800)

        time.sleep(3600)



if __name__ == "__main__":
    main()