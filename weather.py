from urllib.request import urlopen
import json
import time

WU_API_KEY = "83bf26e7f792b9bf"
WU_API_URL = "http://api.wunderground.com/api/" + WU_API_KEY + "/"

ICON32_ROOT = "icon-32/"
ICON64_ROOT = "icon-64/"
ICON128_ROOT = "icon-128/"
LOCATION_ROOT = "location/"

class Weather:
    def __init__(self, location):
        self.location = location
        self.location_url = LOCATION_ROOT + location + ".png"
        # current weather info
        self.temp_c = 0
        self.humidity = 0
        self.condition = ""
        self.wind_kph = 0
        self.precipm = 0
        self.icon = ""
        self.icon32_url = ""
        self.icon64_url = ""
        self.icon128_url = ""

        # hour forecast info
        self.hour_condition = ""
        self.hour_temp = 0
        self.hour_humidity = 0
        self.hour_icon = ""
        self.hour32_icon_url = ""
        self.hour64_icon_url = ""
        self.hour128_icon_url = ""

        # 10-day forecast info
        self.fore_week = []

        # query urls
        self.pws_url = WU_API_URL + "conditions/q/TW/" + self.location + ".json"
        self.forecast_url = WU_API_URL + "hourly/q/TW/" + self.location + ".json"
        self.week_url = WU_API_URL + "forecast10day/q/TW/" + self.location + ".json"

        # init current conditions
        self.getCurrentConditions()

    def getCurrentConditions(self):
        json_str = urlopen(self.pws_url).read().decode('utf-8')
        parsed_json = json.loads(json_str)

        self.temp_c = parsed_json['current_observation']['temp_c']
        self.humidity = parsed_json['current_observation']['relative_humidity']
        self.condition = parsed_json['current_observation']['weather']
        self.wind_kph = parsed_json['current_observation']['wind_kph']
        precipm = parsed_json['current_observation']['precip_today_metric']
        if precipm.isdigit():
            self.precipm = float(precipm)
        else:
            self.precipm = 0

        self.icon = parsed_json['current_observation']['icon']
        img = getIcon(self.condition)
        self.icon32_url = ICON32_ROOT + img
        self.icon64_url = ICON64_ROOT + img
        self.icon128_url = ICON128_ROOT + img

        print("[%s] Location: %s, Temp(c): %.2f, humidity: %s" % (time.ctime(), self.location, self.temp_c, self.humidity))
        print("Description: %s" % self.condition)

    def getHourForecast(self, hour):
        json_str = urlopen(self.forecast_url).read().decode('utf-8')
        parsed_json = json.loads(json_str)

        for forecast in parsed_json['hourly_forecast']:
            if forecast['FCTTIME']['hour'] == str(hour):
                self.hour_condition = forecast['condition']
                self.hour_temp = forecast['temp']['metric']
                self.hour_humidity = forecast['humidity']
                pop = forecast['pop']
                if pop.isdigit():
                    self.poprec = float(pop)
                else:
                    self.poprec = 0
                self.hour_icon = forecast['icon']
                img = getIcon(self.hour_condition)
                self.hour32_icon_url = ICON32_ROOT + img
                self.hour64_icon_url = ICON64_ROOT + img
                self.hour128_icon_url = ICON128_ROOT + img
                break

    def getHourlyForecast(self):
        json_str = urlopen(self.forecast_url).read().decode('utf-8')
        parsed_json = json.loads(json_str)

        self.fore_hourly = []
        index = 0
        for forecast in parsed_json['hourly_forecast']:
            if index >= 24: break

            pop = forecast['pop']
            if pop.isdigit():
                poprec = float(pop)
            else:
                poprec = 0

            temp_j = forecast['temp']['metric']
            if temp_j.isdigit():
                temp = float(temp_j)
            else:
                temp = -1

            icon = forecast['icon']
            condition = forecast['condition']
            img = getIcon(condition)
            hour32_icon_url = ICON32_ROOT + img
            hour64_icon_url = ICON64_ROOT + img
            hour128_icon_url = ICON128_ROOT + img

            self.fore_hourly.append(dict([
                ("hour", float(forecast['FCTTIME']['hour'])),
                ("condition", condition),
                ("temp", temp),
                ("humidity", float(forecast['humidity'])),
                ("poprec", poprec),
                ("icon", icon),
                ("icon32_url", hour32_icon_url),
                ("icon64_url", hour64_icon_url),
                ("icon128_url", hour128_icon_url)
            ]))

            # print("%s %s %.2f" % (self.fore_hourly[index]['hour'], self.fore_hourly[index]['condition'], self.fore_hourly[index]['temp']))
            # print("%.2f %.2f %s" % (self.fore_hourly[index]['humidity'], self.fore_hourly[index]['poprec'], self.fore_hourly[index]['icon']))
            # print("%s %s" % (self.fore_hourly[index]['icon32_url'], self.fore_hourly[index]['icon128_url']))
            index += 1

    def getWeekForecast(self):
        json_str = urlopen(self.week_url).read().decode('utf-8')
        parsed_json = json.loads(json_str)

        # get forecast summary text
        index = 0
        for forecast in parsed_json['forecast']['txt_forecast']['forecastday']:
            if index % 2 != 0:
                index += 1
                continue

            self.fore_week.append(dict([("fcttext", forecast['fcttext_metric'])]))
            index += 1

        # get forecast data
        index = 0
        for simple_forecast in parsed_json['forecast']['simpleforecast']['forecastday']:
            high = simple_forecast['high']['celsius']
            low = simple_forecast['low']['celsius']

            if high.isdigit():
                self.fore_week[index]['temp_high'] = float(high)
            else:
                self.fore_week[index]['temp_high'] = -1

            if high.isdigit():
                self.fore_week[index]['temp_low'] = float(low)
            else:
                self.fore_week[index]['temp_low'] = -1

            self.fore_week[index]['poprec'] = simple_forecast['pop']
            self.fore_week[index]['conditions'] = simple_forecast['conditions']
            self.fore_week[index]['icon'] = simple_forecast['icon']
            img = getIcon(self.fore_week[index]['conditions'])
            self.fore_week[index]['icon32_url'] = ICON32_ROOT + img
            self.fore_week[index]['icon64_url'] = ICON64_ROOT + img
            self.fore_week[index]['icon128_url'] = ICON128_ROOT + img
            index += 1

def getIcon(condition):
    if condition == "Clear":
        return "clear.png"

    if condition == "Cloudy":
        return "cloudy.png"

    if condition == "Fog":
        return "fog.png"

    if condition == "Haze":
        return "cloudy.png"

    if condition == "Mostly Cloudy":
        return "mostlycloudy.png"

    if condition == "Mostly Sunny":
        return "mostlysunny.png"

    if condition == "Partly Cloudy":
        return "partlycloudy.png"

    if condition == "Partly Sunny":
        return "partlysunny.png"

    if "Rain" in condition:
        return "rain.png"

    if "Thunderstorm" in condition:
        return "tstorms.png"

    if condition == "Sunny":
        return "sunny.png"

    if condition == "Overcast":
        return "cloudy.png"

    if condition == "Scattered Clouds":
        return "partlycloudy.png"

    if condition == "Snow":
        return "snow.png"

    return "cloudy.png"# default image
