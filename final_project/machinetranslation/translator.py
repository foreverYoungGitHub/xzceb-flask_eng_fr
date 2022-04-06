import os
import json

from dotenv import load_dotenv

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def initializing_language_translator():
    authenticator = IAMAuthenticator(f'{apikey}')
    language_translator = LanguageTranslatorV3(
        version='2022-04-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(f'{url}')
    return language_translator

def english_to_french(english_text):
    language_translator = initializing_language_translator()
    translation = language_translator.translate(text=english_text, model_id="en-fr").get_result()
    return translation["translations"][0]["translation"]

def french_to_english(french_text):
    language_translator = initializing_language_translator()
    translation = language_translator.translate(text=french_text, model_id="fr-en").get_result()
    return translation["translations"][0]["translation"]
