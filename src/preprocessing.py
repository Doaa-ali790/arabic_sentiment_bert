
import re

def normalize_arabic(text):

    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)

    text = re.sub("[^ا-ي ]", "", text)

    return text
