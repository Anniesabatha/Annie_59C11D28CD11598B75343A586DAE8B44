class student:
  def  __init__(self,name,rollno,cgpa):
        self.name=name
        self.rollno=rollno
        self.cgpa=cgpa
def sort_student(student_list):
  sorted_student=sorted(student_list ,key=lambda studen:studen.cgpa,reverse=True)
  return sorted_student
if __name__=="__main__":
  stu1=[student("anu",101,5),student("aruna",102,7),student("anju",103,8)]
  sorted_stu1=sort_student(stu1)
  print("sort_student(list 1):")
  for student in sorted_stu1:
    print(f"{student.name}_rollno:{student.rollno},cgpa:{student.cgpa}")
