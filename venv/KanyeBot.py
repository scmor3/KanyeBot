# import the random library to help us generate the random numbers
import random
import requests
from albums import ALBUMS
# Create the kanyebot Class
class kanyebot:

    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
        self.channel = channel

    def _get_message(self):
        """generate random kanye quote and song, decorate, and return to user"""

        #access Kanye.Rest API to generate random Kanye West Quote
        quote = requests.get("https://api.kanye.rest/").json()["quote"]
        #custom kanye emojis
        yemojis = [":kanye:", ":kanye1:", ":kanye2:", ":kanye3:", ":kanye4:"]
        #get random kanye emoji
        yemoji = random.choice(yemojis)
        #get random song from random album (in tuple format (song, link))
        result = (random.choice(ALBUMS))
        song = result[0]
        link = result[1]
        if song == "Rick Astley - Never Gonna Give You Up (Video)":
            text = f":smirk:\n<{link}|{song}>"
        else:
            text = f"_{quote}_\t{yemoji}\n<{link}|{song}>"

        return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                *self._get_message(),
            ],
        }