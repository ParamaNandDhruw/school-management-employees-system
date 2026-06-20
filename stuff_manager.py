import json
import os

File = "stuff_manager.json"

class Stuff:
    if not os.path.exists(File):
        with open(File, "w") as f:
            json.dump({"stuff": []}, f)
            
    def Load_data(self):
        with open(File, "r") as f:
            data = json.load(f)
            return data

    def Save_data(self, data):
        with open(File, "w") as f:
            json.dump(data, f, indent=4)
            
    def Add_stuff(self):
        try:
            name = str(input("Enter stuff name: "))
            stuff_id = int(input("Enter ID: "))
            salary = int(input("Enter salary: "))
            work = str(input("Enter work"))
        except ValueError:
            print("fill correct..")    
        stuff = {
                           "stuff_id": stuff_id,
                           "name": name,
                           "salary": salary,
                           "work": work
                            }
        data = Stuff.Load_data(self)
        data["stuff"].append(stuff) 
        Stuff.Save_data(self, data)
        print(f"{name} has added successfully..")
        
            
    def Update_stuff_info(self):
        
        data = Stuff.Load_data(self)
        try:
            stuff_id_check = int(input("Enter stuff ID: "))
        except ValueError:
            print("invlid sytext")
            return
            
        for item in data["stuff"]:
            if stuff_id_check == item["stuff_id"]:
                print("id find succesefully")
            else:
                print("")
             
            print("1). new name\n2). work\n3).  new salary\n4). stuff ID\n). Exit..")
            user_choice = int(input("Enter choice (1 - 4): "))
            
            if user_choice == 1:   
                new_name = str(input("new name: "))
                item["name"] = new_name
                break
                
            
            elif user_choice ==2:
                new_work = str(input("Enter work: "))
                item["work"] = new_work
                break
            
                                   
            elif user_choice == 3:
                new_salary = int(input("Enter salary: "))
                item["salary"] = new_salary
                break
                
            elif user_choice == 4:
                new_id = int(input("Enter id: "))
                item["stuff_id"] = new_id
                break
                
            elif user_choice == 5:
                print("Existing.....")
                break
                
            else:
                print("VolueError")
                return 
         
        
        Stuff.Save_data(self, data)
                
    def Show_all(self):
        data = Stuff.Load_data(self)
        
        print(data)

    def Search_stuff_info(self):
        data = Stuff.Load_data(self)
        stuff_id_ = int(input("enter id: "))
        
        for t in data["stuff"]:
            if t["stuff_id"] == stuff_id_:
                print(t)
                
    def Delete_info(self):
        data =Stuff.Load_data(self)
        
        user = int(input("Enter id: "))
        for item in data["stuff"]:
            if user == item["stuff_id"]:
                print("1")
                data["stuff"].pop(user -1)
                print("2")
                print(item)
                
        Stuff.Save_data(self, data)
            
            
            