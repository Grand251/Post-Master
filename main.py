from pymongo import MongoClient
from fastapi import FastAPI, HTTPException

from models import Letter

mongo_client = MongoClient()
postmaster_db = mongo_client['postmaster']
letters_collection = postmaster_db['letters']

app = FastAPI()

#letters = [
#        Letter(sender='Tester', title='To Santa', body='Hey Santa, I...'),
#        Letter(sender='Tester1', title='To Santa', body='Dear Santa, I...')
#    ]


@app.get('/')
def index():
    return {'msg': 'Hell Yeah!'}


@app.post('/letters')
def send_letter(letter: Letter):
    letters_collection.insert_one(letter.dict())
    #letters.append(letter)


@app.get('/letters')
def all_letters():
    letters = [Letter(**letter) for letter in letters_collection.find()]
    return letters


@app.get('/letters/{sender}')
def get_letter(sender: str):
    for letter in letters_collection.find():
        if letter.sender == sender:
            return letter
    return HTTPException(status_code=404, detail='Letter not found.')
