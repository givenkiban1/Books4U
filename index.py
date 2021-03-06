# from notion.client import NotionClient
# from dotenv import load_dotenv
# import os

# load_dotenv()

# print("starting")
# print(os.getenv("AUTH_TOKEN"))
# client = NotionClient(token_v2=os.getenv("AUTH_TOKEN"))

# print(client.get_email_uid())

# tl = client.get_top_level_pages()

# print(tl)
# GivensWorld = tl[0]
# print(tl)



# cv = client.get_collection("https://www.notion.so/aece8acaf0fe41bdaf51dd56dff8f9a0?v=d204ef5333414cdc9eab2a6be0ba8039")

# for row in cv.get_rows():
#     print(row.name, row.ISBN)

# print("done")

from dotenv import load_dotenv
import os
from ad_create import CreateAd
from notion_sync import NotionSync
from post2IG import clean_up, login, logout

load_dotenv()

nsync = NotionSync()
data = nsync.query_databases(integration_token=os.getenv("AUTH_TOKEN"))
keys = nsync.get_projects_titles(data)
print(keys)
# projects_data,dates = nsync.get_projects_data(data,projects)


# print(projects)

books = data["results"]

noPosted = 0
# clean_up()
if login()==False:
    print("Could not login to IG Successfully.")
    exit()

for book in books:

    url=book["properties"]["img"]["files"][0]["file"]["url"]
    title=book["properties"]["Name"]["title"][0]["text"]["content"]
    ref=  book["properties"]["Ref"]["rich_text"][0]["text"]["content"]
    isbn=book["properties"]["ISBN"]["rich_text"][0]["text"]["content"]
    condition=  book["properties"]["Condition"]["select"]["name"]
    cost =  book["properties"]["Price"]["number"]
    posted = book["properties"]["Posted"]["checkbox"]
    pId= book["id"]

    if (posted==False):
        print(title, 
        # printing the isbn
        # book["properties"]["ISBN"]["rich_text"][0]["text"]["content"],
        
        # page id...
        pId, 

        # printing the img link
        url,

        sep="\n\n", end="\n\n")

        if CreateAd(title=title, img=url, cost=cost, condition=condition, ref=ref, isbn=isbn):
            if nsync.update_page(integration_token=os.getenv("AUTH_TOKEN"), id=pId, dataParam={"properties":{"Posted":{"checkbox":True}}}):
                print("Ad created successfully")
            else:
                print("Could not update notion")

        else:
            print("Could not create Ad.")

        for file in os.listdir('./images/'):
            if file!="canvas.png":
                os.remove('./images/'+file)

        # clean_up()

    else:
        noPosted+=1

logout()

if (noPosted==len(books)):
    print("No new books to create ads for! Work harder")
    
   



    # thinking of using isbn db for getting book covers...
    # https://developers.google.com/books/docs/v1/using#RetrievingVolume
    # https://www.googleapis.com/books/v1/volumes?q=isbn:9781337687669
    # https://syndetics.com/index.php?client=primo&isbn=0495557420/sc.jpg
    # https://pictures.abebooks.com/isbn/9780357113516-us.jpg
    # https://stackoverflow.com/questions/65562340/high-quality-book-covers-using-google-books-api

