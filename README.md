# 2017 IOT Weather underground backend

## Location
- Keelung
- Taipei
- Yilan
- Hsin-chu
- Miao-li
- Taichung
- Chang-hua
- Nantou
- Yun-lin
- Tainan
- Kao-hsiung
- Hualien

## Class Weather
### Import
- `from weather import Weather`

### Constructor
- `varName = Weather(location_str)`
- the constructor will call getCurrentConditions()

### Data field
- current condition
    - location: string
    - location_url: string
    - condition: string
    - temp_c: float
    - humidity: string
    - wind_kph: float
    - precipm: float
    - icon: string
    - icon32_url: string
    - icon64_url: string
    - icon128_url: string

- after calling getHourForecast, you will have the following data
    - hour_condition: string
    - hour_temp: string
    - hour_humidity: string
    - poprec: float
    - icon: string
    - hour32_icon_url: string
    - hour64_icon_url: string
    - hour128_icon_url: string

- after calling getHourlyForecast, you will have the following data
    - fore_hourly list of directory
        - hour: float
        - condition: string
        - temp: string
        - humidity: float
        - poprec: float
        - icon: string
        - icon32_url: string
        - icon64_url: string
        - icon128_url: string
    - use fore_hourly[index][key] to get value. e.x fore_week[0]['temp']

- after calling getWeekForecast, you will have the following data
    - fore_week: list of directory
        - fcttext: string
        - temp_high: float
        - temp_low: float
        - conditions: string
        - poprec: float
        - icon: string
        - icon32_url: string
        - icon64_url: string
        - icon128_url: string
    - use fore_week[index][key] to get value. e.x fore_week[0]['temp_high']

### Method
- getCurrentConditions(): update the current weather condition

- getHourForecast(hour: int): get the forecast info from api, should give parameter 'hour' to get the forecast at 'hour' o'clock

- getHourlyForecast(): get 24 hr forecast info
- getWeekForecast(): get 10 days forecast info

## Class Distance
### Import
- `from distance import Distance`

### Constructor
- `varName = Distance(origin: string, destination: string, mode: int)`
- mode
    - 0: driving
    - 1: transit
    - 2: walking

### Data field
- distance: string
- duration_text: string
- duration_hour: float
    - if less than 1 hr, use 1 hr. Otherwise do rounding
- if mode is 'transit'
    - if has fare => has_fare = True, else has_fare = False
    - currency: string
        - e.x "TWD"
    - fare_text: string
        - e.x "NT$70.00"
    - fare_value: float
        - e.x 70.00

