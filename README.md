# Mushroom neural network
Neural network classifier for edible mushrooms, using Python. Application is prepared for given mushrooms data, but thanks to separated the classification problem from neural network, network is multipurpose. That means network may have any number of inputs, outputs, as well as hidden layers.

### Prerequisutes
- Matplotlib module, can be install with
``` pip install matplotlib ```

### Run application
User may set:
1. Neurons in each hidden layer e.g. [5,4], then we have 5 neurons in first layer and 4 in the second
2. Max number of learnign epochs
3. Learning rate
4. Methof of learning - mini-batch (<i>"batch"</i>) or incremental learnign (<i>"svg"</i>)
5. If batch learning was chosen we may set the size of mini batches

Examples of launching the application:
```
python main.py [5] 10 0.9 svg
```
```
python main.py [2,3] 25 0.9 batch 10
```
