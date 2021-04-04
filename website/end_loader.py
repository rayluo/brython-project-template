# end_loader runs once all main application code is done.
from browser import document, window
def end_loader(done_message="Ready!"):

    def finished_ready(event):
        print("finished ready!")
        # Loading should also be done with its gradient animation too. We can hide it now
        document["loading"].style.display = "none"
        document["loading"].style.cursor = "default"
        document['psychology'].unbind("animationend")
        del document["loading"]


    def finished_loading(event):
        """Finish the loading animation"""
        print("Finished animating!")

        document["loading_icon"].classList.remove('fa-circle-o-notch')
        document["loading_icon"].classList.remove('fa-spin')
        document["loading_icon"].classList.add("fa-thumbs-o-up")

        # We set loading to the gradientout class which animates from grey background to white
        document["loading"].classList.add("gradientout")
        # We set psychology to the growout class which has a single animation.
        document["psychology"].classList.add("growout")
        document["psychology"].classList.remove("pulsing")
        document["loading_message"].innerHTML = done_message
        # When the animation ends we run the code to bring in the rendered app
        document['psychology'].bind('animationend', finished_ready)

        # Remove the binding for end of animation iteration
        document['psychology'].unbind("animationiteration")


    # Animationiteration happens when the loading animation reaches the end of its sequence
    document['psychology'].bind('animationiteration', finished_loading)

# Hack to ensure that our function is available in other scripts
window.end_loader = end_loader