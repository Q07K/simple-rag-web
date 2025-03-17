from apis.api_wrapper import ApiWrapper
from apis.chats_api import generate_initiate

ApiWrapper().login("test@test.com", "test")
for i in generate_initiate(0, 100, "안녕"):
    print(i)
