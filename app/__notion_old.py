import requests, json, random

def getDatabase(url):
    url = "https://api.notion.com/v1/databases/"+ url + "/query"
    payload = {"page_size": 100}
    headers = {

        "Accept": "application/json",

        "Notion-Version": "2021-08-16",

        "Content-Type": "application/json",

        "Authorization": "Bearer secret_xM6R0RWZX6Uykc3qidCGWeBLaUP1RtMytzqLuW8OvV8"

    }
    response = requests.request("POST", url, json=payload, headers=headers)
    #print(response.text)
    return response.text

def GetPageInfo(pageID):
    url = "https://api.notion.com/v1/pages/" + pageID
    return DoRequest(url)

def GetPage(pageID):
    url = "https://api.notion.com/v1/blocks/" + pageID
    return DoRequest(url)

def GetSubPage(pageID):
    url = "https://api.notion.com/v1/blocks/" + pageID + "/children?page_size=100"
    return DoRequest(url)

def GetallPagesContent():
    data = getDatabase('3e65af738fbb4949b08893777dca541c')
    data = json.loads(data)
    pages = data['results']
    result = []
    for page in pages:

        status = json.loads(GetPageInfo(page['id']))['properties']['Status']['select']['name']
        categories_raw = json.loads(GetPageInfo(page['id']))['properties']['Categorie']['multi_select']
        categories = []
        for categorie in categories_raw:
            categories.append(categorie['name'])
        titre = json.loads(GetPage(page['id']))['child_page']['title']
        content = json.loads(GetSubPage(page['id']))['results'][0]['code']['text'][0]['text']['content']

        all_infos = { 
            'id': page['id'],
            'page': titre, 
            'status': status, 
            'categories': categories, 
            'content': content
        }
        result.append(all_infos)

    return result 

def GenerateArraysOfCategories(arr):
    seance_notion = {
        'Fessiers':[],
        'Bras':[],
        'Global':[],
        'Abdos':[],
        'Cardio':[],
        'Jambes':[],
    }
    for page in arr:
        seance_notion[page['categories'][0]].append(page)
    return seance_notion

def DoRequest(url):
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Authorization": "Bearer secret_xM6R0RWZX6Uykc3qidCGWeBLaUP1RtMytzqLuW8OvV8"
    }
    response = requests.request("GET", url, headers=headers)
    return response.text

def RandomFromArray(arr):
    return arr[random.randint(0, len(arr) - 1)]

def createPage(databaseId, title, objectif, duree, nb_training):
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "Bearer secret_xM6R0RWZX6Uykc3qidCGWeBLaUP1RtMytzqLuW8OvV8"
    }
    createUrl = 'https://api.notion.com/v1/pages'
    newPageData = {
        "parent": {"type":"database_id", "database_id": databaseId },
        "properties": {
            "Name": {
                "title": [
                {
                    "type": "text",
                    "text": {
                    "content": str(title)
                    }
                }
                ]
            },
            "Objectif": {
                "rich_text": [
                    {
                        "text": {
                            "content": str(objectif)
                        }
                    }
                ]
            },
            "Durée": {
                "rich_text": [
                    {
                        "text": {
                            "content": str(duree) + " Mois"
                        }
                    }
                ]
            },
            "Training/Semaine": {
                "rich_text": [
                    {
                        "text": {
                            "content": str(nb_training) + " Entrainements par semaine"
                        }
                    }
                ]
            }
        }
    }
    
    
    data = json.dumps(newPageData)
    # print(str(uploadData))

    res = requests.request("POST", createUrl, headers=headers, data=data)
    return json.loads(res.text)['id']

def appendBlock_H1(page_id, title):
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "Bearer secret_xM6R0RWZX6Uykc3qidCGWeBLaUP1RtMytzqLuW8OvV8"
    }
    createUrl = 'https://api.notion.com/v1/blocks/' + page_id + '/children'
    newBlock = {
        "children": [
            {
                "type": "heading_1",
                "heading_1": {
                    "text": [{
                        "type": "text",
                        "text": {
                            "content": str(title)
                        }
                    }]
                }
            }
        ]
    }
    
    data = json.dumps(newBlock)
    # print(str(uploadData))

    res = requests.request("PATCH", createUrl, headers=headers, data=data)
    return res.text

def appendBlock_H2(page_id, title):
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "Bearer secret_xM6R0RWZX6Uykc3qidCGWeBLaUP1RtMytzqLuW8OvV8"
    }
    createUrl = 'https://api.notion.com/v1/blocks/' + page_id + '/children'
    newBlock = {
        "children": [
            {
                "type": "heading_2",
                "heading_2": {
                    "text": [{
                        "type": "text",
                        "text": {
                            "content": str(title)
                        }
                    }]
                }
            }
        ]
    }
    
    data = json.dumps(newBlock)
    # print(str(uploadData))

    res = requests.request("PATCH", createUrl, headers=headers, data=data)
    return res.text

def appendBlock_PageLink(page_id, link):
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "Bearer secret_xM6R0RWZX6Uykc3qidCGWeBLaUP1RtMytzqLuW8OvV8"
    }
    createUrl = 'https://api.notion.com/v1/blocks/' + page_id + '/children'
    newBlock = {
        "children": [
            {
                "type": "link_to_page",
                "link_to_page": {
                    "type": "page_id",
                    "page_id": str(link)
                }
            }
        ]
    }
    data = json.dumps(newBlock)
    # print(str(uploadData))
    res = requests.request("PATCH", createUrl, headers=headers, data=data)
    return res.text
