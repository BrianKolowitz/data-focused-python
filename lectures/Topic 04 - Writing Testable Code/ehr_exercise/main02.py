
def is_new_patient():
    response = input("Have you been here before? Type y or n. ")
    if response[0].lower().strip() == "n":
        return True
    return False


def collect_patient_name():
    name = input("What is your name? ")
    return name


def collect_patient_date_of_birth():
    dateOfBirth = input("What is your birth date? ")
    return dateOfBirth


def collect_patient_email():
    email = input("What is your email? ")
    return email


def collect_patient_information():
    return (collect_patient_name(),
            collect_patient_date_of_birth(),
            collect_patient_email())


if __name__ == "__main__":
    nextPatientId = 1
    db = {}

    running = True
    while running:
        print("Welcome to our Hospital")
        currentPatient = None
        newPatient = is_new_patient()
        if newPatient:
            # register and add to the database
            print("We're so happy you chose us!")
            name, dateOfBirth, email = collect_patient_information()
            currentPatient = {
                "patientId": nextPatientId,
                "name": name,
                "dateOfBirth": dateOfBirth,
                "email": email
            }
            db[currentPatient['patientId']] = currentPatient
            nextPatientId += 1
        else:
            # search and find in the database
            print("Welcome back!")
            name, dateOfBirth, email = collect_patient_information()
            for (patientId, p) in db:
                if p['name'] == name and p['dateOfBirth'] == dateOfBirth and p['email'] == email:
                    currentPatient = p
                    break

        print(currentPatient)
        print(db)
        print(len(db.keys()))
        print(db.keys())

        response = input("Would you like to quit? ")
        if response[0].lower().strip() == "y":
            running = False
