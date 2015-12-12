__author__ = 'Zukis87'
import re

class PhoneBook:

    select = 0
    chooseContactType = 'Should this contact be Simple (S), Friend (F), Professional (P) or Both (B)?'
    def add_contact(self):
        print("Add New Contact")

        while(True):
            choose = input (self.chooseContactType)
            if choose in {'S', 's', 'F', 'f', 'P', 'p', 'B', 'b'} :
                break
            print ('Wrong Selection Choose Again!')

        while(True):
            name = input('Please Enter Contact Name:')
            if name not in {'', None}:
                break
            print('Name field can not be empty')
        print(name)
        while(True):
            phone = input('Please Enter Phone Number:')
            if self.confirmPhone(self,phone):
                break
            print('phone number may contain only digits')
        print(phone)

        if choose in {'f','F'}:
            while (True):
                homePhone = input ('Please Enter Home Phone Number:')
                if self.confirmPhone(self,homePhone):
                    break
                print('Home phone number may contain only digits')
            print(homePhone)
            while (True):
                email = input ('Please Enter Email:')
                if self.confirmEmail(self,email):
                    break
                print('ileagal eMail. please try again')
            print(email)

        elif choose in {'p','P'}:
            while (True):
                workPhone = input ('Please Enter Work Phone Number:')
                if self.confirmPhone(self,workPhone):
                    break
                print('Work phone number may contain only digits')
            print(workPhone)

            while (True):
                workEmail = input ('Please Enter eMail:')
                if self.confirmEmail(self,workEmail):
                    break
                print('ileagal eMail. please try again')
            print(workEmail)
        elif choose in {'b','B'}:
            print('')

    def confirmPhone(self,phone):
        if str.isdigit(phone):
            return True
        return False
    def confirmEmail(self,email):
        if re.fullmatch(r"\w+@\w+\.\w+",email):
            return True
        return False

    def show_contacts(self):
        print('Show all')

    def edit_contact(self):
        print('Edit:')
        print('Enter a valid number of the contact you wish to edit:')
        choose = input (self.chooseContactType)
        print('For the following fields click enter if there\'s no change, '
              'a new value if you want to replace the field,'
              ' or x if you want to delete the field (the name field cannot be deleted).')

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
                self.show_contacts()
            elif (select == 3):
                self.edit_contact()
            elif (select == 4):
                self.find_contact()
            elif (select == 5):
                self.delete_contact()
            elif (select == 6):
                print ('Thank you, Come again !')
                break
            else:
                print (wrongInput)

pb = (PhoneBook)
pb.start(pb)