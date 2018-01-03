from InstagramAPI import InstagramAPI

username = 'okushy'
pwd = 'Aharenar1'
user_id = 'okushy1616'

API = InstagramAPI(username,pwd)
API.login()

query = API.searchTags("おしゃかわ")
print(query)
