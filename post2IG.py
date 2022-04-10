from instabot import Bot
import os
from dotenv import load_dotenv
import shutil
load_dotenv()


def clean_up():
    dir = "config"
    remove_me = "images/upload.jpg.REMOVE_ME"
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it because in 2021 it makes problems with new uploads
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("images/upload.jpg")
        os.rename(remove_me, src)


def upload_post(cap):
    bot = Bot()

    bot.login(username=os.getenv("IG_USERNAME"), password=os.getenv("IG_PWD"))
    return bot.upload_photo("images/upload.jpg", caption=cap)
    


if __name__ == '__main__':
    clean_up()
    # upload_post()