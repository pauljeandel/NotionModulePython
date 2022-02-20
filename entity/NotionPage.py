class NotionPage :

    def __init__(self, id, name, properties, created_by, url, has_children):
        self.id = id
        self.name = name
        self.properties = properties
        self.created_by = created_by
        self.url = url
        self.has_children = has_children

    def __str__(self):
        return self.name + "," + self.id + "," + self.url + "," + str(self.properties) + "," + str(self.created_by) + "," + str(self.has_children) 

