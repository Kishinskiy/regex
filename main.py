from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv


def read_csv(file_path):
    with open(file_path) as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


def check_name(name):
    ls = re.split("\s", name)
    l = len(ls)
    ll = len(ls[0])
    if l > 0 and ll > 0:
        return ls


def main():
    # pprint(contacts_list)

    print(contacts_list[1])

    # TODO 1: выполните пункты 1-3 ДЗ
    # ваш код

    # print (re.split("\s", contacts_list[1]))

    # # TODO 2: сохраните получившиеся данные в другой файл
    # # код для записи файла в формате CSV
    # with open("phonebook.csv", "w") as f:
    #   datawriter = csv.writer(f, delimiter=',')
    #   # Вместо contacts_list подставьте свой список
    #   datawriter.writerows(contacts_list)


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
    init_phonebook()
    dl = []
    for i in range(1, len(contacts_list)):
        d = []
        line = contacts_list[i][0:3]
        n = []
        for i in range(0, 3):
            if len(line[i]) < 5:
                break
            n.extend(line[i].split(' '))

        first_name = n[0]
        second_name = n[1]
        if len(n) < 3:
            surname = ''
        else:
            surname = n[2]

        name = [first_name, second_name, surname]
        d.extend(name)
        d.extend(contacts_list[i][3:])
        n = re.sub(r'(\d)(\d{3})(\d{3})(\d{2})(\d{2})', r'\1 (\2) \3-\4-\5', d[5])
        d.insert(5, n)
        d.remove(d[6])
        dl.append(d)

    add_phonebook(dl)
