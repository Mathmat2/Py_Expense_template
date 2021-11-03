from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },

]

def add_user():
    infos = prompt(user_questions)
    
    with open('users.csv', 'a', newline='') as users_file:
        users_writer = csv.writer(users_file)
        users_writer = users_writer.writerow([infos['name']])

    print("User Added !")
    return True