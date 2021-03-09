from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv


def read_csv(file_path):
    with open(file_path) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


def init_phonebook():
    # lastname, firstname, surname, organization, position, phone, email
    with open("phonebook.csv", "w") as f:
        f.write('lastname,firstname,surname,organization,position,phone,email\n')


def add_phonebook(d):
    with open("phonebook.csv", "a") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(d)


if __name__ == '__main__':
    contacts_list = read_csv("phonebook_raw.csv")
    pattern = r'[А-Яа-яЁё]+'
    for i in range(1, len(contacts_list)):
        words = contacts_list[i][:3]
        res = re.findall(pattern, str(words))
        res.extend(contacts_list[i][3:])
        print(res)
