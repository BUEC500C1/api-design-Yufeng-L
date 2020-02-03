# api-design-Yufeng-L

## Version

Written in python __3.8.0__ <br/>
Testd in python __3.8.0__
 
## Module

This module can check weather when given airport code such as "KBOS" <br/>
Airports codes all referenced to file named __"airport-codes.csv"__ <br/>
Given Airport code -> Collect Coordinates -> Provide weather feedbacks <br/>
The following attributes are going to be collected: <br/>

|Attributes         | Units |
|-------------------|-------|
|Temperature        |°C     |
|Pressure           |hPa    |
|Humidity           | %     |

Here is the sample json data collected: <br/>
```json
{
    "base": "stations",
    "clouds": {
        "all": 20
    },
    "cod": 200,
    "coord": {
        "lat": 42.36,
        "lon": -71.01
    },
    "dt": 1580767233,
    "id": 4955993,
    "main": {
        "feels_like": 274.8,
        "humidity": 56,
        "pressure": 1010,
        "temp": 279.23,
        "temp_max": 280.37,
        "temp_min": 278.15
    },
    "name": "Winthrop",
    "sys": {
        "country": "US",
        "id": 4210,
        "sunrise": 1580730966,
        "sunset": 1580767168,
        "type": 1
    },
    "timezone": -18000,
    "visibility": 16093,
    "weather": [
        {
            "description": "few clouds",
            "icon": "02n",
            "id": 801,
            "main": "Clouds"
        }
    ],
    "wind": {
        "speed": 3.1
    }
}

```

## API

API call referene: https://openweathermap.org/current 


