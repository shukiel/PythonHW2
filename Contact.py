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
def updateField(oldField,newField):
    if newField == '':
        return oldField
    elif newField == 'x':
        return ''
    else:
        return newField

class Contact:
    def __init__(self, olderContact=None):
        if olderContact != None:
            self.name = olderContact.name
            self.cellPhone = olderContact.cellPhone
        else:
            self.name = ''

    def __lt__(self, other):
        return (self.name < other.name)

    def __str__(self):
        string = "Name: " + self.name

        if self.cellPhone:
           string = string + "\n Phone Number: " + self.cellPhone
        return string

    def readValues(self):
        while(True):
            if self.name == '':
                self.name = input('Name:')
            else:
                nameStr = 'Name(' + self.name + '):'
                self.name = updateField(self.name,input(nameStr))
            if self.name not in {''}:
                    break
            print('Name field can not be empty')

        while(True):
            if hasattr(self,'cellPhone'):
                cellStr = 'Cell Phone Number(' + self.cellPhone + '):'
                self.cellPhone = updateField(self.cellPhone,input(cellStr))
            else :
                self.cellPhone = input('Cell Phone Number:')
            if confirmPhone(self.cellPhone):
                break
            print('phone number may contain only digits')
        print(self.cellPhone)

    def match(self, strToMatch):
        pass #TODO

class FriendContact(Contact):
    def __init__(self, olderContact = None):
        pass

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
            if hasattr(self,'homePhone'):
                self.homePhone = updateField(self.homePhone, input('Home Phone Number:(',self.homePhone,'):'))
            else:
                self.homePhone = input ('Home Phone Number:')
            if confirmPhone(self.homePhone):
                break
            print('Home phone number may contain only digits')

        while (True):
            if hasattr(self,'email'):
                self.email = updateField(self.email, input ('Please Enter Email(',self.email,'):') )
            else:
                self.email = input ('Please Enter Email:')
            if confirmEmail(self.email):
                break
            print('ileagal eMail. please try again')
        print(self.email)

class ProfessionalContact(Contact):
    def __init__(self, olderContact = None):
        pass

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
            if hasattr(self,'workPhone'):
                self.workPhone = updateField(self.workPhone, input ('Work Phone Number(',self.workPhone,'):'))
            else:
                self.workPhone = input ('Work Phone Number:')
            if confirmPhone(self.workPhone):
                break
            print('Work phone number may contain only digits')
        print(self.workPhone)

        while (True):
            if hasattr(self,'workEmail'):
                self.workEmail = updateField(self.workEmail, input ('Work Email(',self.workEmail,'):'))
            else:
                self.workEmail = input ('Work Email:')
            if confirmEmail(self.workEmail):
                break
            print('ileagal eMail. please try again')
        print(self.workEmail)

class ProfessionalFriendContact(ProfessionalContact,FriendContact):
    def __init__(self, olderContact = None):
        pass
    def readValues(self):
        super().readValues()

    def __str__(self):
            return FriendContact.__str__(self) + ProfessionalContact.__str__(self,False)
