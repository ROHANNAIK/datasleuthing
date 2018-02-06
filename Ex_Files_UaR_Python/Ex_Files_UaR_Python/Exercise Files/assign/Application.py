# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:14:34 2018

@author: Rohan
"""
import csv
import os

phones = [['Rohan Naik', '(857) 269-0481'],
           ['Sonali Naik','(123) 456-7890']]
name_pos = 0
phone_pos = 1
phone_header =['Name', 'Phone Number']

def proper_menu_choice(which):
    if not which.isdigit():
        print("'"+ which + " 'needs to be a number of a phone!")
        return False
    which = int(which)
    if which < 1 or which > len(phones):
        print("'"+ which + " 'needs to be a number of a phone in range!")
        return False
    return True
        
def delete_phone(which):
    if not proper_menu_choice(which):
        return
    which = int(which)
    
    del phones[which - 1]
    print("Deleted #", which)
          
    #print("Deleting")
    
def show_phones():
    print("Showing Phones.")
    show_phone(phone_header,"")
    index = 1
    for phone in phones:
        show_phone(phone, index)
        index = index + 1
    print()
    
def show_phone(phone, index):
    outputstr = "{0:>3} {1:<20} {2:>16}"
    print(outputstr.format(index, phone[name_pos], phone[phone_pos]))
    

def edit_phone(which):
    if not proper_menu_choice(which):
        return
    which = int(which)
    phone = phones[which - 1]
    print("Enter the data for new phone. Press <enter> otherwise.")
    print(phone[name_pos])
    new_name = input("Enter the name to change: ")
    if new_name == "":
        new_name = phone[name_pos]
        
    print(phone[phone_pos])
    new_phone = input("Enter the phone to change: ")
    if new_phone == "":
        new_phone = phone[phone_pos]
    
    phone = [new_name, new_phone]
    phones[which-1] =   phone

def new_phone():
    print("Enter the name and the phone number: ")
    newname = input("Enter the name: ")
    newphone = input("Enter the phone number: ")
    phone = [newname, newphone]
    phones.append(phone)
    print("Adding new phone")
    
    
def save_phone_list():
    
    file = open("newmyphones.csv",'w',newline='')
    for item in phones:
        csv.writer(file).writerow(item)
    file.close()
    print("saving list")
    
def load_phone_list():
    if os.access("myphones.csv",os.F_OK):
        f = open("myphones.csv")
        for row in csv.reader(f):
            phones.append(row)
        f.close()
        
    print("loading list")
    
def menuchoice():
    print("Choose from the below options")
    print(" a) show \n b) delete \n c) edit \n d) new \n e) exit")
    c = input("Enter your choice:")
    if c.lower() in ['a','b','c','d','e']:
        return c.lower()
    else:
        print("Please choose from the options.")
        return None
    
def menuloop():
    
    load_phone_list()
    
    while True:
        choice = menuchoice()
        if choice == None:
            continue
        if choice == "e":
            print("Exiting.....")
            break
        elif choice == "a":
            show_phones()
        elif choice == "b":
            which = input("Which item do you want to delete?")
            print("Deleting record #", which)
            delete_phone(which)
        elif choice == "c":
            which = input("Which item do you want to edit?")
            print("Editing record #", which)
            edit_phone(which)
        elif choice == "d":
            new_phone()
        else:
            print("Invalid Choice.")
            
    save_phone_list()
        
if  __name__ == '__main__':
    menuloop()
      
