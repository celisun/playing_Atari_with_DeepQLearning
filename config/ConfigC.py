# CONFIG FOR CRITIC BRAIN IN ACTOR-CRITIC
configC = {
    "inputs_dim": 8,
    "hidden_dim": 50,
    "outputs_dim": 1,     # one state value of given state
    "GAMMA": 0.99,
    "learning_rate": 0.00025,#0.01,
    "weight_decay": 0.0001,
    "betas": (0.001, 0.9)
    
    
}
