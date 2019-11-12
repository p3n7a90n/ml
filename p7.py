import numpy as np
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination


data=pd.read_csv("Data7.csv")
data=data.replace("?",np.nan)



print(test.head())
