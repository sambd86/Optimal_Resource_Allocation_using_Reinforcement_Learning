"""
This file contains all constant test parameters which may be altered from this single location for convenience.
"""



class Parameters:
    #algo = "DDPG"
    algo = "TD3"
    gamma = 0.99
    tau = 0.001
    #  The weights of target networks are updated by having them slowly track the learned networks:

    #  This means that the target values are constrained to change slowly, greatly improving the stability of learning.

    ou_noise = True
    param_noise = False
    noise_scale = 0.5
    final_noise_scale = 0.3
    seed = 42 #random number generation seed
    batch_size = 128
    #max_num_time_steps = 700 #maximum episode length By default 1600 for bipedal env
    max_num_timesteps = 4 * 6
    num_episodes = 1000 #total number of episodes
    exploration_end = 0.9* num_episodes #total episodes with exploration

    actor_hidden_size = 256 #number of nodes in all the hidden layers of the actor except the output node
    updates_per_step = 3# total number of parameter updates on both actor and critics per time step
    replay_size = 100000000 #size of the replay buffer


    #-------------------------------Note, we will not use these noise types here, just the parameter noise.
    # DDPG trains a deterministic policy in an off-policy way. Because the policy is deterministic,
    # if the agent were to explore on-policy, in the beginning it would probably not try a wide enough variety of actions to find useful learning signals.
    # i.e, we scale OU noise on the basis of no of episodes remaining, we decrease the noise as the total no of remaining episodes decreases.
    # To make DDPG policies explore better, we add noise to their actions at training time. The authors of the original DDPG paper recommended time-correlated OU noise,
    # but more recent results suggest that uncorrelated, mean-zero Gaussian noise works perfectly well. Since the latter is simpler, it is preferred.
    # To facilitate getting higher-quality training data, you may reduce the scale of the noise over the course of training.
    #
    # At test time, to see how well the policy exploits what it has learned, we do not add noise to the actions.


    save_foldername = 'DataCenter_Parameter_File/'