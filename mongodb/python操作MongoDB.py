from pymongo import MongoClient
from dataclasses import dataclass
from bson.objectid import ObjectId


@dataclass
class Test_Mongo():
    client:dict = MongoClient()
    db:dict = client['test']  # 连接到 test 数据库
    
    def add_one(self):
        post = {
            'name': 'justin',
            'age': 18,
            'sex': 'male',
            'grade': 80
        }
        return self.db.students.insert_one(post)

    def add_many(self):
        return self.db.students.insert_many([{'name':i} for i in range(0,10)])


    def get_one(self):
        return self.db.students.find_one({'name':'justin'})

    def get_more(self):
        return self.db.students.find({'sex':'male'})

    def get_one_from_oid(self, oid):
        obj = ObjectId(oid)
        return self.db.students.find_one({'_id': obj})

    def get_count(self):
        return self.db.students.estimated_document_count()


    def update_one(self):
        return self.db.students.update_one({'name':'justin'},{'$inc':{'age':10}})

    def update_many(self):
        return self.db.students.update_many({},{'$inc':{'age':5}})

    def delete_one(self):
        return self.db.students.delete_one({'name':'justin'})

    def delete_many(self):
        return self.db.students.delete_many({'name':'justin'})


def main():
    obj = Test_Mongo()
    print(obj.add_one().inserted_id)
    print(obj.get_one())
    print(obj.add_many().inserted_ids)
    print(obj.get_count())
    for item in obj.get_more():
        print(item['_id'])
    print(obj.get_one_from_oid(obj.add_one().inserted_id))
    print(obj.update_one().matched_count)
    print(obj.update_one().matched_count)
    print(obj.update_many().matched_count)
    print(obj.update_many().matched_count)
    print(obj.delete_one().deleted_count)
    print(obj.delete_many().deleted_count)


if __name__ == '__main__':
    main()
