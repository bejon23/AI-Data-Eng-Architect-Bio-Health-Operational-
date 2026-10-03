# PROJECT 3: ED Wait Time Optimization
import random

class EDEnvironment:
    def __init__(self):
        self.doctors = [False, False, False]
        self.patient_count = 0

    def reset(self):
        self.doctors = [False, False, False]
        self.patient_count = 0
        return 0

    def step(self, action):
        if not self.doctors[action]:
            self.doctors[action] = True
            reward = 10
        else:
            reward = -5
        self.patient_count += 1
        next_state = self.patient_count % 3
        done = (self.patient_count >= 10)
        return next_state, reward, done

class SimpleAgent:
    def __init__(self):
        self.q_table = {}
        self.learning_rate = 0.1
        self.discount = 0.9

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0)

    def update(self, state, action, reward, next_state):
        current_q = self.get_q_value(state, action)
        future_q = max([self.get_q_value(next_state, a) for a in range(3)])
        new_q = current_q + self.learning_rate * (reward + self.discount * future_q - current_q)
        self.q_table[(state, action)] = new_q

    def choose_action(self, state):
        if random.random() < 0.1:
            return random.randint(0, 2)
        values = [self.get_q_value(state, a) for a in range(3)]
        return values.index(max(values))

agent = SimpleAgent()
env = EDEnvironment()

for episode in range(20):
    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(state)
        state, reward, done = env.step(action)
        agent.update(state, action, reward, state)

print("Training complete!")
print("Q-Table:", agent.q_table)
