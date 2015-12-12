__author__ = 'Zukis87'
import re
import Contact

class PhoneBook:
    select = 0
    contacts = []

    chooseContactType = 'Should this contact be Simple (S), Friend (F), Professional (P) or Both (B)?'
    def add_contact(self):
        print("Add New Contact")

        while(True):
            choose = input (self.chooseContactType)
            if choose in {'S', 's', 'F', 'f', 'P', 'p', 'B', 'b'} :
                break
            print('Wrong Selection Choose Again!')

        if choose in {'S','s'}:
            c = Contact.Contact()
        elif choose in {'f','F'}:
            c = Contact.FriendContact()
        elif choose in {'p','P'}:
            c = Contact.ProfessionalContact()
        elif choose in {'b','B'}:
           c = Contact.ProfessionalFriendContact()
        c.readValues()
        self.contacts.append(c)
        self.contacts.sort()

    def show_contacts(self):
        print('Show all')
        for c in self.contacts:
            print('Contact #',self.contacts.index(c) + 1, ":\n ", c, '\n', sep='')

    def edit_contact(self):
        print('Edit:')
        while(True):
            indexToEdit = input('Enter a valid number of the contact you wish to edit:')
            if str.isdigit(indexToEdit):
                indexToEdit = int(indexToEdit)
                if indexToEdit > 0:
                    indexToEdit= indexToEdit -1
                    if len(self.contacts) > indexToEdit:
                        break

            print("Error. Please ",end= '')
        c = self.contacts[indexToEdit]
        choose = input (self.chooseContactType)
        if choose in {'S','s'}:
            c = Contact.Contact(c)
        elif choose in {'f','F'}:
            c = Contact.FriendContact(c)
        elif choose in {'p','P'}:
            c = Contact.ProfessionalContact(c)
        elif choose in {'b','B'}:
           c = Contact.ProfessionalFriendContact(c)
        print('For the following fields click enter if there\'s no change, '
              'a new value if you want to replace the field,'
              ' or x if you want to delete the field (the name field cannot be deleted).')
        c.readValues()

    def find_contact(self):
        print ('Find')

    def delete_contact(self):
        print ('Delete')

    def start(self):
        while (True):
            print ('What would you like to do?')
            print ('1 - Add a new contact')
            print ('2 - Show all contacts')
            print ('3 - Edit a contact')
            print ('4 - Find a contact')
            print ('5 - Delete a contact')
            print ('6 - Exit')
            print ('-->')

            wrongInput = 'Wrong Selection Input DUDE!!!'
            select = input ()
            try:
                select = int(select)
            except ValueError:
                print (wrongInput)
                continue

            if (select == 1):
                self.add_contact(self)
            elif (select == 2):
                self.show_contacts(self)
            elif (select == 3):
                self.edit_contact(self)
            elif (select == 4):
                self.find_contact(self)
            elif (select == 5):
                self.delete_contact(self)
            elif (select == 6):
                print ('Thank you, Come again !')
                break
            else:
                print (wrongInput)

pb = (PhoneBook)
pb.start(pb)