

# 1. Register a new patient
# 2. Search for a patient
nextPatientId = 1
db = {}

running = True
while running:
    print("Welcome to our Hospital")
    response = input("Have you been here before? ")
    if response[0].lower().strip() =="n" :
        newPatient = True
    else:
        newPatient = False

    currentPatient = None

    if newPatient:
        # register and add to the database
        print("We're so happy you chose us!")
        patientName = input("What is your name? ")
        dateOfBirth = input("What is your birth date? ")
        email = input("What is your email? ")
        currentPatient = {
            "patientId": nextPatientId,
            "name": patientName,
            "dateOfBirth": dateOfBirth,
            "email": email
        }
        db[currentPatient['patientId']] = currentPatient
        nextPatientId += 1
    else:
        # search and find in the database
        print("Welcome back!")
        patientName = input("What is your name? ")
        dateOfBirth = input("What is your birth date? ")
        email = input("What is your email? ")
        for (patientId, p) in db:
            if p['name'] == patientName and p['dateOfBirth'] == dateOfBirth and p['email'] == email:
                currentPatient = p
                break

    print(currentPatient)
    print(db)
    print(len(db.keys()))
    print(db.keys())

    response = input("Would you like to quit? ")
    if response[0].lower().strip() == "y":
        running = False

