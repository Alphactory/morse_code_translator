import keyboard
import time
from MorseTranslator import MorseTranslator


class MorseListener:
    def __init__(self):
        self.done_flag = False
        keyboard.on_press_key("escape", lambda x: self.finish())
        self.morse_string = ""
        self.english_string = ""
        self.tl = MorseTranslator()
        print("Welcome to AT's better morse code python program. Get fucked Henry. \n"
              "This program follows the standardized morse code timings. \n"
              "source: http://www.nu-ware.com/NuCode%20Help/index.html?morse_code_structure_and_timing_.htm \n"
              "in summary, a dot is 1 unit, as is a space between actions, \n"
              "a dash is 3, as is a space between letters, and a space between words is 7. \n"
              "In order to accurately time this program, please press the spacebar for the length of a dot. \n")
        self.dot_timing = self.get_dot_timing()
        print("The program will start when you next press space because I'm not an insane dev who will make you press\n"
              "p, b, and v. (???) also press esc to exit. I actually implemented that one Henry. get fucked.")
        self.start()

    def get_dot_timing(self):
        keyboard.wait("space")
        t1 = time.time()
        print(t1)
        while keyboard.is_pressed("space"):
            time.sleep(.1)
        t2 = time.time()
        print(t2)
        return t2 - t1

    def start(self):
        t1 = 0
        t2 = 0

        # do while but it's in a while itself so that it can be broken out of with escape. main code only goes once.
        while not self.done_flag:
            # dual hotkey implementation ensures that whenever escape is pressed, the program exits cleanly
            if keyboard.is_pressed("space") or keyboard.is_pressed("escape"):
                t1 = time.time()
                break
            time.sleep(.05)

        # main loop. do this over and over until escape pressed.
        while not self.done_flag:
            while keyboard.is_pressed("space"):
                time.sleep(.1)
            t2 = time.time()
            dot_units = (t2 - t1) / self.dot_timing
            if dot_units < 2:
                self.morse_string += "."
            else:
                self.morse_string += "-"
            self.english_string = self.tl.translate(self.morse_string)
            print(self.morse_string + "\n"+ self.english_string)

            # secondary while loop for clean escape
            while not self.done_flag:
                if keyboard.is_pressed("space") or keyboard.is_pressed("escape"):
                    t1 = time.time()
                    dot_units = (t1 - t2) / self.dot_timing
                    if dot_units > 6:
                        self.morse_string += "/"
                    elif dot_units > 2:
                        self.morse_string += " "
                    else:
                        pass
                    break
                time.sleep(.05)

        return self.morse_string

    def finish(self):
        self.done_flag = True
