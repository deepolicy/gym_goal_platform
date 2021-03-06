import tensorflow as tf
import numpy as np
import time

def test_env(env_name='env_platform'):
    
    if env_name == 'env_goal':
        from .env import env_goal as env_wrapper
    else:
        from .env import env_platform as env_wrapper

    env = env_wrapper.env

    state = env.reset()

    def get_action():

        MT_params = env_wrapper.MT_params
        '''
        gym_platform:

        MT_params = {
            'run': 1,
            'hop': 1,
            'leap': 1,
        }

        gym_goal:
        MT_params = {
            'kick-to': 2,
            'shoot-goal-left': 1,
            'shoot-goal-right': 1,
        }

        '''

        action = [MT for MT in MT_params][np.random.randint(0, 3)]
        print('action')
        print(action)

        params = [np.random.rand(MT_params[action]) * 2 - 1]  # [-1, 1)

        print('params')
        print(params)
        '''
        action
        shoot-goal-right
        params
        [array([0.97337239])]
        '''

        return action, params


    while 1:
        action, params = get_action()

        action_trans = env_wrapper.get_action_trans(action, params)

        print('action_trans')
        print(action_trans)

        # time.sleep(1)
        env.render()

        state_next, reward, done, info = env.step(action_trans)

        print('reward, done')
        print(reward, done)

        state = state_next

        if done:
            state = env.reset()
            break


def main():
    test_env()

if __name__ == '__main__':
    main()
