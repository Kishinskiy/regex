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


def clean_phone(phone):
    if phone:
        digits = ''.join(re.findall(r'\d+|доб', phone))
        # print(digits)
        regex = r'(?P<country>\d)(?P<code>\d{3})(?P<first>\d{3})?(?P<second>\d{2})(?P<third>\d{2})(доб)?(?P<add>\d+)?'
        match = re.match(regex, digits)

        code = match.group('code')
        first = match.group('first')
        second = match.group('second')
        third = match.group('third')
        add = match.group('add')

        if add:
            return f'+7({code}){first}-{second}-{third} доб.{add}'
        return f'+7({code}){first}-{second}-{third}'

    return ''


if __name__ == '__main__':
    contacts_list = read_csv("phonebook_raw.csv")
    # pprint(contacts_list)
    # pattern = r'[А-Яа-яЁё]+'
    # for i in range(1, len(contacts_list)):
    #     words = contacts_list[i][:3]
    #     res = re.findall(pattern, str(words))
    #     res.extend(contacts_list[i][3:])
    #     print(111, re.sub(r'(\+\d)(\d{3})(\d{3})(\d{2})(\d{2})', r'\1 (\2) \3-\4-\5', res[5]))

    for contact in contacts_list[1:]:
        contact[-2] = clean_phone(contact[-2])
        print(contact[-2])

    pprint(contacts_list)
