from browser import document, bind
# Note: If you could avoid unnecessary import, your script will save several seconds loading time
# For example, use `"message".title()` instead of `import string; string.capwords("message")`

@bind("#say", "click")
def echo(event):
    message = document["message"].value
    document["output"].text = message.title()

