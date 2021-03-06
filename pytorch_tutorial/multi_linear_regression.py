import torch
import torch.nn as nn
import torch.nn.functional as F 
from torch.utils.data import TensorDataset,DataLoader
class MultivariableLinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(3,3)
        self.linear2 = nn.Linear(3,1)
    def forward(self,x):
        x = self.linear1(x)
        return self.linear2(x)
x_train  =  torch.FloatTensor([[73,  80,  75], 
                               [93,  88,  93], 
                               [89,  91,  90], 
                               [96,  98,  100],   
                               [73,  66,  70]])  
y_train  =  torch.FloatTensor([[152],  [185],  [180],  [196],  [142]])

dataset = TensorDataset(x_train,y_train)
dataloader = DataLoader(dataset,batch_size=2,shuffle=True)

model = MultivariableLinearRegression()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-5)
epcohs = 20
for epoch in range(epcohs+1):
    for batch_idx, samples in enumerate(dataloader):
        x_train , y_train = samples
        prediction = model(x_train)
        cost = F.mse_loss(prediction,y_train)

        optimizer.zero_grad()
        cost.backward()
        optimizer.step()
        print('Epoch {:4d}/{} Batch {}/{} Cost: {:.6f}'.format(
            epoch, epcohs, batch_idx+1, len(dataloader),
            cost.item()
            ))
new_var = torch.FloatTensor([[73,80,75]])
pred_y = model(new_var)
print(pred_y)
torch.save(model.state_dict(),'test_model.pt')