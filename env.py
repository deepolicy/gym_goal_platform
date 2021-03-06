import numpy as np
import gym
import gym_platform
import gym_goal

from .utils import scale_to

class env_platform():

    env = gym.make('Platform-v0')

    obs_dim = 9

    MT_params = {
        'run': 1,
        'hop': 1,
        'leap': 1,
    }
    
    def get_action_trans(action, params):

        MT_params = env_platform.MT_params

        action_index = [i for i in MT_params].index(action)

        # print([(p.low, p.high) for p in env.action_space[1]])
        # [(array([0.], dtype=float32), array([30.], dtype=float32)), 
        # (array([0.], dtype=float32), array([720.], dtype=float32)), 
        # (array([0.], dtype=float32), array([430.], dtype=float32))]

        if action_index == 0:
            low, high = 0., 30.
        elif action_index == 1:
            low, high = 0., 720.
        elif action_index == 2:
            low, high = 0., 430.

        params[0][0] = scale_to(params[0][0], low, high, scale=1.5)

        params = tuple([np.array(params[0]) if MT == action else np.array([0.]) for MT in MT_params])

        return (action_index, params)

class env_goal():

    env = gym.make('Goal-v0')

    obs_dim = 14

    MT_params = {
        'kick-to': 2,
        'shoot-goal-left': 1,
        'shoot-goal-right': 1,
    }

    def get_action_trans(action, params):

        MT_params = env_goal.MT_params

        action_index = [i for i in MT_params].index(action)

        # print([(p.low, p.high) for p in env.action_space[1]])
        # [(array([  0., -15.], dtype=float32), array([40., 15.], dtype=float32)), 
        # (array([-7.01], dtype=float32), array([7.01], dtype=float32)), 
        # (array([-7.01], dtype=float32), array([7.01], dtype=float32))]

        if action_index == 0:
            low, high = [0., -15.], [40., 15.]
        elif action_index == 1:
            low, high = [-7.01], [7.01]
        elif action_index == 2:
            low, high = [-7.01], [7.01]

        for i in range(np.array(params).shape[1]):
            params[0][i] = scale_to(params[0][i], low[i], high[i], scale=1.5)

        params = tuple([np.array(params[0]) if MT == action else np.array([0.] * MT_params[MT]) for MT in MT_params])

        return (action_index, params)