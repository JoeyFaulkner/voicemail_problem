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

    def interact(self, intent):
        assert intent in self.action_space
        if len(self.turns) > self.max_convo_length:
            return {'action': 'EOC', 'reward': -1}
        if intent == 'save':
            if self.current_intention == 'save':
                return {'action': 'EOC', 'reward': 10}

            elif self.current_intention == 'delete':
                return {'action': 'EOC', 'reward': -100}

        elif intent == 'delete':
            if self.current_intention == 'delete':
                return {'action': 'EOC', 'reward': 10}

            elif self.current_intention == 'save':
                return {'action': 'EOC', 'reward': -100}

        elif intent == 'ask':
            seed = np.random.rand()
            if seed < self.error_rate:
                wrong = [intent for intent in self.intent_space if intent != self.current_intention][0]
                return {'action': wrong, 'reward': -1}
            else:
                return {'action': self.current_intention, 'reward': -1}

if __name__ == '__main__':
    ag = agent()
    while True:
        out = ag.interact(np.random.choice(ag.action_space))
        print out['reward']
        if out['action'] == 'EOC':
            print out['reward']
