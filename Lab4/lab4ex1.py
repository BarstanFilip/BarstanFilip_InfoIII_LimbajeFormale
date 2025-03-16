class NFA:
    def __init__(self, transitions, start, accept):
        self.trans = transitions
        self.start = start
        self.accept = accept
    
    def eps_closure(self, states):
        stack, closure = list(states), set(states)
        while stack:
            state = stack.pop()
            for nxt in self.trans.get((state, ''), []):
                if nxt not in closure:
                    closure.add(nxt)
                    stack.append(nxt)
        return closure
    
    def move(self, states, symbol):
        return {nxt for s in states for nxt in self.trans.get((s, symbol), [])}
    
    def accepts(self, input_str):
        states = self.eps_closure({self.start})
        for symbol in input_str:
            states = self.eps_closure(self.move(states, symbol))
        return bool(states & self.accept)

transitions = {
    ('q0', 'a'): {'q1'}, ('q1', 'a'): {'q1'}, ('q1', ''): {'q2'},  ('q2', 'b'): {'q2', 'q3'}, ('q3', 'a'): {'q3'}, ('q3', 'b'): {'q3'}, ('q3', ''): {'q4'}
}

nfa = NFA(transitions, 'q0', {'q4'})
print(f"Accepted: {nfa.accepts('aabb')}")
