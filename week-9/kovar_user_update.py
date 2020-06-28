# ============================================
# Title:  kovar-user-update
# Author: Professor Krasso
# Date:   26 June 2020
# Modified by: Sarah Kovar
# Description: Updating and Deleting Documents
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

#update existing user by employee_id specified
db.users.update_one(
    {"employee_id": "0000001"},
    {
        "$set": {
            "email": "skovar@my365bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id": "0000001"}))
