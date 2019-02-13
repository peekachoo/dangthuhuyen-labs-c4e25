import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds213705.mlab.com:13705/krsmip

host = "ds213705.mlab.com"
port = 13705
db_name = "krsmip"
user_name = "huyenhuyen"
password = "huyen2"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())