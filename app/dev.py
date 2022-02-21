import NotionModule

instance = NotionModule.Notion('secret_xM6R0RWZX6Uykc3qidCGWeBLaUP1RtMytzqLuW8OvV8')


page = instance.GetPage('29d13803fdd24b2bb4229bf6d19755cb')
print(page.token)


