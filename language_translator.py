from googletrans import Translator, constants
from pprint import pprint
translator = Translator()
translation = translator.translate("GO to hell")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
print(f"{translation.text} ({translation.dest}) --> {translation.origin} ({translation.src})")