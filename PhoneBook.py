__author__ = 'Zukis87'
import re
class PhoneBook:
    select = 0
    def  add_contact(self):
        while (True):
            addChoose = input ('Should this contact be Simple (S), Friend (F), Professional (P) or Both (B)?')
            if addChoose in {'S', 'F', 'P', 'B'}:
                break
            else:
                print ('Wrong Selection Choose Again!')

        name = input ('Please Enter Contact Name:')
        phone = input ('Please Enter Phone#:')

        if (addChoose == 'F'):
            while (True):
                homePhone = input ('Please Enter HomePhone#:')
                if (re.match(r"%d+", homePhone)!=None):
                    break

            while (True):
                eMail = input ('Please Enter eMail:')
                if (re.match (r"/w+@/w/+./w+")!=None):
                    break

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

            select = input ()
            try:
                select = int(select)
            except ValueError:
                print ('Wrong Selection Input DUDE!!!')
                continue
                
            if (select == 1):
                self.add_contact()
            elif (select == 2):
                print ('Show all')
            elif (select == 3):
                print ('Edit')
            elif (select == 4):
                print ('Find')
            elif (select == 5):
                print ('Delete')
            elif (select == 6):
                print ('Thank you, Come again !')
                break
            else:
             print ('Wrong Selection Input DUDE!!!')