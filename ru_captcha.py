# -*- coding: utf-8 -*-

from pydub import AudioSegment
from captcha.image import ImageCaptcha
import random
import os


SOUNDS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sounds/ru_digits/')
TTF_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ttf/')
def generateCaptcha(output_file):

    captcha_text = str(random.randint(1111,9999))

    # Загружам наш бип файл - используем чтобы обозначить начало и конец результирующего файла
    beep = AudioSegment.from_wav(SOUNDS_DIR + "beep.wav")
    sounds_cache = []
    # Загружаем наши цифры от 0 до 9
    for digit in range(10):
        sounds_cache.append(AudioSegment.from_wav(SOUNDS_DIR + str(digit) + ".wav"))
    # Начинаем собирать результирующий файл
    result = beep
    for char in captcha_text:
        result += sounds_cache[int(char)]
    result += beep
    result.export(output_file + ".wav", format="wav")

    #создаем графическую капчу
    image = ImageCaptcha(fonts=[TTF_DIR + '1.ttf'])
    data = image.generate(captcha_text)
    image.write(captcha_text, output_file + ".png")
    
    return captcha_text

def main():

    output_file = "captcha"

    captcha = generateCaptcha(output_file)


if __name__ == "__main__":
    main()
    

