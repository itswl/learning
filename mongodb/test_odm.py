from odm import Grade, Student

class TestMongoEngine:
    def add_one(self):
        math = Grade(name = '数学', score = 90)
        English = Grade(name = '英语', score = 89.5)

        stu_obj = Student(
            name =  'weilai',
            age = 22,
            sex = 'male',
            grades = [math, English]
        )
        stu_obj.remake = 'remake'  # 动态插入
        stu_obj.save()
        return stu_obj

    def get_one(self):
        return Student.objects.first()

    def get_more(self):
        return Student.objects.all()
    
    def get_from_oid(self, oid):
        return Student.objects.filter(pk=oid).first()  # 根据id 得到一条数据
         
    def update_more(self):
        return Student.objects.filter(sex='male',age__gt=20).update(inc__age=10)

    def update_one(self):
        return Student.objects.filter(sex='male',age__gt=20).update_one(inc__age=100)

    def delete_one(self):
        return Student.objects.filter(sex='male').first().delete()

    def delete_more(self):
        return Student.objects.filter(sex='male').delete()

def main():
    obj = TestMongoEngine()
    result = obj.add_one()
    print(result.pk)
    get_one = obj.get_one()
    print(get_one.id)
    print(get_one.name)
    print(obj.get_from_oid(get_one.id).id)
    rows = obj.get_more()
    for row in rows:
        print(row.sex)
    print(obj.update_more())
    print(obj.update_one())
    print(obj.delete_one())
    print(obj.delete_more())

if __name__ == '__main__':
    main()
