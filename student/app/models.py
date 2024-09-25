from tortoise import fields
from tortoise.models import Model 


class AddStudent(Model):
    studentId = fields.IntField(pk=True, index=True)
    studentName = fields.CharField(250)
    email = fields.CharField(250)
    password = fields.CharField(250)
    phoneNumber = fields.BigIntField()
    marks = fields.FloatField()
    address = fields.CharField(250)
    marksheet = fields.TextField(null=True)

    def __str__(self) -> str:
        return self.studentName
    
