from urllib.request import urlopen
from urllib.parse import urlencode
from collections import OrderedDict
import json
import decimal as dec

GOOGLE_MAP_API_KEY = "AIzaSyCONgqEAYnvS8Dhs6wRJisnOOivUQecYYU"
GOOGLE_MAP_API_URL = "https://maps.googleapis.com/maps/api/distancematrix/json?"

DRIVING = 0
TRANSIT = 1
WALKING = 2

class Distance:
    def __init__(self, origin, destination, mode = DRIVING):
        if mode == DRIVING:
            mode_s = "driving"
        elif mode == TRANSIT:
            mode_s = "transit"
        elif mode == WALKING:
            mode_s = "walking"
        else:
            mode_s = "driving"

        query = urlencode(OrderedDict([
            ("origins", origin),
            ("destinations", destination),
            ("mode", mode_s),
            ("key", GOOGLE_MAP_API_KEY)
        ]))

        self.url = GOOGLE_MAP_API_URL + query

        json_str = urlopen(self.url).read().decode('utf-8')
        parsed_json = json.loads(json_str)

        self.distance = parsed_json['rows'][0]['elements'][0]['distance']['text']
        self.duration_text = parsed_json['rows'][0]['elements'][0]['duration']['text']
        self.duration_hour = parsed_json['rows'][0]['elements'][0]['duration']['value']
        self.duration_hour /= 3600

        if self.duration_hour < 1.0:
            self.duration_hour = 1.0
        else:
            self.duration_hour = round(self.duration_hour, 0)

        if mode == TRANSIT and 'fare' in parsed_json['rows'][0]['elements'][0]:
            self.has_fare = True
            self.currency = parsed_json['rows'][0]['elements'][0]['fare']['currency']
            self.fare_text = parsed_json['rows'][0]['elements'][0]['fare']['text']
            self.fare_value = parsed_json['rows'][0]['elements'][0]['fare']['value']
        else:
            self.has_fare = False

        print("From %s to %s, distance: %s, duration: %s(%.2f)" % (origin, destination, self.distance, self.duration_text, self.duration_hour))
