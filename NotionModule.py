import requests, json
from entity.NotionPage import NotionPage
# from entity.NotionBlock import NotionBlock
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

        infos = self.GetBlock(id)

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
        return self.DoGetRequest(url)

    def GetSubBlocks(self,blockID,size=100):
        """Return a Array of NotionBlock objects TODO"""

        url = "https://api.notion.com/v1/blocks/" + blockID + "/children?page_size=" + str(size)
        return json.loads(self.DoGetRequest(url))['results']


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