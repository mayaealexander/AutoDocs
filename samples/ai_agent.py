# DOC_TITLE: Simple Environment and Rule-Based Agent Example
# DOC_SUMMARY: Demonstrates a minimal agent-environment loop with state updates and rule-based action selection.
# DOC_NOTE: This example shows how an agent can interact with an environment by choosing actions based on the current state.
# DOC_LINKS: [Python Classes](https://docs.python.org/3/tutorial/classes.html)
# DOC_LINKS: [Reinforcement Learning Basics](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)

### Define the environment class
# DOC_STEP_SUMMARY: Defines a simple environment class that maintains an integer state and updates it based on increment or decrement actions.
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state if action is increment
        elif action == 'decrement':
            self.state -= 1  # Decrease state if action is decrement
        return self.state  # Return updated state

### Define the rule-based agent class
# DOC_STEP_SUMMARY: Implements a rule-based agent that chooses to increment the state until a threshold is reached.
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed for this agent

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Choose to increment if state is below threshold
        return 'decrement'  # Otherwise, choose to decrement

### Run agent-environment interaction loop
# DOC_STEP_SUMMARY: Instantiates the environment and agent, then runs a loop where the agent selects actions and the environment updates its state.
env = SimpleEnvironment()      # Create environment instance
agent = RuleBasedAgent()       # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)    # Agent selects action based on current state
    new_state = env.step(action)               # Environment updates state using action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output current step, action, and state
