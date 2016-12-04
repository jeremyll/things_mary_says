# By Jeremy

import random
import requests
from lxml import html
from subprocess import call
from time import sleep


URL = 'https://noisebridge.net/wiki/Things_Mary_Says'
PATH_TAG = '//p/text()'
RUN_EVERY_IN_MINUTES = 100

def pick_and_say():
    # Go to wiki to grab all the things mary says
    text = requests.get(URL).text
    root = html.fromstring(text)

    # Get list of pharses - split up by paragraph
    phrases = root.xpath(PATH_TAG)

    # Make random selection
    choice = random.choice(phrases)

    command = ['say', choice]
    call(command)

def main():
    while 1:
        time_to_wait = random.randrange(60 * RUN_EVERY_IN_MINUTES)
        sleep(time_to_wait)
        pick_and_say()

if __name__ == "__main__":
    main()
