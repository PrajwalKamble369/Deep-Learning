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

---

# 17/04/2026


## <u>**PyTorch Autograd**</u>
- Topic Studied
    - Why is Autograd Important?
    - What is Autograd?

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
