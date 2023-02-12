# =====importing libraries===========
import datetime
from datetime import datetime
from datetime import date

# =====function definition ===========
def reg_users(new_username, new_password):
    '''The function enables registration of a new user; that is called when the user selects "r" 
        to register a user'''
    menu_r = open("user.txt", "a", encoding="utf-8-sig")
    menu_r.write(f"\n{new_username}, {new_password}")
    menu_r.close()


def add_task(add_person, add_title, add_description, add_assigned_date, add_due_date, add_task_completed):
    '''The function enables adding a new task to file tasks.txt, 
        that is called when a user selects "a" to add a new task'''
    menu_a = open("tasks.txt", "a",encoding="utf-8-sig")  # Open 'tasks.txt' file
    menu_a.write(f"\n{add_person}, {add_title}, {add_description}, {add_assigned_date}, {add_due_date}, {add_task_completed}")
    menu_a.close()


def view_all(person, title, description, assigned_date, due_date, task_completed):
    '''The function is listed all the tasks in "tasks.txt", called when users type "va"  '''
    print(f"\n————————————————————————————————————————————————————————————————————————————————————————")  
    print(f"Task #{i+1}:\t{title}")
    print(f"Assigned to:\t{person}")
    print(f"Due date:\t{due_date}")
    print(f"Assigned date:\t{assigned_date}")
    print(f"Task complate:\t{task_completed}")
    print(f"Task description:\t{description}")
    print(f" ————————————————————————————————————————————————————————————————————————————————————————")


def view_mine(person, title, description, assigned_date, due_date, task_completed):
    '''Displaying tasks for the each user'''
    if person == username:         
        on=i+1          
        print(f"\n————————————————————————————————————————————————————————————————————————————————————————")
        print(f"Task #{on}:\t{title}")
        print(f"Assigned to:\t{person}")
        print(f"Due date:\t{due_date}")
        print(f"Assigned date:\t{assigned_date}")
        print(f"Task complate:\t{task_completed}")
        print(f"Task description:\t{description}")
        print(f"————————————————————————————————————————————————————————————————————————————————————————")
        vm_tasks[i+1]=[line] 


