# DOC_TITLE: Simple Rule-Based Agent and Environment Example
# DOC_SUMMARY: Demonstrates a minimal agent-environment interaction loop in Python.
# DOC_NOTE: This example shows a basic agent that increments or decrements a state variable based on a simple rule.
# DOC_LINKS: [Python Classes](https://docs.python.org/3/tutorial/classes.html)
# DOC_LINKS: [Reinforcement Learning Concepts](https://en.wikipedia.org/wiki/Reinforcement_learning)

### Step 1: Define the environment
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        # Update state based on action
        if action == 'increment':
            self.state += 1  # Increase state by 1
        elif action == 'decrement':
            self.state -= 1  # Decrease state by 1
        return self.state  # Return the new state

### Step 2: Define the rule-based agent
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed

    def select_action(self, state):
        # Choose action based on current state
        if state < 5:
            return 'increment'  # Increment if state is less than 5
        else:
            return 'decrement'  # Decrement otherwise

### Step 3: Run the agent-environment loop
env = SimpleEnvironment()  # Create environment instance
agent = RuleBasedAgent()   # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)  # Agent decides action
    new_state = env.step(action)             # Environment updates state
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output step info
