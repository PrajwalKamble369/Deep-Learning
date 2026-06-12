# This is my Learning Journey of Deep Learning i am Tracking my Study in This repository

# 02/04/2026

## <u>**Introduction to Pytorch**</u>

- PyTorch is open source pythond liabrary which is used for deep learning.
- By using PyTorch we can build powerful nueral network based apps.

---

- PyTorch(0.1) Launched in 2018
    - Python Compatibility.
    - Dynamic Computation Graph.


- PyTorch(1.0) 2018
    - Bridge the gap between research and production environment.
    - Introduce torch script.
    - Merger with Caffe2.

- PyTorch(1.x) Series
    - Support Distrubated Training.
    - Support ONNX.
    - Expanded ecosystem.

- PyTorch(2.x) Series
    - Optimazion in latency and throughput.

    
---

- Core Features
    - Tensor(multidimensional arrays) Computions.
    - GPU Acceleration
    - Dynamic Computation Graph
    - Automatic Differentiation
    - Distrubated Training
    - Interoperability with other liabraries 

[Open Introduction to PyTorch Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/intro_to_Pytorch.ipynb)

---

# 16/04/2026


## <u>**Tensors in PyTorch**</u>
- Topic Studied
    - What are Tensors?
    - Scalar
    - Vector
    - Matrices
    - 3D Tensors
    - 4D Tensors
    - 5D Tensors
    - Why are Tensors Useful?
    - Where are Tensors used in Deep Learning?
    - Practical with Code Example
    - Creating a Tensor
    - Tensor Shapes
    - Tensor Data Types
    - Mathematical Operations on Tensors
    - Inplace Operations
    - Copying a Tensor
    - Tensor Operations on GPU
    - Reshaping Tensors
    - NumPy and PyTorch

[Open Tensors in PyTorch Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/tensors.ipynb)

---

# 17/04/2026


## <u>**PyTorch Autograd**</u>
- Topic Studied
    - Why is Autograd Important?
    - What is Autograd?

[Open PyTorch Autograd Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/pytorch_autograd.ipynb)

---

# 24/04/2026

## <u>**Pytorch Training Pipeline**</u>
- Topic Studied
    - Take a DataSet :
    - Build a small neural network on it
    - Understand Training Piepline in PyTorch through this
    - It can be used for all nueral network
    - In this have manual elements
    - End Goal is understand how to build nueral network in PyTorch

    - Control Flow :
        - Load Data
        - Basic Preprocessing
        - Training Process
            - Create the model (single nueron (30 input feature so 30 weights and 1 bias))
            - Forward Pass
            - Loss Function
            - Backpropogation (Backward Pass)
            - Parameter Update
        - Model evaluation (accuracy is used)

[Open PyTorch Training Pipeline Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/pytorch_training_pipeline.ipynb)

---

# 27/04/2026

## <u>**Pytorch 'nn' module & torch.optim module**</u>

- Topics Studied:
    - How to Improve Training Pipeline:
        - NN Module 
        - torch.optim module
    - What are the improvements:
        - not give parameters manually
        - used built in loss function
        - used built in activation function
        - not update parameter manually will use torch.optim
    - Summary:
        - Built an nueral network using nn module
        - Use built in activation function
        - Use built in loss function
        - Use built in optimizer

[Open torch.nn & torch.optim Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/nn_module.ipynb)

---

# 04/05/2026

## <u>**Dataset & DataLoader Class in PyTorch**</u>

- Topic Studied:
    - Dataset & Dataloader Class

    - Problems
        1) Memory inefficient due to batch gradient decent.
        2) Not Better Convergence due to batch gradient decent.

        - Solution:
            - Using batches (mini batch gradient descent) of data to train the model.

    - The Dataset and Dataloader Classes
        - Dataset and Dataloader are core abstraction in PyTorch that decouple how you define your data from how you efficiently iterate over it in training loop. This means we sperate data load and data training process.
        - Consider we have csv data file having 10 rows and batch size is 2 so toatal batches = 10/2 = 5. 
            - We have to create custom dataset class which inherit from `CustomDataset(Dataset)`
        - Dataset Class:
            - The dataset class is essentially a blueprint when you create custom dataset, you decide how data is loaded and returned.
            - It defines:
                - `__init__()` which tells how data should be loaded.
                - `__len__()` which returns the total number of samples.
                - `__getitem__(index)` which returns the data (and labels) at given index

        - DataLoader Class:
            - The DataLoader wraps a Dataset and handles batching, shuffling and parallel loading.
        - DataLoader Control Flow:
            - At the start of each epoch, the DataLoader (if `shuffle=True`) shuffle indices(using a sampler)
            - It divides the indices into chunck of batch size.
            - For each index in the chunk, data samples are fetched from the Dataset object
            - The samples are then collected and combined into a batch (using collate function)
            - The batch is returned to the main training loop

