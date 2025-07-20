<!-- AUTO‑GENERATED doc for ai_agent.py -->
# Rule-Based Agent in a Simple Environment

_Demonstrates a basic agent interacting with a minimal stateful environment._


- This example shows a loop where an agent chooses actions based on the current state, and the environment updates accordingly.

## Step‑by‑step walk‑through
### 1. Prelude
```python

```

### 2. Define the environment class
```python
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state by 1
        elif action == 'decrement':
            self.state -= 1  # Decrease state by 1
        return self.state  # Return updated state

```

### 3. Define the rule-based agent class
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

### 4. Run the agent-environment interaction loop
```python
env = SimpleEnvironment()  # Create environment instance
agent = RuleBasedAgent()   # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)  # Agent decides action based on current state
    new_state = env.step(action)             # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output current step, action, and state
```


## Resources
* [Python Classes](https://docs.python.org/3/tutorial/classes.html)

<details><summary>Full source</summary>

```python

### Define the environment class
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state by 1
        elif action == 'decrement':
            self.state -= 1  # Decrease state by 1
        return self.state  # Return updated state

### Define the rule-based agent class
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed for this agent

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Choose to increment if state is less than 5
        else:
            return 'decrement'  # Otherwise, choose to decrement

### Run the agent-environment interaction loop
env = SimpleEnvironment()  # Create environment instance
agent = RuleBasedAgent()   # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)  # Agent decides action based on current state
    new_state = env.step(action)             # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output current step, action, and state
```
</details>
Last updated: 2025-07-20
