import os
import csv
import time

subjects = [{}]
subject_info = []
grades = [1, 2, 3, 4, 5]
total_avg = 0


def filterSubject(subject_name):
    return f"{subject_name[0].upper()}{subject_name[1:].lower()}"


def add_subject():
    subject_name = input("Tantárgy neve(Mégsem: ENTER): ")
    if len(subject_name) == 0:
        return add_subject()
    else:
        subjects[0][filterSubject(subject_name)] = []
        subject_info.append(filterSubject(subject_name))
        return f"Sikeresen hozzáadva: {filterSubject(subject_name)}"


def remove_subject():
    ossz_tantargy = ""

    for subject in subjects[0]:
        ossz_tantargy = f"{ossz_tantargy}{subject}\n\t"

    subject_choice = input(f"Tantárgy:{ossz_tantargy}\nMégsem: ENTER\n")
    if len(subject_choice) == 0:
        return "Tantárgy törlése befejezve"

    subject_choice = filterSubject(subject_choice)

    if subject_choice not in subjects[0].keys():
        return remove_subject()

    isUserSure = input("Biztos benne? Igen/Nem\n")
    isUserSure = filterSubject(isUserSure)
    if isUserSure == 'Igen':
        del subjects[0][subject_choice]
    else:
        return "Tantárgy törlése befejezve"


def add_grade():
    ossz_tantargy = ""

    for subject in subjects[0]:
        ossz_tantargy = f"{ossz_tantargy}{subject}\n\t"

    subject_choice = input(f"Tantárgy:{ossz_tantargy}")
    subject_choice = filterSubject(subject_choice)

    if subject_choice not in subjects[0].keys():
        return add_grade()

    grade = int(input("Jegy: "))

    if grade not in grades:
        return add_grade()

    weight = int(input("Jegy súlya: "))
    weight = weight/100

    subjects[0][subject_choice].append([grade, weight])

    return "jegy sikeresen hozzáadva."


def remove_grade():
    ossz_tantargy = ""

    for subject in subjects[0]:
        ossz_tantargy = f"{ossz_tantargy}{subject}\n\t"

    subject_choice = input(f"Tantárgy:{ossz_tantargy}")
    subject_choice = filterSubject(subject_choice)

    if (subject_choice not in subjects[0].keys()):
        return remove_grade()

    gradeIndex = 1
    gradeChoices = ""
    for grade in subjects[0][subject_choice]:
        gradeChoices = f"{gradeChoices}{gradeIndex}:{grade[0]}"
    print(gradeChoices)
    gradeChoice = int(input("Jegy törlése: "))

    if gradeChoice < 1 or gradeChoice > gradeIndex:
        return remove_grade()
    del subjects[0][subject_choice][gradeIndex-1]
    return "Sikeresen kitörölte a jegyet."


def saveExit():
    for subject in subjects[0]:
        for gradeInfo in subjects[0][subject]:
            subjects[0][subject][subjects[0][subject].index(gradeInfo)] = gradeInfo[0]
    with open("mentettjegyek.csv", 'w') as file:
        writer = csv.DictWriter(file, fieldnames=subject_info)
        writer.writeheader()
        writer.writerows(subjects)
        time.sleep(0.5)
    return "sikeresen mentett. Kilépés."


while True:
    if len(subjects[0]) == 0:
        operation = int(input(
            "Válasszon egy műveletet:1)Tantárgy megadása\n\t\t\t2)Kilépés\n"))
        if operation == 1:
            print(add_subject())
        elif operation == 2:
            break
    else:

        for k in subjects[0]:
            if len(subjects[0][k]) != 0:
                grades_output = ""
                gradeTotal = 0
                toDivide = 0
                for gradeInfo in subjects[0][k]:
                    grades_output = f"{grades_output}{gradeInfo[0]}; "
                    gradeTotal += gradeInfo[0]*gradeInfo[1]
                    toDivide += gradeInfo[1]
                gradeTotal = gradeTotal / toDivide
                print(f"{k} - {grades_output} | átlag: {gradeTotal}")
            else:
                print(f"{k} - Semmi")
        try:
            operation = int(input("Válasszon egy műveletet:1)Tantárgy hozzáadása\n\t\t\t2)Jegy hozzáadása\n\t\t\t3)Tantárgy eltávolítása\n\t\t\t4)Jegy eltávolítása\n\t\t\t5)Mentés és Kilépés\n\t\t\t6)Mentés nélküli kilépés\n"))

            if operation == 1:
                print(add_subject())
            elif operation == 2:
                print(add_grade())
            elif operation == 3:
                print(remove_subject())
            elif operation == 4:
                print(remove_grade())
            elif operation == 5:
                print(saveExit())
                time.sleep(2)
                break
            elif operation == 6:
                print("Kilépés.")
                time.sleep(2)
                break
        except:
            pass

    os.system('cls')
