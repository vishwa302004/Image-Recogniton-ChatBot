from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideComponentDetails(Action):
    def name(self) -> Text:
        return "action_provide_component_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        component = next(tracker.get_latest_entity_values("component"), None)

        if component == "capacitor":
            dispatcher.utter_message(template="utter_component_details_capacitor")
        elif component == "resistor":
            dispatcher.utter_message(template="utter_component_details_resistor")
        elif component == "LED":
            dispatcher.utter_message(template="utter_component_details_led")
        elif component == "diode":
            dispatcher.utter_message(template="utter_component_details_diode")
        else:
            dispatcher.utter_message(text="I don't have information on that component.")

        return []

class ActionProvideComponentPrice(Action):
    def name(self) -> Text:
        return "action_provide_component_price"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        component = next(tracker.get_latest_entity_values("component"), None)

        if component == "capacitor":
            dispatcher.utter_message(template="utter_component_details_capacitor")
        elif component == "resistor":
            dispatcher.utter_message(template="utter_component_details_resistor")
        elif component == "LED":
            dispatcher.utter_message(template="utter_component_details_led")
        elif component == "diode":
            dispatcher.utter_message(template="utter_component_details_diode")
        else:
            dispatcher.utter_message(text="I don't have information on that component.")

        return []
