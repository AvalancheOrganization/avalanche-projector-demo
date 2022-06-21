import RPi.GPIO as GPIO
import vlc

import time
from datetime import datetime

import config


class Projector:

    def __init__(self):

        self.is_main_playing = True
        self.init_GPIO()
        self.init_movie()
        self.run()

    def init_GPIO(self):
        """
            Init Pi's pins.
        """
        GPIO.setmode(GPIO.BOARD)
        # Start button
        GPIO.setup(config.button_pin, GPIO.IN)

    def init_movie(self):
        """
            Init pygame.mixer.
        """
        print_log("launching main file")
        self.player = vlc.MediaPlayer(config.path_main)
        self.player.play()
        self.is_main_playing = True

    def run(self):

        try:
            while True:
                if is_activation_button_pushed():
                    self.switch_to_secondary()
                if not self.player.is_playing():
                    self.init_movie()
                time.sleep(.001)
        finally:
            GPIO.cleanup()

    def switch_to_secondary(self):
        print_log("switch_state", "switching to second file")
        self.player.stop()
        self.player = vlc.MediaPlayer(config.path_second)
        self.player.play()


def print_log(func_name, msg):
    print(f" # [{datetime.now()}] - [{func_name} - {msg}]")


def is_activation_button_pushed():
    return GPIO.input(config.button_pin) == 1


if __name__ == "__main__":
    Projector()