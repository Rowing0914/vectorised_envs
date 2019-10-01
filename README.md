## Investigated Libraries
- [OpenAI baselines](https://github.com/openai/baselines/tree/master/baselines/common/vec_env) in python and TensorFlow includes many state of the art algorithms.
- [RLLib](https://github.com/ray-project/ray/blob/master/rllib/env/vector_env.py) in python, for TensorFlow and PyTorch, includes tool for hyperparameter tuning, and very importantly support for multi-agent systems.
- [Nervana’s Coach](https://github.com/NervanaSystems/coach/tree/master/rl_coach/environments) in python and TensorFlow and optimised for Intel processors, also with many relevant algorithms.
- [TensorForce](https://github.com/tensorforce/tensorforce/tree/master/tensorforce/environments) in python and TensorFlow is an ambitious framework that also includes many relevant algorithms.
- [RLLab](https://github.com/rll/rllab/tree/master/rllab/envs)(not active) implements in python very relevant algorithms like Trust Region Policy Optimization (TRPO) and Deep Deterministc Policy Gradient (DDPG) algorithms, Cross-Entropy Method (CEM), Covariance Matrix Adaptation - Evolutionary Strategy (CMA-ES)… and some others.
- [Keras-RL](https://github.com/keras-rl/keras-rl/blob/master/rl/common/vec_env/subproc_env_vec.py)(not active) implements in python Deep Q-learning (DQN), Double DQN (which removes the bias from max operator in Q-learning), DDPG, Continuous DQN (CDQN or NAF) and CEM.
- [tf_agents](https://github.com/tensorflow/agents/tree/master/tf_agents/environments)
  

## Reference
- https://www.quora.com/What-are-some-of-the-good-Reinforcement-Learning-libraries