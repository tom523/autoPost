from autoPost import www51cto


def read_txt(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines


line = read_txt('userPass.txt')
username = line[0].split(' ')[0]
password = line[0].split(' ')[1]
print("username:" + username)
print("password:" + password)
client = www51cto.login(username, password)
if client:
    title = "今天更新4条招聘信息"
    content_html = "<p>招聘工程师</p>"
    tags = "recruitment"
    artical_url = www51cto.postlog(client, title, content_html, tags)
    if artical_url:
        print(artical_url)
    else:
        print("发表失败")
else:
    print("登陆失败")




