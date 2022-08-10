""" Language Translator module """
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Prepare the Authenticator
authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translate English to French
    """
    translation_new = language_translator.translate(
        text=english_text,model_id='en-fr').get_result()
    french_text= translation_new['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translate French to English
    """
    translation_new = language_translator.translate(
        text=french_text,model_id='fr-en').get_result()
    english_text= translation_new['translations'][0]['translation']
    return english_text

print(english_to_french(''))
print(french_to_english('\nBonjour'))
