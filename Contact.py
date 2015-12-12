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
        string = "Name: " + self.name

        if (self.phone):
           string = string + "\n Phone Number: " + self.phone
        return string

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
        return self.name.__contains__(strToMatch) or self.phone.__contains__(strToMatch)

class FriendContact(Contact):
    def __init__(self, olderContact = None):
        if olderContact != None:
            self = olderContact

    def __str__(self):
        string = Contact.__str__(self)
        if (self.homePhone):
           string = string + "\n Home Phone Number: " + self.homePhone
        if (self.email):
           string = string + "\n Personal E-Mail: " + self.email
        return string

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

    def match(self, strToMatch):
        return super().match(strToMatch) or self.email.__contains__(strToMatch) or self.homePhone.__contains__(strToMatch)
    
class ProfessionalContact(Contact):
    def __init__(self, olderContact = None):
        if olderContact != None:
            self = olderContact

    def __str__(self, withSuper = True):
        if (withSuper):
            string = Contact.__str__(self)
        else:
            string = ''
        if (self.workPhone):
           string = string + "\n Work Phone Number: " + self.workPhone
        if (self.workEmail):
           string = string + "\n Work E-Mail: " + self.workEmail
        return string

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
        
    def match(self, strToMatch):
        return super().match(strToMatch) or self.workEmail.__contains__(strToMatch) or self.workPhone.__contains__(strToMatch)

class ProfessionalFriendContact(ProfessionalContact,FriendContact):
    def __init__(self, olderContact = None):
        pass
    def readValues(self):
        super().readValues()
    def match(self, strToMatch):
        return super(ProfessionalFriendContact, self).match(strToMatch)

    def __str__(self):
            return FriendContact.__str__(self) + ProfessionalContact.__str__(self,False)
