from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding="UTF8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)


def contacts(contact_list):
    number = r"(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})"
    ext_number = r"\s*\(*(доб.)\s*(\d*)\)*\s*"
    name = r"(^([А-я]+)\s([А-я]+)\s([А-я]+)\,\,)|(^([А-я]+)\,([А-я]+)\," \
           r"([А-я]+))|(^([А-я]+)\s([А-я]+)(\,)\,)|(^([А-я]+)\,([А-я]+)\s([А-я]+)\,)"
    line = ','.join(contact_list)
    line = re.sub(name, r"\2\6\14\10,\3\7\11\15,\4\8\16", line)
    line = re.sub(number, r"+7(\2)\3-\4-\5", line)
    line = re.sub(ext_number, r" \1\2", line)
    return line.split(',')


update_contacts_list = []
for contact in contacts_list:
    update_contacts_list.append(contacts(contact))
out_contacts_list = []
contacts_list_len = len(update_contacts_list)
pass_records = []

for i in range(contacts_list_len - 1):
    if i in pass_records:
        continue
    contact = update_contacts_list[i]
    for j in range(i + 1, len(update_contacts_list)):
        if contact[0] == update_contacts_list[j][0] and contact[1] == update_contacts_list[j][1]:
            pass_records.append(j)
            contact = [contact[_] if contact[_] != "" else update_contacts_list[j][_]
                       for _ in range(len(contact))]
    out_contacts_list.append(contact)


with open("phonebook.csv", "w", encoding="utf8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(out_contacts_list)