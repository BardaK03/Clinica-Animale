import pickle

class ProceduraMedicala:
    def __init__(self, nume, data, nume_doctor, cost):
        self.nume = nume
        self.data = data
        self.nume_doctor = nume_doctor
        self.cost = cost

    def afisare_detalii(self):
        print("Nume procedura:", self.nume)
        print("Data procedura:", self.data)
        print("Nume doctor:", self.nume_doctor)
        print("Cost procedura:", self.cost)

class AnimalPacient:
    def __init__(self, rasa, nume, nume_stapan, telefon_stapan, email_stapan):
        self.rasa = rasa
        self.nume = nume
        self.nume_stapan = nume_stapan
        self.telefon_stapan = telefon_stapan
        self.email_stapan = email_stapan
        self.proceduri = []

    def adauga_procedura(self, procedura):
        self.proceduri.append(procedura)

    def calculeaza_cost_total(self):
        return sum(procedura.cost for procedura in self.proceduri)

    def afisare_proceduri(self):
        if self.proceduri:
            for procedura in self.proceduri:
                procedura.afisare_detalii()
                print("-------------------------")
        else:
            print("Nu exista proceduri asociate acestui animal pacient.")

class ClinicaVeterinara:
    def __init__(self):
        self.pacienti = []

    def cautare_pacient(self, nume):
        for pacient in self.pacienti:
            if pacient.nume == nume:
                return pacient
        return None

    def adauga_pacient(self, pacient):
        self.pacienti.append(pacient)

    def adauga_procedura_pacient(self, nume, procedura):
        pacient = self.cautare_pacient(nume)
        if pacient:
            pacient.adauga_procedura(procedura)
            print("Procedura adaugata pentru animalul pacient", pacient.nume)
        else:
            print("Animalul pacient nu a fost gasit.")

    def modificare_informatii_pacient(self, nume, nume_nou, nume_stapan_nou, telefon_stapan_nou, email_stapan_nou):
        pacient = self.cautare_pacient(nume)
        if pacient:
            pacient.nume = nume_nou
            pacient.nume_stapan = nume_stapan_nou
            pacient.telefon_stapan = telefon_stapan_nou
            pacient.email_stapan = email_stapan_nou
            print("Informatiile animalului pacient au fost modificate.")
        else:
            print("Animalul pacient nu a fost gasit.")

    def sterge_pacient(self, nume):
        pacient = self.cautare_pacient(nume)
        if pacient:
            self.pacienti.remove(pacient)
            print("Animalul pacient a fost sters.")
        else:
            print("Animalul pacient nu a fost gasit.")

    def sterge_proceduri_pacient(self, nume):
        pacient = self.cautare_pacient(nume)
        if pacient:
            pacient.proceduri = []
            print("Lista de proceduri a fost stearsa pentru animalul pacient", pacient.nume)
        else:
            print("Animalul pacient nu a fost gasit.")

    def afisare_pacienti(self):
        if self.pacienti:
            for pacient in self.pacienti:
                print("Nume pacient:", pacient.nume)
                print("Rasa:", pacient.rasa)
                print("Nume stapan:", pacient.nume_stapan)
                print("Telefon stapan:", pacient.telefon_stapan)
                print("Email stapan:", pacient.email_stapan)
                print("Proceduri asociate:")
                pacient.afisare_proceduri()
                print("-------------------------")
        else:
            print("Nu exista pacienti inregistrati.")

    def salvare_date(self, nume_fisier):
        with open(nume_fisier, "wb") as fisier:
            pickle.dump(self.pacienti, fisier)
        print("Datele au fost salvate in fisierul", nume_fisier)

    def incarcare_date(self, nume_fisier):
        try:
            with open(nume_fisier, "rb") as fisier:
                self.pacienti = pickle.load(fisier)
                print("Datele au fost incarcate din fisierul", nume_fisier)
        except FileNotFoundError:
            print("Fisierul", nume_fisier, "nu a fost gasit. Se va crea un tip de data gol.")

