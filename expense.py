from PyInquirer import prompt
import csv

# Allow to delete chosen spender from involved people list
def delete_spender_from_involved_choice(answers):
    spender = answers['spender']
    expense_questions[3]['choices'].remove({'name' : spender})
    return True

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
    {
        "type":"checkbox",
        "name":"involved",
        "message":"New Expense - Involved People: ",
        "choices":[],
        "when":delete_spender_from_involved_choice
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

    involved_people = []
    for user in users:
        involved_people.append({'name': user})

    print(involved_people)
    
    expense_questions[3]['choices'] = involved_people

    infos = prompt(expense_questions)

    infos['involved'].append(infos['spender'])
    
    with open('expense_report.csv', 'a', newline='') as expenses_file:
        expenses_writer = csv.writer(expenses_file)
        expenses_writer = expenses_writer.writerow([infos['label'], infos['amount'], infos['spender'], infos['involved']])

    print("Expense Added !")
    return True