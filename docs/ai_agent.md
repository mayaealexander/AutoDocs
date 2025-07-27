<!-- AUTO‑GENERATED doc for ai_agent.py -->
# Simple Rule-Based Agent and Environment Example

_Demonstrates a minimal agent-environment interaction loop in Python._


- This example shows how an agent can interact with an environment using simple rule-based logic.

## Step‑by‑step walk‑through
### Step 1: Define the environment class
This step defines the environment class.

```python
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state if action is 'increment'
        elif action == 'decrement':
            self.state -= 1  # Decrease state if action is 'decrement'
        return self.state  # Return the updated state

```

### Step 2: Define the rule-based agent class
This step defines the rule-based agent class.

```python
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed for this agent

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Choose to increment if state is less than 5
        else:
            return 'decrement'  # Otherwise, choose to decrement

```

### Step 3: Run the agent-environment interaction loop
This step runs the agent-environment interaction loop.

```python
env = SimpleEnvironment()  # Create an instance of the environment
agent = RuleBasedAgent()   # Create an instance of the agent

for step in range(10): 
    action = agent.select_action(env.state)  # Agent selects an action based on current state
    new_state = env.step(action)             # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output the current step, action, and state
```


## Resources
* [Python Classes](https://docs.python.org/3/tutorial/classes.html)
* [Reinforcement Learning Basics](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)

<details><summary>Full source</summary>

```python

### Define the environment class
# DOC_STEP_SUMMARY: This step defines a simple environment with a mutable integer state and a method to update it based on actions.
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state if action is 'increment'
        elif action == 'decrement':
            self.state -= 1  # Decrease state if action is 'decrement'
        return self.state  # Return the updated state

### Define the rule-based agent class
# DOC_STEP_SUMMARY: This step creates a rule-based agent that decides whether to increment or decrement the state based on its value.
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed for this agent

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Choose to increment if state is less than 5
        else:
            return 'decrement'  # Otherwise, choose to decrement

### Run the agent-environment interaction loop
# DOC_STEP_SUMMARY: This step runs a loop where the agent selects actions and the environment updates its state, printing results at each step.
env = SimpleEnvironment()  # Create an instance of the environment
agent = RuleBasedAgent()   # Create an instance of the agent

for step in range(10): 
    action = agent.select_action(env.state)  # Agent selects an action based on current state
    new_state = env.step(action)             # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output the current step, action, and state
```
</details>
Last updated: 2025-07-27
