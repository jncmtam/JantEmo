import torch
import torch.nn as nn

class EmotionMentalCNN(nn.Module):
    def __init__(self, num_emotion=4, num_state=2):
        super(EmotionalMentalCNN, self).__init__()
        
        