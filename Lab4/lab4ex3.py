class MealyMachine:
    def __init__(self):
        self.state = 'Q1' 
    
    def transition(self, inputS):
        if self.state == 'Q1' and inputS == 'X':
            self.state = 'Q2'
            return 'O1'
        elif self.state == 'Q1' and inputS == 'Y':
            self.state = 'Q1'
            return 'O1'
        elif self.state == 'Q2' and inputS == 'X':
            self.state = 'Q2'
            return 'O2'
        elif self.state == 'Q2' and inputS == 'Y':
            self.state = 'Q2'
            return 'O2'
        else:
            return 'error'
    
    def process_inputs(self, inputs):
        outputs = []
        for inp in inputs:
            outputs.append(self.transition(inp))
        return outputs


mealy = MealyMachine()
inputs = ['X', 'Y', 'X', 'Y', 'X'] 
outputs = mealy.process_inputs(inputs)
print(outputs)
