from fastapi import FastAPI

api = FastAPI(
    title='My API'
)

users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]

@api.get('/')
def welcome():
    return {'message':'welcome to my API'}

@api.get('/users')
def get_database():
    return users_db

@api.get('/users/{userid:int}')
def get_userinfo(userid):
    try:
        #user = users_db[user-1]
        user = list(filter(lambda x : x.get('user_id')==userid, users_db))[0]
        return user
    except IndexError:
        return {}
    

@api.get('/users/{userid:int}/name')
def get_username(userid):
    try:
        #user = users_db[user-1]
        user = list(filter(lambda x : x.get('user_id')==userid, users_db))[0]
        name = user['name']
        return name
    except IndexError:
        return {}
    
@api.get('/users/{userid:int}/subscription')
def get_usersubcription(userid):
    try:
        #user = users_db[user-1]
        user = list(filter(lambda x : x.get('user_id')==userid, users_db))[0]
        sub = user['subscription']
        return sub
    except IndexError:
        return {}