# ============================================================
# PROG211 - OBJECT-ORIENTED PROGRAMMING 1
# ASSIGNMENT: PATIENT RECORD MANAGEMENT SYSTEM
# DOMAIN: HEALTH
# ===========================================================
# This program demonstrates:
# 1. Classes and Objects
# 2. Attributes
# 3. Instance Methods
# 4. Class Method
# 5. Lists as Data Structures
# 6. Object Interaction
# 7. Adding and Displaying Records
# 8. Searching and Updating Records


# PATIENT CLASS

class Patient:
    total_patients = 0
    def __init__(self, patient_id, name, age, gender, condition, blood_group):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        self.blood_group = blood_group
        self.doctor = None

        Patient.total_patients += 1

# Display Patient Information

    def display_info(self):
        print("\n----- PATIENT INFORMATION -----")
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Condition:", self.condition)
        print("Blood Group:", self.blood_group)
        if self.doctor:
            print("Assigned Doctor:", self.doctor.name)
        else:
            print("Assigned Doctor: None")

# Update Patient Record

    def update_record(self, condition):
        self.condition = condition
        print("Patient record updated successfully.")

# Assign Doctor

    def assign_doctor(self, doctor):
        self.doctor = doctor
        print("Doctor assigned successfully.")

    # CLASS METHOD: Show Total Patients

    @classmethod
    def show_total_patients(cls):
        print("\nTotal registered patients:", cls.total_patients)

# DOCTOR CLASS

class Doctor:
    def __init__(self, doctor_id, name, specialization, department):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.department = department

        self.patients = []


# Display Doctor Information

    def display_info(self):
        print("\n----- DOCTOR INFORMATION -----")
        print("Doctor ID:", self.doctor_id)
        print("Name:", self.name)
        print("Specialization:", self.specialization)
        print("Department:", self.department)

# INSTANCE METHOD: Add Patient to Doctor

    def add_patient(self, patient):
        if patient not in self.patients:
            self.patients.append(patient)

    # INSTANCE METHOD: Display Doctor's Patients

    def display_patients(self):
        print("\n----- ASSIGNED PATIENTS -----")
        if len(self.patients) == 0:
            print("No patients assigned.")
        else:
            for patient in self.patients:
                print(patient.patient_id, "-", patient.name)

# ADD PATIENT FUNCTION

def add_patient(patients):
    print("\n" + "=" * 50)
    print("ADD NEW PATIENT")
    print("=" * 50)

# Get patient ID
    patient_id = input("Enter Patient ID: ").strip()

# Check if patient ID already exists
    for patient in patients:
        if patient.patient_id == patient_id:
            print("Error: A patient with this ID already exists.")
            return

# Get patient information
    name = input("Enter Patient Name: ").strip()
    while True:
        try:
            age = int(input("Enter Age: "))
            if age < 0:
                print("Age cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for age.")
    gender = input("Enter Gender: ").strip()
    condition = input("Enter Medical Condition: ").strip()
    blood_group = input("Enter Blood Group: ").strip()

# Patient object

    patient = Patient(patient_id, name, age, gender, condition, blood_group)

# Add Patient object to the patients list

    patients.append(patient)
    print("\nPatient added successfully!")

# DISPLAY ALL PATIENTS FUNCTION

def display_patients(patients):
    print("\n" + "=" * 50)
    print("ALL PATIENTS")
    print("=" * 50)

# Check if there are no patients
    if len(patients) == 0:
        print("No patients registered.")
        return
    for patient in patients:
        patient.display_info()

# SEARCH PATIENT FUNCTION

def search_patient(patients):
    print("\n" + "=" * 50)
    print("SEARCH PATIENT")
    print("=" * 50)
    patient_id = input("Enter Patient ID: ").strip()

# Search through the patient list
    for patient in patients:
        if patient.patient_id == patient_id:
            print("\nPatient found!")
            patient.display_info()
            return
    print("\nPatient not found.")


# UPDATE PATIENT FUNCTION

def update_patient(patients):
    print("\n" + "=" * 50)
    print("UPDATE PATIENT RECORD")
    print("=" * 50)
    patient_id = input("Enter Patient ID: ").strip()

# Search for patient
    for patient in patients:
        if patient.patient_id == patient_id:
            print("\nCurrent patient information:")
            patient.display_info()

# Get new condition
            new_condition = input("\nEnter New Medical Condition: ").strip()
            patient.update_record(new_condition)
            return
    print("\nPatient not found.")

# ADD DOCTOR FUNCTION

