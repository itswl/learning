from mongoengine import connect, Document, StringField, IntField, \
    FloatField, EmbeddedDocument, ListField, EmbeddedDocumentField, DynamicDocument # 可以在后面插入其他关键字
connect('test')   # 连接的数据库
# connect('test', host = '192.168.0.2', port=27017)
# connect('test', host = 'mongodb://localhost/test') 
SEX_CHOICE = (
    ('male', '男'),
    ('female', '女')
)

class Grade(EmbeddedDocument):
    '''  成绩信息  '''
    name =  StringField(required=True)
    score = FloatField(required=True)

class Student(DynamicDocument):   # 可以在后面插入其他关键字
    ''' 学生信息 '''
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    sex = StringField(choices=SEX_CHOICE, required=True)
    grade = FloatField()
    address = StringField()
    grades = ListField(EmbeddedDocumentField(Grade))  # 与 Grade 关联
    
    meta = {
        'collection': 'students'  # 指定连接的集合
    }
