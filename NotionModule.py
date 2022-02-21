import requests, json
from entity.NotionPage import NotionPage
from entity.NotionBlock import NotionBlock
# from entity.NotionDatabase import NotionDatabase

class Notion:

    def __init__(self, token, notion_version="2021-08-16"):
        self.token = token
        self.PostHeaders = {
            "Accept": "application/json",
            "Notion-Version": notion_version,
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.token
        }
        self.GetHeaders = {
            "Accept": "application/json",
            "Notion-Version": notion_version,
            "Authorization": "Bearer " + self.token
        }

    def DoGetRequest(self,url):
        """Make a GET request to the given url with the token"""

        response = requests.request("GET", url, headers=self.GetHeaders)
        return response.text

    def DoPostRequest(self,url,data):
        """Make a POST request to the given url with the token"""

        response = requests.request("POST", url, headers=self.PostHeaders, data=data)
        return response.text


    def GetPage(self,pageID):
        """Return a NotionPage object"""

        url = "https://api.notion.com/v1/pages/" + pageID

        res = self.DoGetRequest(url)

        id = json.loads(res)['id']
        url = json.loads(res)['url']
        properties = json.loads(res)['properties']

        url = "https://api.notion.com/v1/blocks/" + pageID
        infos = self.DoGetRequest(url)

        title = json.loads(infos)['child_page']['title']
        created_by = json.loads(infos)['created_by']
        has_children = json.loads(infos)['has_children']

        return NotionPage(id,title,properties,created_by,url,has_children)

    def GetPageContent(self,page, size=100):
        """Return a Array of NotionBlocks objects TODO"""

        return self.GetSubBlocks(page.id,size)


    def GetBlock(self,blockID):
        """Return a NotionBlock object"""

        url = "https://api.notion.com/v1/blocks/" + blockID
        raw_json = self.DoGetRequest(url)
        id = json.loads(raw_json)['id']
        type = json.loads(raw_json)['type']
        created_by = json.loads(raw_json)['created_by']
        created_time = json.loads(raw_json)['created_time']
        has_children = json.loads(raw_json)['has_children']
        content = json.loads(raw_json)[type]

        return NotionBlock(id,type,created_by,created_time,has_children,content)

    def GetSubBlocks(self,blockID,size=100):
        """Return a Array of NotionBlock objects TODO"""

        url = "https://api.notion.com/v1/blocks/" + blockID + "/children?page_size=" + str(size)
        raw_json = json.loads(self.DoGetRequest(url))['results']
        content_arr = []
        for block in raw_json:
            id = block['id']
            type = block['type']
            created_by = block['created_by']
            created_time = block['created_time']
            has_children = block['has_children']
            content = block[type]
            content_arr.append(NotionBlock(id,type,created_by,created_time,has_children,content))
        return content_arr


    def getDatabase(self,databaseID,size=100):
        """Return a Array of NotionPage objects"""

        url = "https://api.notion.com/v1/databases/"+ databaseID + "/query"
        payload = {"page_size": size}
        response = requests.request("POST", url, json=payload, headers=self.PostHeaders)
        results = json.loads(response.text)['results']
        content = []
        for page in results:
            content.append(self.GetPage(page['id']))
        return content