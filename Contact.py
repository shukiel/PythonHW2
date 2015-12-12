# Author: Enosh Cohen
#



class Contact:
    name = ""

    def __init__(self, olderContact = None):
        if olderContact != None:
            self = olderContact
        else:
            self.readValues()

    def __lt__(self, other):
        return (self.name < other.name)

    def __str__(self):
        return "Name: " + self.name + "/tPhone# :" + self.phone

    def readValues(self):


    def match(self, strToMatch):
        pass


class FriendContact(Contact):
    homePhone = -1
    personalEmail = ""

    def __init__(self):
        pass


class ProfessionalContact(Contact):
    pass


class ProfessionalFriendContact(FriendContact, ProfessionalContact):
    pass
