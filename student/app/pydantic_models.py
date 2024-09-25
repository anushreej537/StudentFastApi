from pydantic import BaseModel,AnyUrl

class AddStudentDetail(BaseModel):
    studentName : str
    email : str
    password : str
    phoneNumber : int
    marks : float
    address : str
    # marksheet : AnyUrl

    class Meta:
        table ='studentdetail'
    

class DeleteStudent(BaseModel):
    id : int