import requests

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "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"

    def getUser (self, username):
        response = requests.get(self.api_url+"/users/"+username ) # get ile bir rest api oluşturulur "get isteği"
        return response.json() # jsonu import etmeye gerek kalmadı 

    def getRepositories(self, username):
        response = requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json()
    
    def createRepository(self, name):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        data = {
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://sadiktruan.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }

        response = requests.post(
            f"{self.api_url}/user/repos",
            headers=headers,
            json=data
        )
        return response.json()

github = Github()


while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ")

    if secim == "4":
        break
    else:
        if secim== "1":
            username = input("username: ")
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} follower : {result['followers']}")
        elif secim == "2":
            username = input("username: ")
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name']) # repodaki dizilerden isimler bu şekilde çekiliyor
        elif secim == "3":
            name = input("repository name: ")
            result = github.createRepository(name)
            print(result)
        else:
            print("Yanlış seçim")