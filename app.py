# detecting audio frequency from mic:
# Mikael Kristyawicaksono - https://gist.github.com/notalentgeek
# https://gist.github.com/notalentgeek/48aeab398b6b74e3a9134a61b6b79a36

import aubio
import numpy as num
import pyaudio
import sys
import pyautogui
import pydirectinput
import time
from termcolor import colored, cprint


BUFFER_SIZE = 2048
CHANNELS = 1
FORMAT = pyaudio.paFloat32
METHOD = "default"
SAMPLE_RATE = 44100
HOP_SIZE = BUFFER_SIZE//2
PERIOD_SIZE_IN_FRAME = HOP_SIZE


def main(args):

    pA = pyaudio.PyAudio()
    mic = pA.open(format=FORMAT, channels=CHANNELS,
                  rate=SAMPLE_RATE, input=True,
                  frames_per_buffer=PERIOD_SIZE_IN_FRAME)

    pDetection = aubio.pitch(METHOD, BUFFER_SIZE,
                             HOP_SIZE, SAMPLE_RATE)

    pDetection.set_unit("Hz")

    pDetection.set_silence(-40)

    while True:

        data = mic.read(PERIOD_SIZE_IN_FRAME)
        samples = num.fromstring(data,
                                 dtype=aubio.float_type)
        pitch = pDetection(samples)[0]
        testi = num.float32(pitch)
        testi2 = testi.item()
        if 260 <= testi2 <= 263:
            pydirectinput.move(0, -10)
            cprint("up", "green", "on_red", attrs=["bold"])

        elif 330 <= testi2 <= 332:
            pydirectinput.move(0, 10)

            cprint("down", "green", "on_red", attrs=["bold"])
        elif 395 <= testi2 <= 398:
            pydirectinput.move(-10, 0)

            cprint("left", "green", "on_red", attrs=["bold"])

        elif 528 <= testi2 <= 532:
            pydirectinput.move(10, 0)

            cprint("right", "green", "on_red", attrs=["bold"])

        elif 660 <= testi2 <= 662:
            pydirectinput.click()

            cprint("clicked", "green", "on_red", attrs=["bold"])
        elif 790 <= testi2 <= 792:
            pydirectinput.click(button='right')

            cprint("right clicked", "green", "on_red", attrs=["bold"])


if __name__ == "__main__":
    main(sys.argv)
