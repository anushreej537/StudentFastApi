from fastapi import APIRouter, Depends, UploadFile, File
from passlib.context import CryptContext
from . pydantic_models import AddStudentDetail,DeleteStudent
from . models import AddStudent
from datetime import datetime,timedelta
import os

app = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


@app.post('/studentdetail/')
async def post_studentdetail(data : AddStudentDetail = Depends(), marksheet: UploadFile=File(...)):
    if await AddStudent.exists(email = data.email):
        return {'msg':'student detail already exist'}   
    else:
        FILEPATH = "static/marksheetdoc"

        if not os.path.isdir(FILEPATH):
            os.mkdir(FILEPATH)

        filename = marksheet.filename
        extension = filename.split(".")[1]
        imagename = filename.split(".")[0]

        if extension not in ["pdf","docm","docx","doc"]:
            return {"status":"error", "detial":"File extension not allowed"}
        
        dt = datetime.now()
        dt_timestamp = round(datetime.timestamp(dt))

        modified_image_name = imagename+""+str(dt_timestamp)+""+extension
        genrated_name =  FILEPATH+ "/" +modified_image_name
        file_contant = await marksheet.read()

        with open(genrated_name, "wb")as file:
            file.write(file_contant)
            file.close()

        stu_obj = await AddStudent.create(studentName = data.studentName,
                                        email = data.email,password = get_password_hash(data.password),
                                        phoneNumber = data.phoneNumber, marks = data.marks,
                                        address = data.address,marksheet = genrated_name )
        return stu_obj



@app.get('/studentbyid/{studentId}')
async def get_studentdetailbyid(studentId : int):
    stu = await AddStudent.get(studentId = studentId)
    return stu

@app.delete('/deletestudent/{studentId}')
async def delete_studentdetailbyid(data : DeleteStudent):
    stu = await AddStudent.get(studentId = data.id)
    stu.delete()
    return {'msg':'delete successfully'}
