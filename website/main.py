# This script is developed based on Brython https://brython.info
from browser import document, bind
from string import capwords as say

@bind("#say", "click")
def echo(event):
    message = document["message"].value
    document["output"].text = say(message)

