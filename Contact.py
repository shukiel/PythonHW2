# Author: Enosh Cohen
#
import re
def confirmPhone(phone):
    if str.isdigit(phone):
        return True
    return False

def confirmEmail(email):
    if re.fullmatch(r"\w+@(\w+\.\w+)+",email):
        return True
    return False
def updateField(oldField,newField):
    if newField == '':
        return oldField
    elif newField in {'x','X'}:
        return ''
    else:
        return newField

class Contact:
    def __init__(self, olderContact=None):
        if olderContact != None:
            self.name = olderContact.name
            if hasattr(olderContact,'cellPhone'):
                self.cellPhone = olderContact.cellPhone
        else:
            self.name = None

    def __lt__(self, other):
        return (str.lower(self.name) < str.lower(other.name))

    def __str__(self):
        string = "Name: " + self.name

        if hasattr(self,'cellPhone'):
           string = string + "\n Cell Phone Number: " + self.cellPhone
        return string

    def readValues(self):
        while(True):
            if self.name == None:
                self.name = input('Name:')
            else:
                tempName = updateField(self.name,input('Name(' + self.name + '):'))
                if tempName == '':
                    print("Name Value Cannot be erased")
                    continue
                self.name = tempName
                break
            if self.name != '':
                break
            self.name = None
            print('Name field can not be empty')

        while(True):
            if hasattr(self,'cellPhone'):
                tempCellPhone = updateField(self.cellPhone,input('Cell Phone Number(' + self.cellPhone + '):'))
                if tempCellPhone == '':
                    del(self.cellPhone)
                    break
            else :
                tempCellPhone = input('Cell Phone Number:')
                if tempCellPhone == '':
                    break
            if confirmPhone(tempCellPhone):
                self.cellPhone = tempCellPhone
                break
            print('Cell phone number may contain only digits')

    def match(self, strToMatch):
        return self.name.__contains__(strToMatch) or self.cellPhone.__contains__(strToMatch)

class FriendContact(Contact):
    def __init__(self, olderContact=None):
        super().__init__(olderContact)
        if hasattr(olderContact,'homePhone'):
            self.homePhone = olderContact.homePhone
        if hasattr(olderContact,'email'):
            self.email = olderContact.email

    def __str__(self):
        string = Contact.__str__(self)
        if hasattr(self,'homePhone'):
           string = string + "\n Home Phone Number: " + self.homePhone
        if hasattr(self,'email'):
           string = string + "\n Personal E-Mail: " + self.email
        return string

    def readValues(self):
        super().readValues()
        while(True):
            if hasattr(self,'homePhone'):
                tempHomePhone = updateField(self.homePhone, input('Home Phone Number:(' +self.homePhone+'):'))
                if tempHomePhone == '':
                    del(self.homePhone)
                    break
            else:
                tempHomePhone = input('Home Phone Number:')
                if tempHomePhone == '':
                    break
            if confirmPhone(tempHomePhone):
                self.homePhone =tempHomePhone
                break
            print('Home phone number may contain only digits')

        while (True):
            if hasattr(self,'email'):
                tempEmail = updateField(self.email, input ('Email(' + self.email + '):') )
                if tempEmail == '':
                    del(self.email)
                    break
            else:
                tempEmail = input('Email:')
                if tempEmail == '':
                    break
            if confirmEmail(tempEmail):
                self.email = tempEmail
                break
            print('ileagal eMail. please try again')

    def match(self, strToMatch):
        return super().match(strToMatch) or self.email.__contains__(strToMatch) or self.homePhone.__contains__(strToMatch)
    
class ProfessionalContact(Contact):
    def __init__(self, olderContact=None):
        super().__init__(olderContact)
        if hasattr(olderContact,'workPhone'):
            self.workPhone = olderContact.workPhone
        if hasattr(olderContact,'workEmail'):
            self.workEmail = olderContact.workEmail

    def __str__(self, withSuper = True):
        if (withSuper):
            string = Contact.__str__(self)
        else:
            string = ''
        if hasattr(self,'workPhone'):
           string = string + "\n Work Phone Number: " + self.workPhone
        if hasattr(self,'workEmail'):
           string = string + "\n Work E-Mail: " + self.workEmail
        return string

    def readValues(self):
        super().readValues()
        while (True):
            if hasattr(self,'workPhone'):
                tempWorkPhone = updateField(self.workPhone, input ('Work Phone Number(' + self.workPhone + '):'))
                if tempWorkPhone == '':
                    del(self.workPhone)
                    break
            else:
                tempWorkPhone = input('Work Phone Number:')
                if tempWorkPhone == '':
                    break
            if confirmPhone(tempWorkPhone):
                self.workPhone = tempWorkPhone
                break
            print('Work phone number may contain only digits')

        while (True):
            if hasattr(self,'workEmail'):
                tempEmail = updateField(self.workEmail, input ('Work Email(' + self.workEmail + '):') )
                if tempEmail == '':
                    del(self.workEmail)
                    break
            else:
                tempEmail = input('Work Email:')
                if tempEmail == '':
                    break
            if confirmEmail(tempEmail):
                self.workEmail = tempEmail
                break
            print('ileagal Email. please try again')
        
    def match(self, strToMatch):
        return super().match(strToMatch) or self.workEmail.__contains__(strToMatch) or self.workPhone.__contains__(strToMatch)

class ProfessionalFriendContact(ProfessionalContact,FriendContact):
    def __init__(self, olderContact=None):
        super().__init__(olderContact)

    def readValues(self):
        super().readValues()

    def match(self, strToMatch):
        return super(ProfessionalFriendContact, self).match(strToMatch)

    def __str__(self):
            return FriendContact.__str__(self) + ProfessionalContact.__str__(self,False)