def main():
    nume_fisier = "date_clinica.bin"
    clinica = ClinicaVeterinara()
    clinica.incarcare_date(nume_fisier)

    while True:
        print("===== MENIU(CLINICA STEAUA BUCURESTI) =====")
        print("1. Cautare animal pacient")
        print("2. Adaugare animal pacient")
        print("3. Adaugare procedura pentru animalul pacient")
        print("4. Modificare informatii pacient")
        print("5. Stergere animal pacient")
        print("6. Stergere lista proceduri pacient")
        print("7. Afisare proceduri animal pacient")
        print("8. Afisare toti pacientii")
        print("9. Iesire si salvare date")
        print("--Va multumim ca ati ales serviciile noastre--")
        optiune = input("Selectati o optiune: ")

        if optiune == "1":
            nume = input("Introduceti numele animalului pacient: ")
            pacient = clinica.cautare_pacient(nume)
            if pacient:
                pacient.afisare_proceduri()
                cost_total = pacient.calculeaza_cost_total()
                print("Cost total proceduri:", cost_total)
            else:
                print("Animalul pacient nu a fost gasit.")

        elif optiune == "2":
            rasa = input("Introduceti rasa animalului pacient: ")
            nume = input("Introduceti numele animalului pacient: ")
            nume_stapan = input("Introduceti numele stapanului: ")
            telefon_stapan = input("Introduceti numarul de telefon al stapanului: ")
            email_stapan = input("Introduceti adresa de email a stapanului: ")

            pacient = AnimalPacient(rasa, nume, nume_stapan, telefon_stapan, email_stapan)
            clinica.adauga_pacient(pacient)
            print("Animalul pacient a fost adaugat cu succes.")

        elif optiune == "3":
            nume = input("Introduceti numele animalului pacient pentru care doriti adaugarea procedurii: ")
            pacient = clinica.cautare_pacient(nume)
            if pacient:
                nume_procedura = input("Introduceti numele procedurii: ")
                data_procedura = input("Introduceti data procedurii: ")
                nume_doctor = input("Introduceti numele doctorului sau persoanei responsabile: ")
                cost_procedura = float(input("Introduceti costul procedurii: "))

                procedura = ProceduraMedicala(nume_procedura, data_procedura, nume_doctor, cost_procedura)
                clinica.adauga_procedura_pacient(nume, procedura)
            else:
                print("Animalul pacient nu a fost gasit.")

        elif optiune == "4":
            nume = input("Introduceti numele animalului pacient pentru care doriti modificarea informatiilor: ")
            nume_nou = input("Introduceti noul nume al animalului pacient: ")
            nume_stapan_nou = input("Introduceti noul nume al stapanului: ")
            telefon_stapan_nou = input("Introduceti noul numar de telefon al stapanului: ")
            email_stapan_nou = input("Introduceti noua adresa de email a stapanului: ")

            clinica.modificare_informatii_pacient(nume, nume_nou, nume_stapan_nou, telefon_stapan_nou, email_stapan_nou)

        elif optiune == "5":
            nume = input("Introduceti numele animalului pacient pe care doriti sa-l stergeti: ")
            clinica.sterge_pacient(nume)

        elif optiune == "6":
            nume = input("Introduceti numele animalului pacient pentru care doriti stergerea listei de proceduri: ")
            clinica.sterge_proceduri_pacient(nume)

        elif optiune == "7":
            nume = input("Introduceti numele animalului pacient pentru care doriti afisarea procedurilor: ")
            pacient = clinica.cautare_pacient(nume)
            if pacient:
                pacient.afisare_proceduri()
            else:
                print("Animalul pacient nu a fost gasit.")

        elif optiune == "8":
            clinica.afisare_pacienti()

        elif optiune == "9":
            clinica.salvare_date(nume_fisier)
            break

        else:
            print("Optiune invalida. Va rugam selectati o optiune valida.")
main()