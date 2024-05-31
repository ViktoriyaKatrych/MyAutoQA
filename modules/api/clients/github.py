import requests

class GitHub:

    def get_user_defunkt(self):
        r = requests.get('https://api.github.com/users/defunkt')
        body = r.json()

        return body
    
    def get_user(self, username):
        r =requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self,name):
        repositories = requests.get("https://api.github.com/search/repositories",
        params = {"q": name})                          
        body = repositories.json()

        return body
    
    def get_emo(self, nameicon):
        r = requests.get('https://api.github.com/emojis')
        body = r.json()
    
        kicon = body.get(nameicon)
        return kicon
   
    
    def get_commit(self, owner, repo, ref):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits/{ref}')
        body = r.json()
        return body
    
