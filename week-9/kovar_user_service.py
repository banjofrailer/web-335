# ============================================
# Title:  kovar-user-service
# Author: Professor Krasso
# Date:   26 June 2020
# Modified by: Sarah Kovar
# Description: Querying and Creating Documents
# ===========================================

#name displayed on screen
first_name = 'Sarah'
last_name = 'Kovar'
print(first_name + ' ' + last_name)


from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

#insert user into db
user = {

    "first_name": "Sheryl",

    "last_name": "Crow",

    "email": "rockstar@sherylcrow.com",

    "employee_id": "0000001",

    "date_created": datetime.datetime.utcnow()

}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

employee_id = "0000001"

#find and display search results
pprint.pprint(db.users.find_one({"employee_id": employee_id}))