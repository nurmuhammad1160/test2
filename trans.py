from googletrans import Translator

translator = Translator()

def translate_text(text, dest='en'):
    try:
        result = translator.translate(text, dest=dest)
        return result.text
    except Exception as e:
        return "Bunday so'z topilmadi"
    


