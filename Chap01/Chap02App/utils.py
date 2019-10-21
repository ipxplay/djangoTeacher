import os

filepath = os.path.join(os.path.dirname(__file__),r"config\user.txt")
with open(filepath,"r",encoding="utf-8") as f:
    userinfo = f.readlines()
print(userinfo)