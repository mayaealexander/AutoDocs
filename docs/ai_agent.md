<!-- AUTO‑GENERATED doc for ai_agent.py -->
# Minimal Rule-Based Agent and Environment Example

_Demonstrates a simple agent-environment interaction loop in Python._


- This example shows a basic agent that increments or decrements state based on a threshold.

## Step‑by‑step walk‑through
### Step 1: Define a simple environment with integer state
Initialize state to zero Increase state by one if action is increment Decrease state by one if action is decrement Return updated state.

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

### Step 2: Define a rule-based agent that selects actions based on state
No initialization needed for this agent Choose increment if state is below threshold Choose decrement if state is at or above threshold.

```python
class RuleBasedAgent:
    def __init__(self):
        pass

    def select_action(self, state):
        if state < 5:
            return 'increment'
        else:
            return 'decrement'

```

### Step 3: Instantiate environment and agent, then run interaction loop
Create environment instance Create agent instance Agent chooses action based on current state Environment updates state based on action Display step, action, and state.

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
* [Reinforcement Learning Basics](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)

<details><summary>Full source</summary>

```python

### Define a simple environment with integer state
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state by one if action is increment
        elif action == 'decrement':
            self.state -= 1  # Decrease state by one if action is decrement
        return self.state  # Return updated state

### Define a rule-based agent that selects actions based on state
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed for this agent

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Choose increment if state is below threshold
        else:
            return 'decrement'  # Choose decrement if state is at or above threshold

### Instantiate environment and agent, then run interaction loop
env = SimpleEnvironment()  # Create environment instance
agent = RuleBasedAgent()   # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)  # Agent chooses action based on current state
    new_state = env.step(action)             # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Display step, action, and state
```
</details>
Last updated: 2025-07-27