[Open Datset & DataLoader Class Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/dataset%26dataloaderclasses.ipynb)

---
# 21/05/2026

## <u>**Building a ANN using PyTorch**</u>

- Topic Studied:

    - ANN (Artificial Nueral Network)/ MLP (Multi Layer Perceptron)
        - Built ANN
        - Architecture of ANN:
            - input layer (784 nodes)
            - first hidden layer (128 neurons and relu function is used)
            - second hidden layer (64 neurons and relu function is used)
            - output layer (10 neurons and softmax function is used)
        - Workflow:
            - DataLoader Object for training and test data.
            - Training Loop
            - Evaluation

[Open Building ANN Using PyTorch Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/ann.ipynb)

---
# 27/05/2026
## <u>**Neural Network Training on GPU**</u>

- Topic Studied:
    - Nueral Network Training on GPU
        - Check GPU Availibility
        - Move Model to GPU
        - Modify the Trainnig Lopp by Moving Data to GPU
        - Modify the Evaluation loop by Moving Data to GPU

[Open Nueral Network Training on GPU Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/trainingongpu.ipynb)

--- 
# 28/05/2026

## <u>**Optimizing The Nueral Network**</u>

- Topic Studied:
    - Problem:
        - Accuracy on Test Data = 0.8895
        - Accuracy on Train Data = 0.9778541666666667
        - This is Overfitting and this is not good
    - Solutions:
        - Adding more data
        - Reducing the complexity of nueral network architecture
        - Regularization
        - Dropouts
        - Data Augmentation
        - Batch Normalization
        - Early Stopping
    - Used Solutions for this problem are:
        - Regularization
        - Dropout
        - Batch Normalization
    - Accuracies after using Regulaization, Dropout,Bactch Normalization
        - Accuracy on Test Data = 0.8933333333333333
        - Accuracy on Train Data = 0.9483958333333333
        - 0.9483958333333333 - 0.8933333333333333 = 0.055062500000000014

[Open Optimazion of Nueral Network Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/optimizingnn.ipynb)

--- 
# 29/05/2026

## <u>**Hyperparameter Tuning the ANN using Optuna**</u>
- Topic Studied:
    - Hyperparmeter Tuning on Parameters:
        1) Number of Hidden Layers
        2) Neurons Per Layer
        3) Number of Epochs
        4) Optimizer
        5) Learning Rate
        6) Batch Size
        7) Dropout Rate
        8) Weight Decay (lambda)
    
    - Use of optuna
    1) create objective function
        - `def objective()`
        - search space
        - model init
        - parameters init
        - training loop
        - evaluation loop
    2) Study Object
        - Trail

[Open Hyperparameter Tuning Using Optuna Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/hyperparametertuning.ipynb)


--- 
# 05/06/2026

## <u>**Building CNN Using PyTorch**</u>
- Topic Studied:
    - What is CNN?
    - CNN Architecture

[Open CNN with PyTorch Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/cnn_pytorch.ipynb)

---
# 07/06/2026

## <u>**Transfer Learning using PyTorch**</u>
- Topic Studied:
    - What is Transfer Learning
    - Why does Transfer learning work?
    - Workflow

[Open Transfer Learning Using PyTorch Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/transfer_learning.ipynb)

---
# 12/06/2026

## <u>**RNN using PyTorch**</u>
- Topic Studied:

[Open RNN Using PyTorch Notebook](https://github.com/PrajwalKamble369/Deep-Learning/blob/main/rnn_pytorch.ipynb)
