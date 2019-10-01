# https://github.com/openai/baselines/blob/master/baselines/common/vec_env/test_vec_env.py#L114
import gym, numpy as np

class SimpleEnv(gym.Env):
    """
    An environment with a pre-determined observation space
    and RNG seed.
    """

    def __init__(self, seed, shape, dtype):
        np.random.seed(seed)
        self._dtype = dtype
        self._start_obs = np.array(np.random.randint(0, 0x100, size=shape), dtype=dtype)
        self._max_steps = seed + 1
        self._cur_obs = None
        self._cur_step = 0
        # this is 0xFF instead of 0x100 because the Box space includes
        # the high end, while randint does not
        self.action_space = gym.spaces.Box(low=0, high=0xFF, shape=shape, dtype=dtype)
        self.observation_space = self.action_space

    def step(self, action):
        self._cur_obs += np.array(action, dtype=self._dtype)
        self._cur_step += 1
        done = self._cur_step >= self._max_steps
        reward = self._cur_step / self._max_steps
        return self._cur_obs, reward, done, {'foo': 'bar' + str(reward)}

    def reset(self):
        self._cur_obs = self._start_obs
        self._cur_step = 0
        return self._cur_obs

    def render(self, mode=None):
        raise NotImplementedError