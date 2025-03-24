class ENFA:
    def __init__(self, states, input_symbols, transitions, iState, fState):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = iState
        self.final_states = fState

    def Eclosure(self, state, vizitat=None):
        if vizitat is None:
            vizitat = set()
        vizitat.add(state)
        if '' in self.transitions.get(state, {}):
            for next_state in self.transitions[state]['']:
                if next_state not in vizitat:
                    self.Eclosure(next_state, vizitat)
        return vizitat

    def accepts(self, input_str):
        current_states = self.Eclosure(self.initial_state)
        for symbol in input_str:
            next_states = set()
            for state in current_states:
                if symbol in self.transitions.get(state, {}):
                    for next_state in self.transitions[state][symbol]:
                        next_states.update(self.Eclosure(next_state))
            current_states = next_states
        return any(state in self.final_states for state in current_states)


nfa = ENFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'': {'q1', 'q4'}},  'q1': {'b': {'q2'}},'q2': {'a': {'q3'}, 'b': {'q3'}},'q3': {'a': {'q3'}, 'b': {'q3'}, '': {'q5'}}, 'q4': {'a': {'q5'}} },
    iState='q0',fState={'q5'}
)


print(nfa.accepts("ba"))  
print(nfa.accepts("bb"))  
print(nfa.accepts("baba"))  
print(nfa.accepts("a"))  
print(nfa.accepts("b")) 
