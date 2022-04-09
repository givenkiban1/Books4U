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
from notion_sync import NotionSync

load_dotenv()

nsync = NotionSync()
data = nsync.query_databases(integration_token=os.getenv("AUTH_TOKEN"))
keys = nsync.get_projects_titles(data)
print(keys)
# projects_data,dates = nsync.get_projects_data(data,projects)


# print(projects)

books = data["results"]

for book in books:
    print(book["properties"]["Name"]["title"][0]["text"]["content"], 
    # printing the isbn
    # book["properties"]["ISBN"]["rich_text"][0]["text"]["content"], 

    # printing the img link
    book["properties"]["img"]["files"][0]["file"]["url"],

    sep="\n\n", end="\n\n")

    # thinking of using isbn db for getting book covers...
    # https://developers.google.com/books/docs/v1/using#RetrievingVolume
    # https://www.googleapis.com/books/v1/volumes?q=isbn:9781337687669
    # https://syndetics.com/index.php?client=primo&isbn=0495557420/sc.jpg
    # https://stackoverflow.com/questions/65562340/high-quality-book-covers-using-google-books-api

