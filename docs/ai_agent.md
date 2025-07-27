<!-- AUTO‑GENERATED doc for ai_agent.py -->
# Simple Rule-Based Agent and Environment Example

_Demonstrates a minimal environment and a rule-based agent interacting over discrete steps._


- This example shows how an agent can use simple logic to interact with an environment by observing state and choosing actions.

## Step‑by‑step walk‑through
### Step 1: Define a simple environment class
This step creates a SimpleEnvironment class that tracks a single integer state and updates it based on 'increment' or 'decrement' actions.

```python
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state if action is 'increment'
        elif action == 'decrement':
            self.state -= 1  # Decrease state if action is 'decrement'
        return self.state  # Return updated state

```

### Step 2: Define a rule-based agent class
This step defines a RuleBasedAgent class that chooses to increment the state if it is less than 5, otherwise decrements it.

```python
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Choose to increment if state is below 5
        else:
            return 'decrement'  # Otherwise, choose to decrement

```

### Step 3: Run the agent-environment loop
This step runs a loop where the agent observes the environment's state, selects an action, and the environment updates its state accordingly, printing each step.

```python
env = SimpleEnvironment()      # Create environment instance
agent = RuleBasedAgent()       # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)   # Agent selects action based on current state
    new_state = env.step(action)              # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output step details
```


## Resources
* [Python Classes](https://docs.python.org/3/tutorial/classes.html)
* [Reinforcement Learning Basics](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)

<details><summary>Full source</summary>

```python

### Define a simple environment class

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

class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Choose to increment if state is below 5
        else:
            return 'decrement'  # Otherwise, choose to decrement

### Run the agent-environment loop

env = SimpleEnvironment()      # Create environment instance
agent = RuleBasedAgent()       # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)   # Agent selects action based on current state
    new_state = env.step(action)              # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output step details
```
</details>
Last updated: 2025-07-27
