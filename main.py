class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__history = []

    def add_record(self, doctor, record):
        if isinstance(doctor, Doctor):
            self.__history.append(record)
        else:
            print("Faqat shifokor yozuv qo‘sha oladi.")

    def get_history(self, requester):
        if isinstance(requester, Doctor):
            return self.__history
        else:
            return "Maxfiy ma'lumot"


class Doctor:
    def __init__(self, name):
        self.name = name


class Receptionist:
    def __init__(self, name):
        self.name = name



pat = Patient("Javohir", 30)
doc = Doctor("Dr. Karimov")
rec = Receptionist("Oygul")

pat.add_record(doc, "Tomoq og‘rishi.")
print(pat.get_history(doc))  # ['Tomoq og‘rishi.']
print(pat.get_history(rec))  # Maxfiy ma'lumot
