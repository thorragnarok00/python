import csv

class Person:
    def __init__(self, id, first_name, middle_name, last_name, birthday, gender, address):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.address = address

    def __str__(self):
        return f"ID: {self.id}\nName: {self.first_name} {self.middle_name} {self.last_name}\nBirthday: {self.birthday}\nGender: {self.gender}\nAddress: {self.address}"

def load_csv(file_path):
    persons = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row if present
        for row in reader:
            id, first_name, middle_name, last_name, birthday, gender, address = row # unpacking
            persons.append(Person(id, first_name, middle_name, last_name, birthday, gender, address))
    return persons

person_list = load_csv("persons.csv")
    
def search_person(search_term):
    search_term = search_term.lower()
    results = 0;
    for person in person_list:
        if (search_term in person.first_name.lower() or search_term in person.middle_name.lower() or search_term in person.last_name.lower()):
            print(f"\n{person}")
            results += 1
    print(f"\n{results} results found in 1000")

if __name__ == "__main__":
    search_term = input("Enter search term: ")
    search_person(search_term)