

import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, IsolationForest, VotingClassifier
from sklearn import svm
from sklearn.model_selection import cross_val_score
from read_data import get_data, get_tones
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import tensorflow as tf

def one_hot_encoding(chosen_classes, number_of_classes):
    # Prepare array for target output
    one_hot_encoding = np.zeros([len(chosen_classes), number_of_classes])
    one_hot_encoding[np.arange(one_hot_encoding.shape[0]), chosen_classes] = 1
    return one_hot_encoding

class simple_classifier(nn.Module):

    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.linear1 = nn.Linear(input_size,self.hidden_size)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(self.hidden_size,self.hidden_size)
        self.linear3 = nn.Linear(self.hidden_size,self.output_size)

    def forward(self, x):
        x = self.linear1(x)
        x = self.linear2(x)
        x = self.linear3(x)
        return x
        # END TODO #############

def get_batch(x,y, batch_size):
    chosen_index = np.random.randint(max(len(y) - batch_size,0))
    return x[chosen_index:chosen_index + batch_size], y[chosen_index:chosen_index + batch_size]

def train(model,x,y, episodes, batch_size):
    optimizer = torch.optim.Adam(model.parameters(), lr=0.2)
    loss_fn = torch.nn.MSELoss(reduction='mean')
    for e in range(episodes):
        for b in range(len(y)//batch_size):
            # Get data
            x_batch, y_batch = get_batch(x,y,batch_size)
            # Reset gradient
            optimizer.zero_grad()
            output = model(x_batch)
            loss = loss_fn(output, y_batch)
            loss.backward()
            optimizer.step()

def main():
    # Here get data
    X,y = get_data()
    tones = get_tones()
    # Prepare data
    X = np.array(X)
    tones = np.array(tones)
    X = np.concatenate((X, tones), axis=1)

    # Classifiers
    # Adaboost classifier
    clfAda = AdaBoostClassifier(n_estimators=20, random_state=0)
    clfAda.fit(X, y)
    
    # Support vector machine
    clfSVC = svm.SVC()
    clfSVC.fit(X, y)
    
    # Gradient boosting
    clfGBC = GradientBoostingClassifier(n_estimators=20, learning_rate=1.0, max_depth=1, random_state=0)
    clfGBC.fit(X, y)

    # RandomForestClassifier
    clfRF = RandomForestClassifier(n_estimators=10)
    clfRF.fit(X, y)
    
    # Use all classifiers
    clfV = VotingClassifier(estimators=[('clfAda', clfAda), ('clfSVC', clfSVC), ('clfGBC', clfGBC), ('clfRF', clfRF)], voting='hard')
    
    

    # Get model
    classifier_network = simple_classifier(input_size = 10, hidden_size = 10, output_size = 4)
    # Convert data to tensor
    y = np.array(y)
    y = one_hot_encoding(y,4)
    y = torch.tensor(y)
    y = y.float()
    X = torch.tensor(X)
    X = X.float()
    # Train model
    train(classifier_network,X,y,1,8)
    # Accuracy
    y_hat = classifier_network(X)
    #for x,y in zip(X, y_hat):
        #print(x,' | ',y,'\n')
    y_hat_hot = one_hot_encoding(np.argmax(y_hat.detach(), axis=1), 4)
    #print('accuracies ',torch.mean(4*(y * y_hat_hot)))
    wyniki = np.argmax(y_hat.detach(), axis=1)
    with open('wyniki', 'w') as f:
        #print(y_hat_hot)
        f.write(str(wyniki))
    

if __name__ == "__main__":
    main()