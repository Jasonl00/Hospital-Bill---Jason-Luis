#Jason Luis 
#Professor Ghaforyfard 
#April 14, 2024 
#Write a program that computes and displays the charges for a patient's hospital stay. 

#Variables/Inputs 

num_of_days = ""

rate = ""

daily_rate = ""

hospital_services = ""

med_charges = ""


from ast import Num
from sqlite3 import enable_shared_cache
from statistics import median


    
#Inputs
patient = input("Was the patient admitted as an in-patient? Enter Y or N: ").upper()

while True:
    
    if patient == "Y":
        num_of_days = int(input("\nHow many days was the patient in the hospital for? ")) 
        if num_of_days <= 0:
             print("\nInvalid, Try Again.")
             num_of_days = int(input("\nHow many days was the patient in the hospital for? ")) 

        rate = float(input("\nWhat is the rate per day at the hospital?: $")) 
        if rate <= 0:
            print("\nInvalid input, please try again.")
            rate = float(input("\nWhat is the rate per day at the hospital?: $")) 

        daily_rate = float(num_of_days * rate) 
        print("\nThe Daily Rate is $", daily_rate)

        hospital_services = float(input("\nEnter the charges of the Hospital used for the patient (lab test, etc.): $"))
        if hospital_services <= 0:
            print("\nInvalid input, please try again.")
            hospital_services = float(input("\nEnter the charges of the Hospital used for the patient (lab test, etc.): $"))

        print("\nThe Hospital Services are $", hospital_services)
        
        med_charges = float(input("\nWhat are the charges of the medication used for the patient?: $"))
        if med_charges <= 0:
           print("\nInvalid input, please try again.")
           med_charges = float(input("\nWhat are the charges of the medication used for the patient?: $"))

        print("\nThe Hosptial Medication Charges are $", med_charges) 
        
        #total charge
        total_charge = float(daily_rate + hospital_services + med_charges)
        print("\nThe Total Hospital Bill is $",total_charge)
        break

    elif patient == "N": 
        hospital_services = float(input("\nEnter the charges of the Hospital used for the patient (lab test, etc.): $"))
        if hospital_services <= 0:
            print("\nInvalid input, please try again.")
            hospital_services = float(input("\nEnter the charges of the Hospital used for the patient (lab test, etc.): $"))

        print("\nThe Hospital Services are $", hospital_services)
        
        med_charges = float(input("\nWhat are the charges of the medication used for the patient?: $"))
        if med_charges <= 0:
            print("\nInvalid input, please try again.")
            med_charges = float(input("\nWhat are the charges of the medication used for the patient?: $"))

        print("\nThe Hosptial Medication Charges are $", med_charges) 

        #total charge
        total_charge = float(hospital_services + med_charges)
        print("\nThe Total Hospital Bill is $",total_charge)
        break

    else:
            print("\nInvalid input. Please try again.")
            patient = input("\nWas the patient admitted as an in-patient? Enter Y or N: ").upper()
            continue