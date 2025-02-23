#1
def AutomatFinit(input_string):
    state = 'q0'
    final_states = {'q3'}
    transitions = {
        'q0': {'0': 'q1', '1': 'q2'}, 'q1': {'0': 'q3', '1': 'q0'}, 'q2': {'0': 'q1', '1': 'q3'}
    }
    
    for symbol in input_string:
        state = transitions.get(state, {}).get(symbol)
        if state is None:
            return False
    
    return state in final_states


print(AutomatFinit("010"))
#2
def detectCat(text):
    state = "q0"  
    
    for char in text:
        if state == "q0":
            if char == 'c':
                state = "q1"
                
        elif state == "q1":
            if char == 'a':
                state = "q2"
            elif char != 'c':
                state = "q0"  
        elif state == "q2":
            if char == 't':
                state = "q3"  
                return True
            elif char == 'c':
                state = "q1"  
            else:
                state = "q0" 
    
    return False 


text = "there is a cat here"
print(detectCat(text)) 

#3
class automatFinitVerificare:
    def __init__(self):
        self.finalState = "q3"
        self.transitions = {"q0": "q1","q1":"q2","q2":"q3","q3":"q3"}

    def eCuvant(self, cuvant):
        state = "q0"
        for char in cuvant:
         if char not in "abcd":
              return False
         state = self.transitions.get(state, "q3")
        return state == self.finalState

af = automatFinitVerificare()
words = ["abcac", "aaabbc", "bbbac"]

for cuvant in words:
    print(f"'{cuvant}{af.eCuvant(cuvant)}")
