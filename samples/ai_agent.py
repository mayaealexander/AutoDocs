# DOC_TITLE: Simple Environment and Rule-Based Agent Example
# DOC_SUMMARY: Demonstrates a minimal agent-environment loop with state updates and rule-based action selection.
# DOC_NOTE: This example shows how an agent can interact with an environment by choosing actions based on the current state.
# DOC_STEP_SUMMARY: Defines a simple environment class that maintains an integer state and updates it based on increment or decrement actions.

### Define the environment class
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state if action is increment
        elif action == 'decrement':
            self.state -= 1  # Decrease state if action is decrement
        return self.state  # Return updated state

# DOC_STEP_SUMMARY: Implements a rule-based agent that chooses to increment the state until a threshold is reached.

### Define the rule-based agent class
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed for this agent

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Choose to increment if state is below threshold
        return 'decrement'  # Otherwise, choose to decrement

# DOC_STEP_SUMMARY: Instantiates the environment and agent, then runs a loop where the agent selects actions and the environment updates its state.

### Run agent-environment interaction loop
env = SimpleEnvironment()      # Create environment instance
agent = RuleBasedAgent()       # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)    # Agent selects action based on current state
    new_state = env.step(action)               # Environment updates state using action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output current step, action, and state
