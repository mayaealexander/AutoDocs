# DOC_TITLE: Minimal Rule-Based Agent and Environment Example
# DOC_SUMMARY: Demonstrates a simple agent interacting with an environment by incrementing or decrementing state.
# DOC_NOTE: This example illustrates a basic agent-environment loop, useful for understanding reinforcement learning fundamentals.
# DOC_LINKS: [OpenAI Gym Basics](https://www.gymlibrary.dev/content/basic_usage/)

### Define the simple environment class
# DOC_STEP_SUMMARY: This step creates a SimpleEnvironment class that tracks a single integer state and updates it based on increment or decrement actions.
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state if action is increment
        elif action == 'decrement':
            self.state -= 1  # Decrease state if action is decrement
        return self.state  # Return the updated state

### Define the rule-based agent class
# DOC_STEP_SUMMARY: This step defines a RuleBasedAgent class that selects actions to increment the state until it reaches 5, then decrements.
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed for this agent

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Choose to increment if state is below 5
        else:
            return 'decrement'  # Otherwise, choose to decrement

### Run the agent-environment interaction loop
# DOC_STEP_SUMMARY: This step runs a loop where the agent observes the environment's state, selects an action, updates the environment, and prints the results for 10 steps.
env = SimpleEnvironment()  # Create environment instance
agent = RuleBasedAgent()   # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)  # Agent chooses action based on current state
    new_state = env.step(action)             # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output step details