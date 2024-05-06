from fastapi import FastAPI
from data_models import NewStudent,UpdateStudent
# Creating an instance of our application
app = FastAPI(
    title="CRUD Operations",
    description="API for CRUD Operations"
)
students = {
    1: {"name": "anil", "age": 19}
}


@app.get("/")
def index():
    return "Welcome to the API : CRUD Operations"
#####################################################


@app.get("/students")
def get_students():
    return students
########################################################


@app.get("/student/{stu_id}")
def get_student(stu_id : int):
    if stu_id not in students:
        return f"No student found with the student id ={stu_id}"
    return students[stu_id]
######################################################


@app.post("/add-student")
def add_student(stu : NewStudent):
    if not students:
        new_id = 1
    else:
        new_id = max(students.keys()) + 1
    students[new_id] = stu.model_dump()
    return students[new_id]

##################################################################


@app.put("/update-student/{stu_id}")
def update_student(stu_id: int, stu: UpdateStudent):
    if stu_id not in students:
        return f"No Student found with student id ={stu_id}"
    if stu.name is not None:
        students[stu_id]["name"] = stu.name
    if stu.age is not None:
        students[stu_id]["age"] = stu.age
    return students[stu_id]
#######################################################

@app.delete("/delete-student/{stu_id}")
def delete_student(stu_id:int):
    if stu_id not in students:
        return f"No Student found with student id ={stu_id}"
    del students[stu_id]
    return students