def generate_reports():
    '''The function generate reports creats two text files, called
task_overview.txt and user_overview.txt.

o The task_overview.txt contain:
    ▪ The total number of tasks that have been generated and tracked using the task_manager.py.
    ▪ The total number of completed tasks.
    ▪ The total number of uncompleted tasks.
    ▪ The total number of tasks that haven’t been completed and that are overdue.
    ▪ The percentage of tasks that are incomplete.
    ▪ The percentage of tasks that are overdue.
o The user_overview.txt should contain:
    ▪ The total number of users registered with task_manager.py.
    ▪ The total number of tasks that have been generated and tracked using task_manager.py.
▪ For each user also describe:
    ▪ The total number of tasks assigned to that user.
    ▪ The percentage of the total number of tasks that have been assigned to that user
    ▪ The percentage of the tasks assigned to that user that have been completed
    ▪ The percentage of the tasks assigned to that user that must still be completed
    ▪ The percentage of the tasks assigned to that user that have not yet been completed and are overdue
'''
    task_gr = open("tasks.txt", "r",encoding="utf-8-sig")
    lines = task_gr.readlines()
    task_gr.close()
    # Create a list with tasks
    total_task = []
    for line in lines:
        total_task.append(line)
    # Creating a lists for raport
    unfinished_stat=[]
    finished_stat=[]
    overdute_stat=[]
    no_tasks_overdue=0
    for line in lines:
        line = line.strip()
        l=line.split(', ')
        if l[5]=='No': # Comput of the unfinished number task
            unfinished_stat.append(l)
        if l[5]=='Yes':  # Comput of the finished number task
            finished_stat.append(l)
        
        # date operation            
        d = datetime.strptime(l[4], '%d %b %Y')
        
        if d<datetime.today()and l[5]!='Yes': # Comparison of execution date with NOW date'
            no_tasks_overdue+=1

    # Writing to the task_overview.txt file
    task_overview=open('task_overview.txt', "w",encoding="utf-8-sig") 
    task_overview.write(f'Date of Reports: {datetime.today()}\n')
    task_overview.write(f'————————————————————————————————————————————————————————————————————————————————————————\n')
    task_overview.write(f'The total number of tasks is: {len(total_task)}\n') 
    task_overview.write(f'Nubers of unfinished tasks: {len(unfinished_stat)}\n')
    task_overview.write(f'Nubers of finished tasks: {len(finished_stat)}\n')
    task_overview.write(f'The number of overdue tasks: {no_tasks_overdue}\n')
    task_overview.write(f'Persentage of unfinished tasks: {round(float(100*len(unfinished_stat))/len(total_task),2)}[%]\n')
    task_overview.write(f'Persentage of overdue tasks: {round(float(100*no_tasks_overdue)/len(total_task),2)}[%]\n') 
    task_overview.close() 

    # Users report
    file = open("tasks.txt", "r", encoding="utf-8-sig") 
    lines = file.readlines() 
    
    tasks=[]
    for i, line in enumerate(lines):
        line = line.strip()
        tab = line.split(', ')
        tasks.append(tab)

    user_gr = open("user.txt", "r", encoding="utf-8-sig")
    lines = user_gr.readlines() 
    user_gr.close() 

    us=[]
    for line in lines:
        line = line.strip() 
        tab_user = line.split(', ')
        user=tab_user[0]
        us.append(user)
    # Saving the report to a file
    user_overview=open('user_overview.txt', "w",encoding="utf-8-sig") 
    user_overview.write(f'Date of Reports: {datetime.today()}\n')
    user_overview.write(f'The namber of user is: {len(us)}\n')
    user_overview.write(f'The total namber of tasks is: {len(tasks)}\n')
    user_overview.write(f'————————————————————————————————————————————————————————————————————————————————————————\n')
    user_overview.close() 

    for i in range(0, len(us)):
        user_total_tasks = 0
        user_percentage_tasks = 0
        user_finished_stat= 0 
        user_unfinished_stat= 0
        user_overdute_stat= 0

        for j in range(0,len(tasks)):
            if us[i]==tasks[j][0]:
                user_total_tasks += 1
                if tasks[j][5]=='Yes': # Comput of the unfinished number task
                    user_finished_stat += 1 
                if tasks[j][5]=='No':  # Comput of the finished number task
                    user_unfinished_stat += 1

                d = datetime.strptime(tasks[j][4], '%d %b %Y')
        
                if d<datetime.today()and tasks[j][5]=='No': # Comparison of execution date with NOW date'
                    user_overdute_stat += 1
        
        # Report for each user          
        if user_total_tasks > 0:
            user_overview=open('user_overview.txt', "a",encoding="utf-8-sig") 
            user_overview.write(f'User: {us[i]}\n')
            user_overview.write(f'The the total number of tasks assigned to that user is: {user_total_tasks}\n')
            user_overview.write(f'The percentage of the total number of tasks assigned to that user is: {round(float(100*user_total_tasks)/len(total_task),2)}[%]\n')
            user_overview.write(f'The percentage of completed tasks: {round(float(100*user_finished_stat)/user_total_tasks,2)}[%]\n')
            user_overview.write(f'The percentage of uncompleted tasks: {round(float(100*user_unfinished_stat)/user_total_tasks,2)}[%]\n')
            user_overview.write(f'The percentage of overdue tasks: {round(float(100*user_overdute_stat)/user_total_tasks,2)}[%]\n')
            user_overview.close()    


def print_raports():
    ''' The function displays the contents of files: task_overview.txt, user_overview.txt'''
    generate_reports()
    file = open("task_overview.txt", "r", encoding="utf-8-sig")
    lines = file.readlines()
    file.close()
    
    for i, line in enumerate(lines):
        line = line.strip() 
        tab = line.split(', ')
        print(line)
    print("\n")

    # Ds for user_overview.txt
    file = open("user_overview.txt", "r", encoding="utf-8-sig")
    lines = file.readlines()
    file.close()
   
    for i, line in enumerate(lines):
        #ordinal_number(lines)
        #for i in range(1,len(lines)+1):
        line = line.strip()  # Remove whitespace from beginning and end of line (\n ' ')
        tab = line.split(', ')  # Assign sp         lit lines to tab array
        # Printing table elements with description
        print(line)


