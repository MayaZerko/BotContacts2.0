from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def get_info(self):
        phones_info = ''

        for phone in self.phones:
            phones_info += f'{phone.value}, '

        return f'{self.name.value} : {phones_info[:-2]}'

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def clear_phones(self):
        self.phones = []



class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        # if record.name.value in self.data:
        #     record = self.data[record.name.value]

    def get_all_record(self):
        return self.data

    def has_record(self, name):
        return bool(self.data.get(name))

    def get_record(self, name) -> Record:
        return self.data.get(name)
