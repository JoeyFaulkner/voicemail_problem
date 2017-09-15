# voicemail_problem

A simple python implementation of the voicemail problem (as explained in https://www.researchgate.net/publication/220794470_Gaussian_Processes_for_Fast_Policy_Optimisation_of_POMDP-based_Dialogue_Managers), which is a starting point for reinforcement learning in dialogue. From there,


>The state space of this task consists of three states:the user asked for the message either to be savedor deleted, or the dialogue ended. The systemcan take three actions: ask the user what to do,save or delete the message. For both learning and evaluation, a simulated user is usedwhich makes an error with probability 0.3 and ter-minates the dialogue after at most 10 turns. In theﬁnal state, it gives a positive reward of 10 or apenalty of −100 depending on whether the systemperformed a correct action or not. Each intermediate state receives the penalty of −1.

Agent can be interacted with via agent.interact(action), where the action can be either 'save', 'delete' or 'ask'. The agent will return a dictionary with 'intent' and 'reward' dependent on its desired intent. Intent is either 'delete', 'save', or 'EOC' - i.e. end of conversation. The agent will automatically end the conversation after 10 turns.

For example, a random set of actions for an agent can be done by: 

```
  ag = agent()
  while True:
    out = ag.interact(np.random.choice(ag.action_space))
    print out['reward']
    if out['intent'] == 'EOC':
        print out['reward']
```

Hopefully will get around to implementing some algos for learning it.
