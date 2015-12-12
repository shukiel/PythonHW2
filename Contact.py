# Author: Enosh Cohen
#
import re
def confirmPhone(phone):
    if phone == '' or str.isdigit(phone):
        return True
    return False

def confirmEmail(email):
    if email == '' or re.fullmatch(r"\w+@\w+\.\w+",email):
        return True
    return False

class Contact:
    def __init__(self, olderContact=None):
        if olderContact != None:
            self = olderContact
        else:
            name = ''

    def __lt__(self, other):
        return (self.name < other.name)

    def __str__(self):
        return "Name: " + self.name + "/tPhone# :" + self.phone

    def readValues(self):
        while(True):
            self.name = input('Please Enter Contact Name:')
            if self.name not in {'', None}:
                break
            print('Name field can not be empty')
        print(self.name)

        while(True):
            self.phone = input('Please Enter Phone Number:')
            if confirmPhone(self.phone):
                break
            print('phone number may contain only digits')
        print(self.phone)

    def match(self, strToMatch):
        pass #TODO

class FriendContact(Contact):
    def __init__(self, olderContact = None):
        pass

    '''
    def __lt__(self, other):
        return super().__lt__(self, other)
    '''

    def __str__(self):
        return super().__str__() + "\tHome Phone#:" + self.homePhone + "\tPersonal E-Mail: " + self.personalEmail

    def strWithoutName(self):
        return "\tHome Phone#:" + self.homePhone + "\tE-Mail: " + self.personalEmail

    def readValues(self):
        super().readValues()
        while (True):
            self.homePhone = input ('Please Enter Home Phone Number:')
            if confirmPhone(self.homePhone):
                break
            print('Home phone number may contain only digits')
        print(self.homePhone)
        while (True):
            self.email = input ('Please Enter Email:')
            if confirmEmail(self.email):
                break
            print('ileagal eMail. please try again')
        print(self.email)

class ProfessionalContact(Contact):
    def __init__(self, olderContact = None):
        pass

    def __str__(self):
        return super().__str__() + "\tWork Phone#:" + self.workPhone + "\tWork E-Mail: " + self.workEmail

    def readValues(self):
        super().readValues()
        while (True):
            self.workPhone = input ('Please Enter Work Phone Number:')
            if confirmPhone(self.workPhone):
                break
            print('Work phone number may contain only digits')
        print(self.workPhone)

        while (True):
            self.workEmail = input ('Please Enter Work Email:')
            if confirmEmail(self.workEmail):
                break
            print('ileagal eMail. please try again')
        print(self.workEmail)

class ProfessionalFriendContact(ProfessionalContact,FriendContact):
    def __init__(self, olderContact = None):
        pass
    def readValues(self):
        super().readValues()


