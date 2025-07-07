# DOC_TITLE: Simple AI Agent Example
# DOC_SUMMARY: Implements a basic rule-based AI agent that interacts with a simple environment.
# DOC_NOTES: This sample demonstrates class definition, agent policy, and an environment loop.
# DOC_LINKS: https://en.wikipedia.org/wiki/Intelligent_agent

### Define the Environment
class SimpleEnvironment:
    def __init__(self):
        self.state = 0
    def step(self, action):
        if action == 'increment':
            self.state += 1
        elif action == 'decrement':
            self.state -= 1
        return self.state

### Define the AI Agent
class RuleBasedAgent:
    def __init__(self):
        pass
    def select_action(self, state):
        # Simple policy: increment if state < 5, else decrement
        if state < 5:
            return 'increment'
        else:
            return 'decrement'

### Run the Agent in the Environment
env = SimpleEnvironment()
agent = RuleBasedAgent()

for step in range(10):
    action = agent.select_action(env.state)
    new_state = env.step(action)
    print(f"Step {step+1}: Action={action}, State={new_state}") 