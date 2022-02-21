This project is a simple python integration of the notion API


# Get Started

## Initialize

`You can specify a notion version like this : Notion('YOUR_SECRET_TOKEN','2021-08-16')`

```python
import NotionModule

instance = NotionModule.Notion('YOUR_SECRET_TOKEN')
```

## Retreive a page

`This method return a NotionPage object.`

```python
page = instance.GetPage('PAGE_ID')
```

## Retreive the page content

`This method return an array of NotionBlock objects.`

```python
page = instance.GetPage('PAGE_ID')
size = 100
content = GetPageContent( page ,size )
```

## Retreive a block

`This method return a NotionBlock object.`

```python
block = instance.GetBlock('BLOCK_ID')
```

## Retreive sub-blocks

`This method return an array NotionBlock object.`

```python
block = instance.GetSubBlock('PARENT_BLOCK_ID')
```

## Retreive a database

`This method return an array of NotionPage objects`

```python
size = 100
database = instance.GetDatabase('DATABASE_ID',size)
```

# Objects properties

## NotionPage

```
id : id of the page
name : title of the page
properties : json containing all the properties of the page
created_by : json user object
url : url of the page
has_children : true if the page have childrens
```

## NotionBlock

```
id : id of the block
type : type of block
created_by : json user object
created_time : created time of the block
has_children : true if the block have children
json_content : if exists, json content of the block
```
