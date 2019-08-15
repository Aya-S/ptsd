# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []


#Starting code for form action
#for more info: https://rasa.com/docs/rasa/core/forms/#id1
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class dsm_cri_A_form(FormAction):
    """Example of a custom form action"""
    #required function
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "dsm_cri_A"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["cri_A_a", "cri_A_b","traumatic_event_id"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "cri_A_a": [self.from_entity(entity="trauma"),
                        self.from_intent(intent='affirm',
                                         value=True),
                        self.from_intent(intent='deny',
                                         value=False)],
            "cri_A_b": [self.from_entity(entity="is_personal_experience"),
                                         self.from_intent(intent='affirm',
                                                          value=True),
                                         self.from_intent(intent='deny',
                                                          value=False)]
        }
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template("utter_goodbye", tracker)
        return []

