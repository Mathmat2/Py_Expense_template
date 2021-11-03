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
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices":[],
    },

]



def new_expense(*args):
    with open('users.csv', 'r', newline='') as users_file:
        users_reader = csv.reader(users_file)
        users = []

        for row in users_reader:
            users.append(row[0])

    if len(users) == 0:
        print('No Spender To Choose From ! Please Create A User First')
        return True

    expense_questions[2]['choices'] = users

    infos = prompt(expense_questions)
    
    with open('expense_report.csv', 'a', newline='') as expenses_file:
        expenses_writer = csv.writer(expenses_file)
        expenses_writer = expenses_writer.writerow([infos['label'], infos['amount'], infos['spender']])

    print("Expense Added !")
    return True