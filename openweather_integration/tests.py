from unittest import TestCase

import frappe

class TestOpenWeatherMapAPICall(TestCase):

    def test_open_weather_api(self):
        open_weather_api.call_api(5121636, c7dbb6524fa00c76e6679f8f5d8de9f1)


api.openweathermap.org/data/2.5/