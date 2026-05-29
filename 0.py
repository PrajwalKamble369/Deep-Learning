import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import optuna
from torch.utils.data import Dataset, DataLoader

data = pd.read_csv(r"C:\Users\DELL\My_Local_Desktop\Deep-Learning\DataSets\breast_cancer_data.csv")
data.head()
