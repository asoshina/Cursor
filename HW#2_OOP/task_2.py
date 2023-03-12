"""
Сlass Profile:
Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
Override a printable string representation of Profile class and return: list of the params mentioned above

"""


class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __repr__(self):
        lst = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday, self.age, self.sex]
        return ', '.join(str(elem) for elem in lst)


person = Profile('Ted', 'Bundy', '+380681234567', 'address string', 'test@gmail.com', '12-02-1999', 24, 'Male')
print(person)
