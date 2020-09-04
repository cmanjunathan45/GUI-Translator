from textblob import TextBlob
import text_to_speech as sp
from googletrans import Translator
translator=Translator()
x=input("Enter the Word to Translate :\n")
translated=translator.translate(x,src='en', dest='en')
print(translated.text)
a=TextBlob(translated.text)
b=a.detect_language()
sp.speak(translated.text,b)
