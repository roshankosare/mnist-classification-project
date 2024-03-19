
# Build the CNN model
import sys
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
import pandas as pd
import numpy as np

from src.exception import CustomException


class CnnModel:
    def __init__(self) -> None:
        self.model = None
        
    def create_model(self):
        try:
            self.model  =Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Flatten(),
            Dense(64, activation='relu'),
            Dense(10, activation='softmax')
            ])
            self.model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'],)
        except Exception as e:
            raise CustomException(e,sys)
        
    def train_model(self,X_train:pd.DataFrame,y_train:pd.DataFrame,X_test:pd.DataFrame,y_test:pd.DataFrame):
        
        try:
            
            X_train = np.array(X_train).reshape(X_train.shape[0], 28, 28, 1)
            history = self.model.fit(X_train, y_train, epochs=5, batch_size=32)
            
            return self.model
        except Exception as e:
            raise CustomException(e,sys)
            
    

        # Evaluate the model







