import json
import os

File = "teacher_manager.json"

class Teacher:
    if not os.path.exists(File):
        with open(File, "w") as f:
            json.dump({"teacher": []}, f)
            
    def Load_data(self):
        with open(File, "r") as f:
            data = json.load(f)
            return data

    def Save_data(self, data):
        with open(File, "w") as f:
            json.dump(data, f, indent=4)
            
    def Add_teacher(self):
        try:
            name = str(input("Enter teacher name: "))
            subject = str(input("Enter subject name: "))
            teacher_id = int(input("Enter ID: "))
            while True:
                cls = int(input("Enter class name (1 to 12): "))
                if 1 <= cls <= 12:
                    break
                else:
                    print("please write (1 - 12)")
            salary = int(input("Enter salary: "))
        except ValueError:
            print("fill correct..")    
        teacher = {
                           "teacher_id": teacher_id,
                           "name": name,
                            "subject": subject,
                            "class": cls,
                            "salary": salary
                            }
        data = Teacher.Load_data(self)
        data["teacher"].append(teacher) 
        Teacher.Save_data(self, data)
        print(f"{name} has added successfully..")
        
            
    def Update_teacher_info(self):
        
        data = Teacher.Load_data(self)
        try:
            Teacher_id_check = int(input("Enter Teacher ID: "))
        except ValueError:
            print("invlid sytext")
            return
            
        for item in data["teacher"]:
            if Teacher_id_check == item["teacher_id"]:
                print("id find succesefully")
            else:
                print("")
             
            print("1). new name\n2). new subject\n3). new class\n4). new salary\n5). teacher ID\n6). Exit..")
            user_choice = int(input("Enter choice (1 - 6): "))
            
            if user_choice == 1:   
                new_name = str(input("new name: "))
                item["name"] = new_name
                break
                
            
            elif user_choice ==2:
                new_subject = str(input("Enter subject: "))
                item["subject"] = new_subject
                break
            
            elif user_choice == 3:
                new_cls = int(input("Enter class: "))
                item["class"] = new_cls
                break
            
            elif user_choice == 4:
                new_salary = int(input("Enter salary: "))
                item["salary"] = new_salary
                break
                
            elif user_choice == 5:
                new_id = int(input("Enter id: "))
                item["teacher_id"] = new_id
                break
                
            elif user_choice == 6:
                print("Existing.....")
                break
                
            else:
                print("VolueError")
                return 
         
        
        Teacher.Save_data(self, data)
                
    def Show_all(self):
        data = Teacher.Load_data(self)
        
        print(data)

    def Search_teacher_info(self):
        data = Teacher.Load_data(self)
        teacher_id_ = int(input("enter id: "))
        
        for t in data["teacher"]:
            if t["teacher_id"] == teacher_id_:
                print(t)
                
    def Delete_info(self):
        data =Teacher.Load_data(self)
        
        user = int(input("Enter id: "))
        for item in data["teacher"]:
            if user == item["teacher_id"]:
                print("1")
                data["teacher"].pop(user -1)
                print("2")
                print(item)
                
        Teacher.Save_data(self, data)
            
            
            