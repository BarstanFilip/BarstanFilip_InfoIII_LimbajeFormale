class TrafficLightController:
    def __init__(self):
        self.state = "S0" 

    def transition(self, A, B):
     
        transitions = {
            "S0": {(0, 0): ("S0", 0), (0, 1): ("S1", 1), (1, 0): ("S0", 0), (1, 1): ("S1", 1)},
            "S1": {(0, 0): ("S1", 1), (0, 1): ("S1", 1), (1, 0): ("S0", 0), (1, 1): ("S0", 0)}
        }
        
      
        self.state, output = transitions[self.state][(A, B)]
        return output


controller = TrafficLightController()
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1), (0, 1), (1, 0), (1, 1)]

for inp in test_inputs:
    output = controller.transition(*inp)
    print(f"input {inp}, output {output}, newState {controller.state}")
