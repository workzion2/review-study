import torch
from torch import nn

device = 'cuda' if torch.cuda.is_available() else 'cpu'
device

class DenseModel(nn.module):
    def __init__(self, features_size:int , target_size:int, 
                dense_size:int = 512)-> None:
                
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(in_features= features_size, 
            out_features= dense_size),
            nn.ReLU(),
            nn.Linear(in_features= dense_size,
            out_features= dense_size*2),
            nn.ReLU(),
            nn.Linear(in_features= dense_size*2, 
            out_features =target_size),
            nn.ReLU()
        )
#모델 학습 함수
    def forward(self, features): #(batch, features)
        out =self.fc_layer(features)
        return out

model = DenseModel(features_size= 10, target_size = 1).to(device)



