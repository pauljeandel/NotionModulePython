import NotionModule

instance = NotionModule.Notion('secret_xM6R0RWZX6Uykc3qidCGWeBLaUP1RtMytzqLuW8OvV8')


page = instance.GetPage('29d13803fdd24b2bb4229bf6d19755cb')
content = instance.GetPageContent(page, 10)
for i in content:
    print(i.id)
    print(i.type)
    print(i.created_by)
    print(i.created_time)
    print(i.has_children)
    print(i.json_content)
    print('\n')


