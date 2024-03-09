from randomuser import RandomUser

import pandas as pd

random = RandomUser()

def get_users():

    users=[]

    for user in random.generate_users(10):
        users.append({
            "Name":user.get_full_name(),
            "Birthday":user.get_dob(),  
            "State":user.get_state(),
            "Email":user.get_email()
        })
    return pd.DataFrame(users)

df1 = get_users()

print(df1)