def readtask():
    all_tasks={}
    file = open("tasks.txt", "r", encoding="utf-8-sig")
    lines = file.readlines()
    file.close()
    for i,line in enumerate(lines): 
        all_tasks[i] = lines[i]
        i+=1
    return(all_tasks)
    
    print('These are all the tasks\n',all_tasks)


# ====Login Section====
'''The code allow a user to login.
    - Code read usernames and password from the user.txt file
    - Use dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
# Read the text file 'user.txt' and convert it to a dictionary
# Opening the file stored username and password
user_file = open("user.txt", "r", encoding="utf-8-sig")
lines = user_file.readlines()
user_file.close()
users = {}  # Create dictionary username: password
for line in lines:
    line = line.strip()
    tab = line.split(', ')
    users[tab[0]] = tab[1]
while True:
    username = input("Please enter your usrename: ")
    password = input("please enter your password: ")
    # Condition if the password value exists for the key username in the dictionary loop ends (break) goes to menu
    # When the usernnam key has no 'password' value in the users, the 'get' function returns 'None'
    if users.get(username, None) == password:
        break
    else:
        # Display message: "Your login is faild,try again"
        print("Your loggin is faild,try again ")
while True:
    # presenting the menu to the user and
    # making sure that the user input is coneverted to lower case.
    if username == "admin":  # Admin menu
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        gr - generate raports
        ds - display statistics
        e - Exit
            : ''').lower()
    else:  # Menu for all users
        menu = input('''Select one of the following Options below:
        va - View all tasks
        vm - view my task
        e - Exit
            : ''').lower()
    
    if menu == 'r' and username == "admin":  # Securing access to option 'r - Registering a user' for administrator only
        '''The code option "r" adds a new user to the user.txt file
        - This optionthe has following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        # Entering for  new user new username
        new_username = input("Please enter new username :")
        # Entering for  new user new username
        check_new_username=users.get(new_username,None)
        if check_new_username==None:
            new_password = input("Please enter password: ")
            # Confirmation the new possword
            confirm_password = input("Please confirm your password: ")
            while new_password!=confirm_password:
                print("password incorrect! Try again.")
                new_password = input("Please enter password: ")
            # Confirmation the new possword
                confirm_password = input("Please confirm your password: ")
            if new_password == confirm_password:  # Add condition of new user to flie 'user.txt'
                reg_users(new_username, new_password)
        else: 
            print("'username' already exists, please enter a new username")
            new_username = input("Please enter new username :")
            check_new_username=users.get(new_username,None)
            if check_new_username==None:
                new_password = input("Please enter password: ")
                # Confirmation the new possword
                confirm_password = input("Please confirm your password: ")
                if new_password == confirm_password:  # Add condition of new user to flie 'user.txt'
                    reg_users(new_username, new_password)

    elif menu == 'a' and "admin":  # Securing access to option 'a - Adding a task' for administrator only
        '''The code option "a" allow a user to add a new task to task.txt file
        - This optionthe has following steps::
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - The due date of the task.
                - The current date.
                - Status - Task complate: "No"
            '''
        
        person = input("Please enter the username of the person to whom you will assign this task: ")
        # Entering titel of the task
        title = input("Please enter titel of the task: ")
        # Entering description of the task
        description = input("Please enter short descriptio of the task: ")
        # Entering due date of the task
        due_date = datetime.strptime(input('Please enter due date of the task dd Mon. YYYY:'), '%d %b %Y') # Convert string to datetime object.
        due_date = due_date.strftime('%d %b %Y') # Convert date object to a string date
        # Set the current date
        # Assign to the variable 'assgned_date' today's date
        
        assigned_date = date.today() 
        assigned_date = assigned_date.strftime('%d %b %Y')
        task_completed = 'No'  # Marking task status as unfinished 'NO'
        # Adding a new task to the 'tasks.txt' file
        add_task(person, title, description, assigned_date, due_date, task_completed )
    
    elif menu == 'gr':
        generate_reports() # Call the function which generating reports files: task_overview.txt and user_overview.txt
          
    elif menu == 'ds' and "admin":  # Securing access to option ds - Display Statistics' for administrator only
        # Calling the "print_reports" function which displays the contents of the files: task_overview.txt and user_overview.txt
        print_raports()
      
    elif menu == 'va':
        '''The block of code which read the tasks from task.txt file and
         print to the console in the format:
            Task:
            Assigned to:
            Due date:
            Assigned date:
            Task Complete:
            Task descipion:
            '''
        file = open("tasks.txt", "r", encoding="utf-8-sig")
        lines = file.readlines()
        file.close()
        
        for i, line in enumerate(lines):
            line = line.strip()
            tab = line.split(', ')
            # Printing table elements with description
            view_all(tab[-6],tab[-5],tab[-4],tab[-3],tab[-2],tab[-1])       

    elif menu == 'vm':  # Execution of option 'vm' - reading tasks assigned to the user and printing formated output
        '''The block of code which read the tasks assigned to the login user from task.txt file and
         print to the console in the format:
            Task:
            Assigned to:
            Due date:
            Assigned date:
            Task Complete:
            Task descipion:
            '''
        file = open("tasks.txt", "r", encoding="utf-8-sig")
        lines = file.readlines()
        file.close()

        vm_tasks={}
        for i, line in enumerate(lines):
            line = line.strip()
            tab = line.split(', ')
            
            on=i
            # Calling the function to view all the tasks that have been assigned to the login user
            view_mine(tab[-6],tab[-5],tab[-4],tab[-3],tab[-2],tab[-1])
            
        all_tasks={}   
        choose=int(input('select task (-1 to return): '))
        if choose==-1: # Exit to main menu
            continue
        else:
            edit_task=(vm_tasks[choose]) # Substituting a specific task into a variable that I use in editing
            str_editT=edit_task[0] # Substitution of the value from the list [0] into the variable (type to string)
                   
            vm_menu = input('''Select one of the following Options below:
            ct - Mark the task as complet
            et - Edit a task
            -1 - Exit to main menu
            ''')
        #edit_task=[]
        if vm_menu=='ct':
            str_editT= str_editT.replace('No','Yes') # Changing task status from 'No to 'Yes'
            str_editT.strip()
            str_editT.split(', ')
            str_editT=str_editT+'\n'
            print(f'\n this is after status change "No" na "Yes":\n{type(str_editT)} {str_editT}')
            file_txt = open("tasks.txt", "w",encoding="utf-8-sig")
            for i,line in enumerate(lines): 
                all_tasks[i] = lines[i]  
                all_tasks[choose-1]=str_editT
                file_txt.write(all_tasks[i])
                i+=1 
                
            print('total after cheanging', all_tasks)
            file_txt.close()
            print('\ wstawiony z pliku task.txt po zmianie statusu na Yes i zapisie: ',readtask())
        
        elif vm_menu=='et':
                edit_username=input('Please enter new username:')
                edit_due_date = datetime.strptime(input('Please enter due date of the task:  dd Mon YYYY :'), '%d %b %Y') # Convert string to datetime object.
                edit_due_date  = edit_due_date .strftime('%d %b %Y') # Convert date object to a string date
                print(len(edit_task)) # Task which will be selected type list (variable choose)          
                ed=str_editT.split(',')
                ed[0]=edit_username # Replace item at index 0 [username]
                ed[4]=edit_due_date # Replace item at index 4 [due_date] 
                ed_str=','
                ed_str=ed_str.join(ed)+'\n'
                file_txt = open("tasks.txt", "w",encoding="utf-8-sig")
                for i,line in enumerate(lines): 
                    all_tasks[i] = lines[i]
                    all_tasks[choose-1]=ed_str
                    file_txt.write(all_tasks[i])
                    i+=1 
                file_txt.close()

    elif menu == 'e':  # Exit the program
        print('Goodbye!!!')
        exit()
    else:  # Display of a message about the wrong choice of menu option
        print("You have made a wrong choice, Please Try again")
