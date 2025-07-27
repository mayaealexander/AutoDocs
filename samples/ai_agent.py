class SimpleEnvironment:
    def __init__(self):
        self.state = 0  

    def step(self, action):
        if action == 'increment':
            self.state += 1 
        elif action == 'decrement':
            self.state -= 1  
        return self.state 

class RuleBasedAgent:
    def __init__(self):
        pass 

    def select_action(self, state):
        if state < 5:
            return 'increment' 
        else:
            return 'decrement'  

env = SimpleEnvironment()  
agent = RuleBasedAgent()  

for step in range(10): 
    action = agent.select_action(env.state)  
    new_state = env.step(action)           
    print(f"Step {step+1}: Action={action}, State={new_state}")  
