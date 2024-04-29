from django.test import TestCase
import requests

class TemperatureAPITest(TestCase):
    def test_temperature_equality(self):
        try:
            # Fetch temperature from custom API
            response_custom = requests.post('http://3.71.86.177:8000/api/temperature', json={"city": "Oslo"})
            response_custom.raise_for_status()  # Raise exception if response status code is not 2xx
            temp_custom = response_custom.json()['temperature']

            # Fetch temperature from OpenWeatherMap
            response_owm = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Oslo&appid=d2a2b4ae87b93c165c5421cee9970939&units=metric')
            response_owm.raise_for_status()  # Raise exception if response status code is not 2xx
            temp_owm = response_owm.json()['main']['temp']

            # Compare temperatures with a tolerance of less than 1 degree difference
            self.assertAlmostEqual(temp_custom, temp_owm, delta=1, msg="The difference in temperatures is greater than 1 degree.")
        except requests.exceptions.RequestException as e:
            self.fail(f"Failed to fetch temperature data: {e}")

    def test_temperature_equality_on_client(self):  # New test method with a different name
        try:
            # Fetch temperature from custom API
            response_custom = requests.post('http://3.71.86.177:8000/api/temperature', json={"city": "Oslo"})
            response_custom.raise_for_status()  # Raise exception if response status code is not 2xx
            temp_custom = response_custom.json()['temperature']

            # Fetch temperature from OpenWeatherMap
            response_owm = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Oslo&appid=d2a2b4ae87b93c165c5421cee9970939&units=metric')
            response_owm.raise_for_status()  # Raise exception if response status code is not 2xx
            temp_owm = response_owm.json()['main']['temp']

            # Compare temperatures with a tolerance of less than 1 degree difference
            self.assertAlmostEqual(temp_custom, temp_owm, delta=1, msg="The difference in temperatures is greater than 1 degree.")
        except requests.exceptions.RequestException as e:
            self.fail(f"Failed to fetch temperature data: {e}")
