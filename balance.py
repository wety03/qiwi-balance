from SimpleQIWI import *

token=input('token:     ')
phone=input('phone:     ')

api = QApi(token=token, phone=phone)

print(api.balance)