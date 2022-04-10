DATABASE_ID = "aece8acaf0fe41bdaf51dd56dff8f9a0"
NOTION_URL = 'https://api.notion.com/v1/'
import requests
import json

class NotionSync:
    def __init__(self):
        pass    

    def query_databases(self,integration_token="YOUR INTEGRATION TOKEN"):
        database_url = NOTION_URL + 'databases/' + DATABASE_ID + "/query"
        response = requests.post(database_url, headers={"Authorization": f"Bearer {integration_token}", 'Notion-Version': '2022-02-22'})
        if response.status_code != 200:
            raise Exception(f'Response Status: {response.status_code}')
        else:
            return response.json()
    
    def get_projects_titles(self,data_json):
        return list(data_json["results"][0]["properties"].keys())
    
    def update_page(self, integration_token="YOUR INTEGRATION TOKEN",id="PAGE ID", dataParam={}):
        database_url = NOTION_URL + 'pages/' + id
        response = requests.patch(database_url, headers={"Authorization": f"Bearer {integration_token}", "Content-Type": "application/json", 'Notion-Version': '2022-02-22'},
        data=json.dumps(dataParam))

        if response.status_code!=200:
            print(f'Response Status: {response.status_code}')
            print(f'{response.content}')
            print(response.request.body)
            return False
        else:
            print(f'{response.content}')
            return True
        


    def get_projects_data(self,data_json,projects):
        projects_data = {}
        for p in projects:
            if p=="Name":
                projects_data[p] = [data_json["results"][i]["properties"][p]["title"][0]["text"]["content"]
                                    for i in range(len(data_json["results"]))]
            # elif p=="DateListed":
            #     dates = [data_json["results"][i]["properties"]["date"]["start"]
            #                         for i in range(len(data_json["results"]))]

        
        return projects_data,[]


if __name__=="__main__":
    print(NotionSync().update_page(integration_token="",id="", dataParam={"properties":{}}))