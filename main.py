from Teacher_manager import Teacher
from students_manager import  Student
from stuff_manager import Stuff


def main(self):
    print("     ======== Schoole management/employees system ======== \n")
    while True:
        print("\n1). Tearcher record management\n2). Student record management\n3). Stuff record management\n4). Exit\n")
    
        try:
            user_input = int(input("Enter operation 1 - 4: "))
        except ValueError:
            print("please try 1 or 4 to numbers")
            continue
        
        if user_input == 1:
            print("1). Add Teacher\n2). Update Teacher\n3). Show all info\n4). Search Teachers\n5). Delete info\n6). Exist\n ")
            try:
                user = int(input("Enter 1 - 6: "))
            except ValueError:
                print("please Enter 1 - 6 to numbers\n")
                continue
            if user == 1:
                Teacher.Add_teacher(self)
                continue
                
            elif user == 2:
                Teacher.Update_teacher_info(self)
                continue
            
            elif user == 3:
                Teacher.Show_all(self)
                continue
            
            elif user == 4:
                Teacher.Search_teacher_info(self)
                continue
                
            elif user == 5:
                Teacher.Delete_info(self)
                continue
                
            elif user == 6:
                print("Exiting...")
                continue
                
            else:
                print("Volue Error....")
                continue
                
        elif user_input == 2:
            print("1). Add student\n2). Update student\n3). Search student\n4). Show all\n5). Delete\n6). Exit\n")
        
            try:
                user_choice = int(input("Enter operation 1 - 6: "))
            except ValueError:
                print("please try 1 - 6 to numbers\n")
                continue
            
            if user_choice == 1:
                Student.Add_Student(self)
                continue
            
            elif user_choice == 2:
                Student.Updete_id(self)
                continue
            
            elif user_choice == 3:
                Student.Search_id(self)
                continue
                
            elif user_choice == 4:
                Student.Show_all(self)
                continue
                
            
            elif user_choice == 5:
                Student.Delete_info(self)
                continue
            
            elif user_choice == 6:
                print("Exiting...\n")
                continue
                
            else:
                print("Volue Error....\n")
                continue
                
        elif user_input == 3:
            print("1). Add stuff\n2). Update stuff\n3). Search stuff'\n4). Show all\n5). Delete stuff \n6). Exit\n")
            
            try:
                user_choose = int(input("Enter 1 - 6: "))
            except ValueError:
                print("please enter 1 - 6 to number\n")
                continue
            
            if user_choose == 1:
                Stuff.Add_stuff(self)
                continue
                
            elif user_choose == 2:
                Stuff.Update_stuff_info(self)
                continue
            
            elif user_choose == 3:
                Stuff.Search_stuff_info(self)
                continue
                
            elif user_choose == 4:
                Stuff.Show_all(self)
                continue
                
            elif user_choose == 5:
                Stuff.Delete_info(self)
                continue
                
            elif user_choose == 6:
                print("Exiting....\n")
                continue
                
            else:
                print("Volue Error....\n")
                continue
                
        elif user_input == 4:
            print("Thanks for use this project, you have a good day.\nExiting....")
            break
        else:
            print("Volue Error.....")
            continue
main(self=0)    