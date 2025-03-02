import random

class Parcare:
    def __init__(self, n):
        self.n = n
        self.locuriParcare = [random.choice([0, 1]) for _ in range(n)]
        print("Parcare initiala ", self.locuriParcare)

    def displayLocuri(self):
        print("Parcarea acum ", self.locuriParcare)

    def parcheaza_masina(self):
        locuriLibere = [i for i in range(self.n) if self.locuriParcare[i] == 0]
        if not locuriLibere:
            print("Nu sunt locuri libere momentan")
            return False

        locAles = random.choice(locuriLibere)
        self.locuriParcare[locAles] = 1
        print(f"Loc ocupat la nr {locAles + 1}")
        return True

    def pleacaMasina(self):
        locuriOcupate = [i for i in range(self.n) if self.locuriParcare[i] == 1]
        if not locuriOcupate:
            print("Parcare goala")
            return False

        locAles = random.choice(locuriOcupate)
        self.locuriParcare[locAles] = 0
        print(f"Loc eliberat la nr  {locAles + 1}")
        return True

    def run(self):
        while True:
            self.displayLocuri()
            action = input("p parcheaza s sterge x inchide program ").strip().lower()
            if action == 'p':
                self.parcheaza_masina()
            elif action == 's':
                self.pleacaMasina()
            elif action == 'x':
                print("  ")
                break
            else:
                print("Tasta gresita")

if __name__ == "__main__":
    n = int(input("Nr de locuri "))
    parcare = Parcare(n)
    parcare.run()
 