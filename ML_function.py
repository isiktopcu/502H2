import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import stats as st
np.set_printoptions(suppress=True) #to discard the scientific notation 


def ML_regression(X,Y):

    #a column of ones is created to add to the explanatory variable matrix 
    
    column_of_ones = np.ones((len(X),1), dtype=int)
    column_of_ones
    
    #concatenating the explanatory variables matrix with the column of ones 
   
    X_final = np.concatenate((column_of_ones,X), axis=1)
   
    #the normal equation 
    
    res1 = np.dot(X_final.T,X_final)
    res2 = np.linalg.inv(res1)
    res3 = np.dot(res2,X_final.T)
    res4 = np.dot(res3,Y)
    print("Coefficients: ",res4.reshape(res4.shape[0],).tolist())
    
    #Y-pred 
    Y_pred = np.dot(X_final,res4)
   
    
    
    #Sum of Squared Errors (SSE)
    #E = Errors 
    E = Y - Y_pred
    sse = np.dot(E.T,E)
    sse
    print("SSE: ",sse.reshape(sse.shape[0],).tolist())
   
    
    #Mean of Squared Errors (MSE) 
    
    E = Y - Y_pred
    n = len(Y)
    mse = sse / (n - X.shape[1])
    print("MSE: ", mse.reshape(mse.shape[0],).tolist())
    
    #Standard Errors
    
    se = math.sqrt(mse)
    print("SE: ",se)
    
    #a list of variable standard errors 
    se_variables = np.sqrt(np.diag(mse*res2)).tolist()
    
    #a list of betas
    betalist = res4.reshape(res4.shape[0],).tolist()
    
    #a dictionary of beta - se tuples to be used in the CI formula 
    d1 = dict(zip(betalist,se_variables))
    
    #t-stat
    #%95 confidence
    t = st.t.ppf(1-0.025,n-X.shape[1])
    print("t-stat: ", t)
    
    
    #%95 Confidence Intervals 
    #Lower CI's

    #intercept lower
    #GDP lower
    #Undernourishment lower 
    for beta in d1:
        print("Lower CI's: ", beta-(t*d1[beta]))
        
    #Upper CI's

    #intercept upper
    #GDP upper
    #Undernourishment upper

    for beta in d1:
        print("Upper CI's: ", beta+(t*d1[beta]))
        
    #t-values 
    
    t_list = []
    #intercept t-value
    #GDP t-value
    #Undernourishment t-value 
    for beta in d1:  
        beta/d1[beta]
        t_list.append(beta/d1[beta])
    print("t-values: ", t_list)
    
    #intercept t
    #GDP t
    #Undernourishment t 
    for t_v in t_list:
        if t_v >= t:
            print('Null hypothesis rejected.')
        else:
            print("Failed to reject the null hypothesis.")