class DFA:
    def __init__(self):
        self.stari = {'q0', 'q1', 'q2'}
        self.alfabet = {'0', '1', '2'}
        self.tranzitie = {('q0', '0'): 'q0',('q0', '1'): 'q1',('q0', '2'): 'q2',('q1', '1'): 'q1',('q1', '2'): 'q1',('q2', '2'): 'q2' }
        self.stareInceput = 'q0'
        self.stareFinala = {'q2'}

    def simulare(self, input_string):
        stareCurenta = self.stareInceput
        for symbol in input_string:
            if (stareCurenta, symbol) in self.tranzitie:
                stareCurenta = self.tranzitie[(stareCurenta, symbol)]
            else:
                return False  
        return stareCurenta in self.stareFinala
    
dfa = DFA()
inputTranzitii = ["", "0", "1", "2", "10", "12", "111", "112", "222", "0212"]

for test in inputTranzitii:
    result = dfa.simulare(test)
    print(f"input {test} gasit {result}")
