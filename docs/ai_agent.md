<!-- AUTO‑GENERATED doc for ai_agent.py -->
# Simple Rule-Based Agent and Environment Example

_Demonstrates a minimal agent-environment loop with state updates and rule-based action selection._




**Notes:**
> This example shows how an agent can interact with an environment by choosing actions based on the current state, and how the environment updates its state accordingly.


## Step‑by‑step walk‑through
### Step 1: Define the environment class
This step creates an environment class that maintains a state variable and provides a step method to update it based on actions.

```python
class SimpleEnvironment:
    def __init__(self):
        self.state = 0

    def step(self, action):
        if action == 'increment':
            self.state += 1
        elif action == 'decrement':
            self.state -= 1
        return self.state

```

### Step 2: Define the rule-based agent class
This step defines an agent class that selects actions based on the current state using a simple rule.

```python
class RuleBasedAgent:
    def __init__(self):
        pass

    def select_action(self, state):
        if state < 5:
            return 'increment'
        return 'decrement'

```

### Step 3: Run the agent-environment interaction loop
This step runs a loop where the agent selects actions and the environment updates its state, printing each step's outcome.

```python
env = SimpleEnvironment()
agent = RuleBasedAgent()

for step in range(10):
    action = agent.select_action(env.state)
    new_state = env.step(action)
    print(f"Step {step+1}: Action={action}, State={new_state}")
```


## Resources
* [Python Classes](https://docs.python.org/3/tutorial/classes.html)
* [Reinforcement Learning (Wikipedia)](https://en.wikipedia.org/wiki/Reinforcement_learning)

<details><summary>Full source</summary>

```python

### Define the environment class
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state if action is 'increment'
        elif action == 'decrement':
            self.state -= 1  # Decrease state if action is 'decrement'
        return self.state  # Return updated state

### Define the rule-based agent class
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed for this agent

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Choose to increment if state is less than 5
        return 'decrement'  # Otherwise, choose to decrement

### Run the agent-environment interaction loop
env = SimpleEnvironment()     # Create environment instance
agent = RuleBasedAgent()      # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)    # Agent chooses action based on current state
    new_state = env.step(action)               # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")   # Output step, action, and state
```
</details>
Last updated: 2025-07-27
