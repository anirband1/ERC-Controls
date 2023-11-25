import gym

LENGTH = 3000
THRESHOLD = 0.8

gym.envs.register(
    id='CartPole-v1',
    entry_point='gym.envs.classic_control:CartPoleEnv',
    max_episode_steps=LENGTH,
    reward_threshold=-110.0,
)


env = gym.make("CartPole-v1", render_mode = "human")
observation = env.reset()

action = env.action_space.sample() # + your agent here (this takes random actions)

def run(threshold_val):
    THRESHOLD_VAL = threshold_val # 0.3
    
    env = gym.make("CartPole-v1", render_mode = "human")
    observation = env.reset()

    action = env.action_space.sample() # + your agent here (this takes random actions)

    observation, reward, terminated, truncated, info = env.step(action)
    init_pos = observation[0]
    for _ in range(LENGTH):
        env.render()
        final_pos = []

        # 1
        if observation[3] >= THRESHOLD_VAL:
            action = 1
        if observation[3] <= -THRESHOLD_VAL:
            action = 0

        # 2
        if -THRESHOLD_VAL < observation[3] < THRESHOLD_VAL:
            if observation[2] > 0:
                action = 1
            else:
                action = 0
        
        observation, reward, terminated, truncated, info = env.step(action)
        final_pos_t = observation[0]
        final_pos.append(final_pos_t)

        if terminated or truncated:
            observation, info = env.reset()
    env.close()

run(THRESHOLD)



# logic: 1 makes the cart's velocity approx. equal to the velocity of COM of pole (since pole wont rotate if vel is same)
#        2 once velocity is similar, the system still travels strongly to one side, hence to correct that, adjust the cart position according 
#           to the angle the pole is making. This makes the pole come to the centre and prevents the whole system wandering off to one side

# if THRESHOLD too low, system drifts off
# if too high, it oscillates (not a problem in sim, but irl would take up more energy)
