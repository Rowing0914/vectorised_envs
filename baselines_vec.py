# I don't like this,,,,

import numpy as np
from baselines.common.vec_env.subproc_vec_env import SubprocVecEnv
from utils import SimpleEnv

dtype = "float32"
num_envs = 5
num_steps = 100
shape = (1, 4)

def make_fn(seed):
    """
    Get an environment constructor with a seed.
    """
    return lambda: SimpleEnv(seed, shape, dtype)

fns = [make_fn(i) for i in range(num_envs)]
env = SubprocVecEnv(fns)

state = env.reset()

for t in range(10):
    actions = np.array([env.action_space.sample() for _ in range(env.num_envs)])
    env.step_async(actions)
    next_state, reward, done, info = env.step_wait()
    state = next_state
    print(state.shape)
    # (5, 1, 4)