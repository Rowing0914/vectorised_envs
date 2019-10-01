"""
Check the url below
https://github.com/openai/gym#whats-new
"""

import gym

env = gym.vector.make("PongDeterministic-v4", num_envs=4)
state = env.reset()

for t in range(10):
    action = env.action_space.sample()
    next_state, reward, done, info = env.step(action)
    state = next_state
    print(state.shape)
    # (4, 210, 160, 3)