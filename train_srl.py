import omnisafe


env_id = 'SafetyPointGoal0-v0'

agent = omnisafe.Agent('PPOLag', env_id)
agent.learn()