class MooreMachine:
    def __init__(self):
        self.state = 'S1'  
        self.output = {'S1': 'O1', 'S2': 'O2'} 
    def transition(self, inputS):
        if self.state == 'S1':
            if inputS == 'A':
                self.state = 'S1'
            elif inputS == 'B':
                self.state = 'S2'
        elif self.state == 'S2':
            if inputS == 'A':
                self.state = 'S1'
            elif inputS == 'B':
                self.state = 'S2'
        return self.output[self.state]  
    
    def process_inputs(self, inputs):
        outputs = []
        for inp in inputs:
            outputs.append(self.transition(inp))
        return outputs


moore = MooreMachine()
inputs = ['A', 'B', 'B', 'A', 'A', 'B']  
outputs = moore.process_inputs(inputs)
print(outputs)