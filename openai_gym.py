import gym

env = gym.make("PongDeterministic-v4")
state = env.reset()

for t in range(10):
    action = env.action_space.sample()
    next_state, reward, done, info = env.step(action)
    state = next_state
    print(state.shape)
    # (210, 160, 3)