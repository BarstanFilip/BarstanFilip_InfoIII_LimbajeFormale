class AutomatCafea:
    def __init__(self):
        self.stare = "q0"  
    
    def tranzitie(self, input):
        if self.stare == "q0":
            if input == "c":
                self.stare = "q1"
            elif input == "t":
                self.stare = "q2"
            elif input == "h":
                self.stare = "q3"
            elif input == "a":
                self.stare = "q4"
        elif self.stare in ["q1", "q2", "q3", "q4"] and input == "ok":
            self.stare = "q5"
        else:
            self.stare = "q0"  
    
    def run(self, inputs):
        for input in inputs:
            self.tranzitie(input)
        
        if self.stare == "q5":
            return "bautura este gata "
        else:
            return "litera gresita"


inputs = input("comenzi c,t,h,a,ok ")
automat = AutomatCafea()
rezultat = automat.run(inputs.split())
print(rezultat)
