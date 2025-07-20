# DOC_TITLE: Simple Rule-Based Agent and Environment Example
# DOC_BLURB: Demonstrates a minimal agent-environment interaction loop in Python.
# DOC_NOTE: This example shows how a simple agent can interact with an environment using basic rules.
# DOC_LINKS: [Reinforcement Learning Basics](https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf)

### Step 1: Define the environment class
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        # Update state based on action
        if action == 'increment':
            self.state += 1  # Increase state by 1
        elif action == 'decrement':
            self.state -= 1  # Decrease state by 1
        return self.state  # Return updated state

### Step 2: Define the rule-based agent class
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed

    def select_action(self, state):
        # Choose action based on current state
        if state < 5:
            return 'increment'  # Move state up if below 5
        else:
            return 'decrement'  # Move state down if 5 or above

### Step 3: Run the agent-environment interaction loop
env = SimpleEnvironment()  # Create environment instance
agent = RuleBasedAgent()   # Create agent instance

for step in range(10):  # Run for 10 steps
    action = agent.select_action(env.state)  # Agent decides action
    new_state = env.step(action)             # Environment updates state
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Log step info
