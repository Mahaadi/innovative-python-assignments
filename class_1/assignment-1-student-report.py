name=input("Enter Student Name:")
age=int(input("Enter Age:"))
roll=int(input("Enter Roll Number:"))
math=int(input("Enter Marks in Math:"))
science=int(input("Enter Marks in Science:"))
english=int(input("Enter Marks in English:"))


print("Student Report:")
print("-----------------------")
print("Name : ", name)
print("Age : ", age)
print("Roll Number : ", roll)
print("Total Marks :", (math + science + english))
print("Average :", (math + science + english)/3)


