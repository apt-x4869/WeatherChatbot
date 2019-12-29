# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "action_hello_world"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Hello World!")
        return []



import datetime
class ActionTime(Action):
    def name(self) -> Text:
        return "action_time"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        txt = str(datetime.datetime.now())
        dispatcher.utter_message(txt)
        return []
from rasa_core_sdk.events import SlotSet
import requests, json
class ActionWeather(Action):
    def name(self) -> Text:
        return "action_weather"
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        api_key = "7fa2f3ab99eafedc592b7690bba5d54d"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = str(loc)
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the current pressure is {} hpa.""".format(weather_description, city_name, current_temperature, current_humidiy, current_pressure)
            dispatcher.utter_message(response)
        else:
            dispatcher.utter_message("City Not found")
        return [SlotSet('location',loc)]
