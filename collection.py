# create a sample collection

users = {'Hans': 'Active', 'James': 'Unactive', 'Andrew': 'Active'}

#strategy: iterate over a copy

for user, status in users.copy().items():
    if status == 'Inactive':
        del users[user]
        
# strategy: Create a new collection  

Active_users = {}
for user, status in users.items():
    if status == 'Active':
        Active_users[user] = status      