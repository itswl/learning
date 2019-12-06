from pymongo import MongoClient
from dataclasses import dataclass
from bson.objectid import ObjectId


@dataclass
class Test_Mongo():
    client:dict = MongoClient()
    db:dict = client['test']  # 连接到 test 数据库
    
    def get_one(self):
        return self.db.students.find_one({'sex':'male'})

    def get_more(self):
        return self.db.students.find({'sex':'male'})

    def get_one_from_oid(self, oid):
        obj = ObjectId(oid)
        return self.db.students.find_one({'_id': obj})


def main():
    obj = Test_Mongo()
    print(obj.get_one())
    for item in obj.get_more():
        print(item['_id'])
    print(obj.get_one_from_oid('5de8b35c75deb540ecfc5340'))

if __name__ == '__main__':
    main()

