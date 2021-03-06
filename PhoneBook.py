#By Enosh Cohen & Zuriel Sarusi
#    301752754     301272498

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
        if self.contacts.__len__() == 0:
            print("Contact list is empty")
            return
        while(True):
            indexToEdit = input('Enter a valid number of the contact you wish to edit:')
            if str.isdigit(indexToEdit):
                indexToEdit = int(indexToEdit)
                if indexToEdit in range(1, len(self.contacts)+1):
                    indexToEdit= indexToEdit -1
                    break
            print("Error. Please ",end= '')
        c = self.contacts[indexToEdit]
        choose = input (self.chooseContactType)
        if choose in {'S','s'}:
            d = Contact.Contact(c)
        elif choose in {'f','F'}:
            d = Contact.FriendContact(c)
        elif choose in {'p','P'}:
            d = Contact.ProfessionalContact(c)
        elif choose in {'b','B'}:
           d = Contact.ProfessionalFriendContact(c)
        print('For the following fields click enter if there\'s no change, '
              'a new value if you want to replace the field,'
              ' or x if you want to delete the field (the name field cannot be deleted).')
        d.readValues()
        self.contacts.append(d)
        self.contacts.remove(c)
        self.contacts.sort()

    def find_contact(self):
        strToMatch = input('Type contact details (name, phone, email):')
        for c in self.contacts:
            if (c.match(strToMatch)):
                print('Contact #',self.contacts.index(c) + 1, ":\n ", c, '\n', sep='')

    def delete_contact(self):
        if self.contacts.__len__() == 0:
            print("Contact list is empty")
            return

        while(True):
            deleteSelection =input ("Enter a valid number of the contact you wish to delete or 0 to abort: ")
            if str.isdigit(deleteSelection):
                deleteSelection = int(deleteSelection)
                if deleteSelection == 0:
                    return
                if deleteSelection in range(1, len(self.contacts)+1):
                    break
        delName = self.contacts[deleteSelection-1].name
        self.contacts.remove(self.contacts[deleteSelection-1])
        print ('\n\n\n', delName, ' Deleted! \n\n\n')


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