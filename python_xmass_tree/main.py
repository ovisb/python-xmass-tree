from postcard import Postcard
from user_interface import UserInterface

if __name__ == "__main__":
    postcard = Postcard()
    user_interface = UserInterface(postcard)

    user_interface.start()
