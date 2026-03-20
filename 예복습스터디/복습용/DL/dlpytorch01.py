import torch
from torch import nn

tensor = torch.rand(3,4)
tensor.shape
tensor.dtype
tensor.device
torch.cuda.is_available()

tensor = tensor.to('cpu')

tensor.device

device = 'cuda' if torch.cuda.is_available() else 'cpu'

#model

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer1_linear = nn.Linear(in_features= 28*28 , out_features= 512)
        self.layer1_linear = nn.ReLU()

        self.layer2_linear = nn.Linear(in_features= 512 , out_features= 10)
        self.layer1_linear = nn.ReLU()

    def forward(self, features):
        out = self.layer1_linear(features)
        out = self.layer1_relu(out)
        out = self.layer2_linear(out)
        return self.layer2_relu(out)
        