def add_doctor(doctors):
    print("\n" + "=" * 50)
    print("ADD NEW DOCTOR")
    print("=" * 50)

# Get Doctor ID

    doctor_id = input("Enter Doctor ID: ").strip()
    for doctor in doctors:
        if doctor.doctor_id == doctor_id:
            print("Error: A doctor with this ID already exists.")
            return

# Get doctor information

    name = input("Enter Doctor Name: ").strip()
    specialization = input("Enter Specialization: " ).strip()
    department = input( "Enter Department: " ).strip()

# Doctor object

    doctor = Doctor(doctor_id, name, specialization, department )

# Add Doctor object to doctors list

    doctors.append(doctor)
    print("\nDoctor added successfully!")

# DISPLAY ALL DOCTORS FUNCTION
def display_doctors(doctors):
    print("\n" + "=" * 50)
    print("ALL DOCTORS")
    print("=" * 50)

# Check if there are no doctors

    if len(doctors) == 0:
        print("No doctors registered.")
        return

# Display every doctor

    for doctor in doctors:
        doctor.display_info()

# ASSIGN DOCTOR TO PATIENT

def assign_doctor_to_patient(patients, doctors):
    print("\n" + "=" * 50)
    print("ASSIGN DOCTOR TO PATIENT")
    print("=" * 50)
    patient_id = input("Enter Patient ID: ").strip()
    doctor_id = input("Enter Doctor ID: ").strip()
    selected_patient = None
    selected_doctor = None

# Find Patient

    for patient in patients:
        if patient.patient_id == patient_id:
            selected_patient = patient
            break

# Find Doctor

    for doctor in doctors:
        if doctor.doctor_id == doctor_id:
            selected_doctor = doctor
            break

# Check if Patient exists

    if selected_patient is None:
        print("\nPatient not found.")
        return

# Check if Doctor exists

    if selected_doctor is None:
        print("\nDoctor not found.")
        return
    selected_patient.assign_doctor(selected_doctor)

# Add Patient to Doctor's patient list

    selected_doctor.add_patient(selected_patient)
    print(f"{selected_doctor.name} has been assigned "f"to {selected_patient.name}." )

# DISPLAY DOCTOR'S PATIENTS

def display_doctor_patients(doctors):
    print("\n" + "=" * 50)
    print("DISPLAY DOCTOR'S PATIENTS")
    print("=" * 50)

# Check if there are no doctors

    if len(doctors) == 0:
        print("\nNo doctors registered.")
        return

# Ask for Doctor ID

    doctor_id = input("Enter Doctor ID: ").strip()
    selected_doctor = None

# Search for doctor

    for doctor in doctors:
        if doctor.doctor_id == doctor_id:
            selected_doctor = doctor
            break

# Check if doctor exist

    if selected_doctor is None:
        print("\nDoctor not found.")
        return

# Display patients assigned to doctor

    print("\nDoctor:", selected_doctor.name)
    selected_doctor.display_patients()

# MAIN MENU

def main_menu():

# DATA STRUCTURES

# List for storing multiple Patient objects
    patients = []

# List for storing multiple Doctor objects
    doctors = []

# PROGRAM LOOP

    while True:
        print("\n")
        print("=" * 60)
        print("********** PATIENT RECORD MANAGEMENT SYSTEM ********" )
        print("=" * 60)
        print("1. Add Patient")
        print("2. Display All Patients")
        print("3. Search Patient")
        print("4. Update Patient Record")
        print("5. Add Doctor")
        print("6. Display Doctors")
        print("7. Assign Doctor to Patient")
        print("8. Show Total Patients")
        print("9. Display Doctor's Patients")
        print("10. Exit")
        print("=" * 60)

# Ask user for menu choice

        choice = input("Enter your choice: " ).strip()
        if choice == "1":
            add_patient(patients)

# DISPLAY ALL PATIENTS
        elif choice == "2":
            display_patients(patients)
        elif choice == "3":
            search_patient(patients)
        elif choice == "4":
            update_patient(patients)
        elif choice == "5":
            add_doctor(doctors)
        elif choice == "6":
            display_doctors(doctors)
        elif choice == "7":
            assign_doctor_to_patient(patients, doctors)
        elif choice == "8":
            Patient.show_total_patients()
        elif choice == "9":
            display_doctor_patients(doctors)
        elif choice == "10":
            print("\nThank you for using the " "Patient Record Management System.")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice.")
            print( "Please select a number from 1 to 10." )

main_menu()