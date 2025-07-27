# DOC_TITLE: Minimal Rule-Based Agent and Environment Example
# DOC_SUMMARY: Demonstrates a simple agent-environment interaction loop in Python.
# DOC_NOTE: This example shows a basic agent that increments or decrements state based on a threshold.
# DOC_LINKS: [Python Classes](https://docs.python.org/3/tutorial/classes.html)
# DOC_LINKS: [Reinforcement Learning Basics](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)

### Define a simple environment with integer state
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state by one if action is increment
        elif action == 'decrement':
            self.state -= 1  # Decrease state by one if action is decrement
        return self.state  # Return updated state

### Define a rule-based agent that selects actions based on state
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed for this agent

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Choose increment if state is below threshold
        else:
            return 'decrement'  # Choose decrement if state is at or above threshold

### Instantiate environment and agent, then run interaction loop
env = SimpleEnvironment()  # Create environment instance
agent = RuleBasedAgent()   # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)  # Agent chooses action based on current state
    new_state = env.step(action)             # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Display step, action, and state