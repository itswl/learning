
from mongoengine import connect, Document, StringField, IntField, \
    FloatField, EmbeddedDocument, ListField, EmbeddedDocumentField
connect('students') 
# connect('Test', host = '192.168.0.2', port=27017)
# connect('Test', host = 'mongodb://localhost/Test') 
SEX_CHOICE = (
    ('male', '男'),
    ('female', '女')
)

class Grade(EmbeddedDocument):
    '''  成绩信息  '''
    name =  StringField(required=True)
    score = FloatField(required=True)

class Student(Document):
    ''' 学生信息 '''
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    sex = StringField(choices=SEX_CHOICE, required=True)
    grade = FloatField()
    address = StringField()
    grades = ListField(EmbeddedDocumentField(Grade))  # 与 Grade 关联
    
