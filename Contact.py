# Author: Enosh Cohen
#



class Contact:
    name = ""

    def __init__(self, olderContact=None):
        if olderContact != None:
            self = olderContact
        else:
            self.readValues()

    def __lt__(self, other):
        return (self.name < other.name)

    def __str__(self):
        return "Name: " + self.name + "/tPhone# :" + self.phone

    def readValues(self):
        pass #TODO

    def match(self, strToMatch):
        pass #TODO


class FriendContact(Contact):
    def __init__(self):
        pass

    '''
    def __lt__(self, other):
        return super().__lt__(self, other)
    '''

    def __str__(self):
        return super().__str__() + "\tHome Phone#:" + self.homePhone + "\tPersonal E-Mail: " + self.personalEmail

    def strWithoutName(self):
        return "\tHome Phone#:" + self.homePhone + "\tE-Mail: " + self.personalEmail


class ProfessionalContact(Contact):
    def __init__(self, olderContact):
        pass

    def __str__(self):
        return super().__str__() + "\tWork Phone#:" + self.workPhone + "\tWork E-Mail: " + self.workEmail


class ProfessionalFriendContact(FriendContact, ProfessionalContact):
    pass
