import pandas as pd
import numpy as np;
import unittest
from ML_function import ML_regression
d1 = {'Animals':[1,"dog","cat","bird"],"Fruits": ["banana",5,"orange","blueberry"]}
df = pd.DataFrame(d1)
X = df[['Animals']]
Y = df[['Fruits']]

class TestMLRegresion(unittest.TestCase):
    
    def test_input(self):#checking if the input data is a string
        with self.assertRaises(TypeError): 
            ML_regression(X,Y)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
