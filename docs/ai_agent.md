<!-- AUTO‑GENERATED doc for ai_agent.py -->
# Simple Rule-Based Agent and Environment Example

_Demonstrates a minimal agent-environment interaction loop in Python._


- This example shows a simple environment where the agent chooses to increment or decrement a state variable based on a rule.

## Step‑by‑step walk‑through
Step 1: Define a simple environment with increment/decrement actions
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

Step 2: Define a rule-based agent that chooses actions based on state
```python
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed for this agent

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Increase state if less than 5
        else:
            return 'decrement'  # Decrease state if 5 or more

```

Step 3: Run the agent-environment loop
```python
env = SimpleEnvironment()  # Create environment instance
agent = RuleBasedAgent()   # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)  # Agent decides action based on current state
    new_state = env.step(action)             # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output step info
```


## Resources
* [Python Classes](https://docs.python.org/3/tutorial/classes.html)
* [Reinforcement Learning Concepts](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)

<details><summary>Full source</summary>

```python

### Define a simple environment with increment/decrement actions
class SimpleEnvironment:
    def __init__(self):
        self.state = 0  # Initialize state to zero

    def step(self, action):
        if action == 'increment':
            self.state += 1  # Increase state by 1
        elif action == 'decrement':
            self.state -= 1  # Decrease state by 1
        return self.state  # Return updated state

### Define a rule-based agent that chooses actions based on state
class RuleBasedAgent:
    def __init__(self):
        pass  # No initialization needed for this agent

    def select_action(self, state):
        if state < 5:
            return 'increment'  # Increase state if less than 5
        else:
            return 'decrement'  # Decrease state if 5 or more

### Run the agent-environment loop
env = SimpleEnvironment()  # Create environment instance
agent = RuleBasedAgent()   # Create agent instance

for step in range(10): 
    action = agent.select_action(env.state)  # Agent decides action based on current state
    new_state = env.step(action)             # Environment updates state based on action
    print(f"Step {step+1}: Action={action}, State={new_state}")  # Output step info
```
</details>
Last updated: 2025-07-27
