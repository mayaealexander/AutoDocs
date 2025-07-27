# DOC_TITLE: Simple Rule-Based Agent and Environment Example
# DOC_SUMMARY: Demonstrates a minimal environment and a rule-based agent interacting over discrete steps.
# DOC_NOTE: This example shows how an agent can use simple logic to interact with an environment by observing state and choosing actions.
# DOC_LINKS: [Python Classes](https://docs.python.org/3/tutorial/classes.html)
# DOC_LINKS: [Reinforcement Learning Basics](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)

### Define a simple environment class
# DOC_STEP_SUMMARY: This step creates a SimpleEnvironment class that tracks a single integer state and updates it based on 'increment' or 'decrement' actions.

class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state if action is 'increment'
        elif action == 'decrement':
            self.state -= 1  # Decrease state if action is 'decrement'
        return self.state  # Return updated state

### Define a rule-based agent class
# DOC_STEP_SUMMARY: This step defines a RuleBasedAgent class that chooses to increment the state if it is less than 5, otherwise decrements it.

class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Choose to increment if state is below 5
        else:
            return 'decrement'  # Otherwise, choose to decrement

### Run the agent-environment loop
# DOC_STEP_SUMMARY: This step runs a loop where the agent observes the environment's state, selects an action, and the environment updates its state accordingly, printing each step.

env = SimpleEnvironment()      # Create environment instance
agent = RuleBasedAgent()       # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)   # Agent selects action based on current state
    new_state = env.step(action)              # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output step details
