from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    
    with open('expense_report.csv', 'a', newline='') as expenses_file:
        expenses_writer = csv.writer(expenses_file)
        expenses_writer = expenses_writer.writerow([infos['label'], infos['amount'], infos['spender']])

    print("Expense Added !")
    return True

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },

]

def new_user(*args):
    infos = prompt(user_questions)
    
    with open('users.csv', 'a', newline='') as users_file:
        users_writer = csv.writer(users_file)
        users_writer = users_writer.writerow([infos['name']])

    print("User Added !")
    return True