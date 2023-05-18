class State:
    def __init__(self, name, transitions):
        self.name = name
        self.transitions = transitions
    
class Transition:
    def __init__(self, target_state, condition):
        self.target_state = target_state
        self.condition = condition
    
class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state
        
    def transition(self, condition):
        for transition in self.current_state.transitions:
            if transition.condition(condition):
                self.current_state = transition.target_state
                break
        
    def run(self, inputs):
        for input in inputs:
            self.transition(input)
    
    def is_in_state(self, state_name):
        return self.current_state.name == state_name
    


# Define the states and transitions
s0 = State('s0', [Transition(s1, lambda x: x == 'a'), Transition(s2, lambda x: x == 'b')])
s1 = State('s1', [Transition(s2, lambda x: x == 'b')])
s2 = State('s2', [Transition(s0, lambda x: x == 'a'), Transition(s3, lambda x: x == 'c')])
s3 = State('s3', [])

# Create the state machine with an initial state of s0
sm = StateMachine(s0)

# Run the state machine with some inputs
inputs = ['a', 'b', 'c', 'a', 'b']
sm.run(inputs)

# Check if the state machine is in a specific state
print(sm.is_in_state('s3'))  # True