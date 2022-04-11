from glob import glob
# from instabot import Bot
from instagrapi import Client
from instagrapi import types
import os
from dotenv import load_dotenv
import shutil
load_dotenv()

bot=None

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

def login():
    global bot
    # bot = Bot()
    bot = Client()
    return bot.login(username=os.getenv("IG_USERNAME"), password=os.getenv("IG_PWD"))

    

def upload_post(cap):
    global bot
    resp = bot.photo_upload("images/upload.jpg", cap)
    return resp, type(resp)==types.Media
    

def logout():
    global bot
    bot.logout()

if __name__ == '__main__':
    clean_up()
    # upload_post()