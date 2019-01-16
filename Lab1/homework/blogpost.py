from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_database()
posts = db["posts"]

new_post = {
    "title": "GUYS GUESS THESE SONGS!",
    "author": "Peekachoo",
    "content": '''
    1. Easy - A Imagine Dragon's song:
        Vuông!
        Tròn méo méo vuông tròn méo méo vuông tròn tròn méo.
        Méo vuông tròn.
        Vuông!
        Tròn méo méo vuông tròn méo méo vuông tròn tròn méo.
        Méo vuông tròn.
        Méo!
        Tròn vuông tròn vuông tròn vuông tròn vuông tròn méo.
        Tròn vuông tròn vuông tròn vuông tròn vuông tròn.
        Vuông!
        Tròn méo méo vuông tròn méo méo vuông tròn tròn méo.
        Méo vuông tròn.
    Answer: https://www.youtube.com/watch?v=7wtfhZwyrcc&t=53s
    
    2. Normal - Bigbang's song: 
        Tròn tròn vuông vuông vuông / vuông vuông méo vuông tròn vuông. 
        Tròn tròn tròn tròn vuông vuông / méo méo vuông méo vuông vuông tròn.
        Tròn tròn tròn vuông vuông vuông vuông méo vuông tròn vuông / méo tròn.
        Tròn vuông méo méo méo méo vuông méo vuông vuông tròn.
        Tròn tròn vuông vuông méo méo vuông tròn vuông.
        Tròn tròn tròn vuông vuông vuông méo-vuông tròn tròn-vuông
        Tròn tròn tròn vuông vuông méo / méo vuông tròn vuông. 
        Méo vuông tròn vuông. 
        Méo vuông tròn tròn méo vuông. 
        Tròn vuông. 
    Answer: https://www.youtube.com/watch?v=MzCbEdtNbJ0&t=87s

    3. Hard - A Son Tung MTP's song:
        Méo méo méo vuông tròn méo vuông.
        Tròn vuông vuông méo vuông méo méo vuông tròn vuông tròn.
        Méo méo méo vuông tròn méo vuông.
        Méo vuông vuông tròn vuông méo.
        Tròn vuông vuông tròn méo vuông vuông vuông tròn tròn vuông vuông.
        Tròn vuông méo vuông vuông vuông vuông tròn tròn.
        Vuông vuông tròn vuông tròn vuông méo tròn.
        Vuông tròn vuông méo tròn.
    Answer: https://www.youtube.com/watch?v=Llw9Q6akRo4&t=89s

    4. Insane - A classical song:
        Méo tròn vuông méo tròn vuông méo 
        Tròn tròn tròn tròn vuông vuông méo vuông 
        Tròn vuông méo
        Tròn vuông vuông méo vuông tròn vuông tròn tròn vuông tròn
        Méo vuông tròn
        Vuông tròn vuông vuông tròn vuông vuông tròn vuông méo tròn
        Vuông tròn vuông

        Vuông méo tròn tròn vuông vuông vuông tròn vuông méo vuông
        Tròn vuông méo
        Vuông tròn vuông tròn tròn vuông méo vuông vuông tròn vuông
        Tròn vuông méo
        Tròn tròn vuông méo vuông tròn vuông méo vuông méo tròn
        Méo vuông tròn
        Vuông tròn vuông tròn tròn tròn vuông vuông vuông méo tròn
        Méo vuông tròn
        Vuông tròn vuông vuông méo vuông vuông méo tròn vuông vuông
    Answer: https://www.youtube.com/watch?v=xl-fXIgiITQ&t=140s

    4. Impossible (or super easy?) - A random song:
        Tròn tròn vuông tròn méo vuông.
        Tròn tròn vuông tròn méo vuông.
        Tròn tròn méo vuông méo méo vuông tròn.
        Tròn tròn vuông vuông tròn méo.

        Tròn tròn vuông tròn méo vuông.
        Tròn tròn vuông tròn méo vuông.
        Tròn tròn méo vuông méo méo vuông tròn.
        Méo méo vuông tròn méo vuông.
    Answer: https://www.youtube.com/watch?v=PSGQ9_qmSDY&t=36s
    ''',
}

posts.insert_one(new_post)
client.close()