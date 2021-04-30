from browser import document, bind

# Note: If you could avoid unnecessary import, your script will save several seconds loading time
# For example, use `"message".title()` instead of `import string; string.capwords("message")`
# In this sample, though, we want to demonstrate importing 3rd-party package.
from cowpy.cow import milk_random_cow as say

@bind("#say", "click")
def echo(event):
    message = document["message"].value
    document["output"].text = say(message.title())

