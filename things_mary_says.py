# By Jeremy

import random
import requests
from lxml import html
from subprocess import call
from time import sleep


URL = 'https://noisebridge.net/wiki/Things_Mary_Says'
PATH_TAG = '//p/text()'
RUN_EVERY_IN_MINUTES = 150

previous_phrases = []

def pick_and_say(look_back=10):
    global previous_phrases
    # Go to wiki to grab all the things mary says
    text = requests.get(URL).text
    root = html.fromstring(text)

    # Get list of pharses - split up by paragraph
    phrases = root.xpath(PATH_TAG)

    # Make random selection
    choice = random.choice(phrases).strip()

    # Make sure the choice hasn't been said recently
    while choice in previous_phrases:
        print 'choice: "%s", but skipping' \
            % choice
        choice = random.choice(phrases)

    # Add choice to beginning of previous_phrases
    previous_phrases = [choice] + previous_phrases
    # Pop the oldest off the list
    previous_phrases = previous_phrases[:look_back]

    command = ['say', choice]
    print 'saying "%s"' % choice
    call(command)

def main():
    while 1:
        time_to_wait = random.randrange(60 * RUN_EVERY_IN_MINUTES)
        sleep(time_to_wait)
        pick_and_say()

if __name__ == "__main__":
    main()
