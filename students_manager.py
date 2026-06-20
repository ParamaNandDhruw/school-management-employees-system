import sqlite3

FIle = "student_manager.db"

core = sqlite3.connect(FIle)
cursor = core.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS student_manager(
                            student_id INTEGER PRIMARY KEY,
                            name TEXT, 
                            parents TEXT, 
                            cls INTEGER,
                            age INTEGER,
                            admission INTEGER)'''
                            )
core.commit() 



class Student:
      
    def Add_Student(self):
        try:
            name = str(input("Enter Student name: "))
            parents = str(input("Enter parents name (Mr/Miss): "))
            while True:
                clss = int(input("Enter class name: (1 - 12): "))
                vilidetion = 1 <= clss <=12
                if clss == vilidetion:
                    break
                
            age = int(input("Enter age: "))
            admission = int(input("Enter admission year (20XX): "))
        
        except ValueError:
            print("please Enter velid info..")
            return
        
               
        cursor.execute("INSERT INTO student_manager(name, parents, cls, age,  admission) VALUES (?,?, ?, ?, ?)",       (name, parents, clss, age, admission ))  
        
        core.commit()
        print("added succesfully..")
        
        
    def Search_id(self):
        try:
            student_id = int(input("Enter student id: "))
        except ValueError:
            print("please give me correct id..")
            return
        
        cursor.execute("SELECT * FROM student_manager WHERE student_id=? ",
                                         (student_id,))
       
        data = cursor.fetchone()
        print("ID: ",data[0])
        print("NAME: ", data[1])
        print("PARENTS: ",data[2])
        print("CLASS: ", data[3])
        print("AGE: ", data[4])
        print("ADMISSION: ", data[5])
                                     
    
    def Show_all(self):
        cursor.execute("SELECT * FROM student_manager")
        data = cursor.fetchall()
        print(data)
        
        
    def Updete_id(self):
        try:
            Update_id = int(input("Enter ID: "))
            new_name = str(input("Enter new name: "))
            new_parents = str(input("Enter new parents name: "))
            new_cls = int(input("Enter new class: "))
            new_age = int(input("Enter new age: "))
            new_admission = int(input("Enter new admission date: "))
        except ValueError:
            print("id not found..")
            return
           
        
        cursor.execute("UPDATE student_manager SET name=?, parents=?, cls=?, age=?, admission=? WHERE student_id=?  " ,
                                    (new_name, new_parents,new_cls,new_age,new_admission,Update_id))
        
        if cursor.rowcount > 0:
            print("Student info Update succefully.")
        else:
            print("Update agien")
        core.commit()
        

    def Delete_info(self):
        try:
            Delete_id = int(input("Enter ID: "))
        except ValueError:
            print("invalid enter..")
            return
        
        cursor.execute("DELETE FROM student_manager WHERE student_id=?",
                                       (Delete_id,)  )
        core.commit()
        print("Deleted succesfully..")

