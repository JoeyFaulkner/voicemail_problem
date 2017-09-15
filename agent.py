import numpy as np


class agent:
    def __init__(self, error_rate=0.3, max_convo_length=10):
        self.error_rate = error_rate
        self.max_convo_length = max_convo_length
        self.intent_space = ['save', 'delete']
        self.action_space = ['save', 'delete', 'ask']
        self.past_conversations = []
        self.start_new_conversation()

    def start_new_conversation(self):
        self.current_intention = np.random.choice(self.intent_space)
        self.turns = []

    def interact(self, action):
        assert action in self.action_space
        self.turns.append(action)
        if len(self.turns) > self.max_convo_length:
            self.start_new_conversation()
            return {'intent': 'EOC', 'reward': -1}
        if action == 'save':
            if self.current_intention == 'save':
                self.start_new_conversation()
                return {'intent': 'EOC', 'reward': 10}

            elif self.current_intention == 'delete':
                self.start_new_conversation()
                return {'intent': 'EOC', 'reward': -100}

        elif action == 'delete':
            if self.current_intention == 'delete':
                self.start_new_conversation()
                return {'intent': 'EOC', 'reward': 10}

            elif self.current_intention == 'save':
                self.start_new_conversation()
                return {'intent': 'EOC', 'reward': -100}

        elif action == 'ask':
            seed = np.random.rand()
            if seed < self.error_rate:
                wrong = [intent for intent in self.intent_space if intent != self.current_intention][0]
                return {'intent': wrong, 'reward': -1}
            else:
                return {'action': self.current_intention, 'reward': -1}

if __name__ == '__main__':
    ag = agent()
    while True:
        out = ag.interact(np.random.choice(ag.action_space))
        print out['reward']
        if out['intent'] == 'EOC':
            print out['reward']

