def team_members():
    import sys
    global members
    members={}
    number_people=int(input("Enter the number of people in the workshop:  ")) 
    if number_people<=1 or number_people>8:
        print("The number of people in the workshop is either too less or too much, we can't handle the workshop with this amount of people ")
        sys.exit()
    else:
        for i in range(number_people):
            name=str(input("Enter the person's name:  "))
            availability=input("Enter the day(s) that the people can work for:  ")
            members[name]=availability
    print(members)
team_members()

def task_entry():
    global task 
    import sys
    task_track=0
    for i in members.keys():
        i=input("Enter a certain time period for you to work for (Based on Hours), and also give the Deadline for the task:(Format- Time Period: -Am/PM to -AM/PM) Deadline: date/day):    ")   
        task=input("Enter your task to be done today:  ")
    Continuous_task=str(input("Enter your task completion:  "))
    if Continuous_task=="Done" or "done":
        task_track+=1
        sys.exit()
    else:
        print("You have to work until you are done for the day")
    print(Continuous_task)
    print(task)
task_entry()

def Assignment_rules():
    import sys
    Assignment_Tasks=int(input("Enter a number:  "))
    if Assignment_Tasks==1:
        print(f"{task} is specifically for you")
    elif Assignment_Tasks==2:
        print(f"{task} is split amoung your team")
    elif Assignment_Tasks==3:
        print(f"{task} is un-assigned, please wait for further notice")
    else:
        print(f"This option is invalid, please try again with a new option")
        sys.exit()
Assignment_rules()

            
    