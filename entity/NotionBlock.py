class NotionBlock:

    def __init__(self, id, type, created_by, created_time, has_children, json_content):
        self.id = id
        self.type = type
        self.created_by = created_by
        self.created_time = created_time
        self.has_children = has_children
        self.json_content = json_content

    def __str__(self):
        return self.type + "," + self.id + "," + str(self.created_by) + "," + str(self.created_time) + "," + str(self.has_children) + "," + str(self.json_content)

