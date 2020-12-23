import csv
def add_user(first_name, last_name):
    with open("users.csv","a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first_name,last_name])

#add_user("Sare","Taban")
def get_users():
    with open("users.csv") as file:
        csv_reader = csv.DictReader(file)
        for user in csv_reader:
            print(f'{user["FirstName"]} {user["LastName"]}')

#get_users()

def find_user(first_name,last_name):
    with open("users.csv")as file:
        csv_reader = csv.reader(file)
        for (index,row) in enumerate(csv_reader):
            if(row[0]== first_name) and (row[1]==last_name):
                return index
            return -1


#print(find_user("Sare","Taban"))

