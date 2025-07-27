<!-- AUTO‑GENERATED doc for ai_agent.py -->
# Simple Rule-Based Agent and Environment Example

_Demonstrates a minimal agent-environment interaction loop in Python._


- This example shows a basic agent that increments or decrements a state variable based on a simple rule.

## Step‑by‑step walk‑through
### Step 1: Step 1: Define the environment
Initialize state to zero Increase state by 1 Decrease state by 1 Return the new state

```python
class SimpleEnvironment:
    def __init__(self):
        self.state = 0

    def step(self, action):
        # Update state based on action
        if action == 'increment':
            self.state += 1
        elif action == 'decrement':
            self.state -= 1
        return self.state

```

### Step 2: Step 2: Define the rule-based agent
No initialization needed Increment if state is less than 5 Decrement otherwise

```python
class RuleBasedAgent:
    def __init__(self):
        pass

    def select_action(self, state):
        # Choose action based on current state
        if state < 5:
            return 'increment'
        else:
            return 'decrement'

```

### Step 3: Step 3: Run the agent-environment loop
Create environment instance Create agent instance Agent decides action Environment updates state Output step info

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
* [Reinforcement Learning Concepts](https://en.wikipedia.org/wiki/Reinforcement_learning)

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

### Step 2: Define the rule-based agent
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
Last updated: 2025-07-27
