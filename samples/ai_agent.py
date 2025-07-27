# DOC_TITLE: Simple Rule-Based Agent and Environment Example
# DOC_SUMMARY: Demonstrates a minimal agent-environment interaction loop in Python.
# DOC_NOTE: This example shows a simple environment where the agent chooses to increment or decrement a state variable based on a rule.
# DOC_LINKS: [Python Classes](https://docs.python.org/3/tutorial/classes.html)
# DOC_LINKS: [Reinforcement Learning Concepts](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)

### Define a simple environment with increment/decrement actions
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state by 1
        elif action == 'decrement':
            self.state -= 1  # Decrease state by 1
        return self.state  # Return updated state

### Define a rule-based agent that chooses actions based on state
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed for this agent

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Increase state if less than 5
        else:
            return 'decrement'  # Decrease state if 5 or more

### Run the agent-environment loop
env = SimpleEnvironment()  # Create environment instance
agent = RuleBasedAgent()   # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)  # Agent decides action based on current state
    new_state = env.step(action)             # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output step info
