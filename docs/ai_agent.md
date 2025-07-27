<!-- AUTO‑GENERATED doc for ai_agent.py -->
# Simple Rule-Based Agent and Environment Example

_Demonstrates a minimal agent-environment loop with rule-based action selection._


- This example shows how an agent can interact with a simple environment using a fixed rule.

## Step‑by‑step walk‑through
Step 1: Define the environment
```python
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        # Update state based on action
        if action == 'increment':
            self.state += 1  # Increase state by 1
        elif action == 'decrement':
            self.state -= 1  # Decrease state by 1
        return self.state  # Return the new state

```

Step 2: Define the agent
```python
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed

    def select_action(self, state):
        # Choose action based on current state
        if state < 5:
            return 'increment'  # Increment if state is less than 5
        else:
            return 'decrement'  # Decrement otherwise

```

Step 3: Run the agent-environment loop
```python
env = SimpleEnvironment()  # Create environment instance
agent = RuleBasedAgent()   # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)  # Agent decides action
    new_state = env.step(action)             # Environment updates state
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output step info
```


## Resources
* [OpenAI Gym Basics](https://www.gymlibrary.dev/)

<details><summary>Full source</summary>

```python

### Step 1: Define the environment

class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        # Update state based on action
        if action == 'increment':
            self.state += 1  # Increase state by 1
        elif action == 'decrement':
            self.state -= 1  # Decrease state by 1
        return self.state  # Return the new state

### Step 2: Define the agent

class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed

    def select_action(self, state):
        # Choose action based on current state
        if state < 5:
            return 'increment'  # Increment if state is less than 5
        else:
            return 'decrement'  # Decrement otherwise

### Step 3: Run the agent-environment loop

env = SimpleEnvironment()  # Create environment instance
agent = RuleBasedAgent()   # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)  # Agent decides action
    new_state = env.step(action)             # Environment updates state
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output step info
```
</details>
Last updated: 2025-07-20
