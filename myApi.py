from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# GET get a information
# POST create something new
# PUT update
# DELETE delete something

students = {
    1 : {
        "first_name" : "mossab",
        "last_name" : "Errahal",
        "age":"",
        "grade":"m1"
    },
    2 : {
        "first_name" : "aboubakr",
        "last_name" : "krid",
        "age":"",
        "grade":"l2"
    },
    3 : {
        "first_name" : "nini",
        "last_name" : "khalid",
        "age":"",
        "grade":"l1"
    },
    4 : {
        "first_name" : "llaho a3lam",
        "last_name" : "saad",
        "age":"22",
        "grade":"l3"
    }
}

class CreateStudent(BaseModel):
    first_name : str
    last_name : str
    age : int
    grade : str

class Student(BaseModel):
    id: int
    first_name : str
    last_name : str
    age : int
    grade : str

@app.get("/")
def root():
    return {'hello':'home page'}

@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(..., description="the id of a specific student  student_id", gt=0)):# , lt=5 less than 4 khas nresha 3la hsab max dyal database
    return students[student_id]

@app.get("/get-by-first-name/{first_name}")
def get_student(first_name : str = Path(..., description="the first_name of a specific student")):
    for i in students:
        print("getting the student by first name\n")
        if students[i]["first_name"] == first_name:
            return students[i]
    return {"error": "student not found"}

@app.get("/get-by-last-name")
def get_student(last_name : str = Path(..., description="the last_name of a specific student")):
    print("getting the student by last name\n")
    for i in students:
        if students[i]["last_name"] == last_name:
            return students[i]
    return {"error": "student not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student : Student):
    if student_id in students:
        return {"error": "user alrady exists with this id"}
    students[student_id] = student
    return students[student_id]

class UpdateStudent(BaseModel):
    first_name : Optional[str] = None
    last_name : Optional[str] = None
    age : Optional[int] = None
    grade : Optional[str] = None

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "no user with this id"}
    if student.first_name:
        students[student_id]["first_name"] = student.first_name
    if student.last_name:
        students[student_id]["last_name"] = student.last_name
    if student.age:
        students[student_id]["age"] = student.age
    if student.grade:
        students[student_id]["grade"] = student.grade
    return students[student_id]
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "student does not exist"}
    del students[student_id]
    return {"message": "student has been deleted"}