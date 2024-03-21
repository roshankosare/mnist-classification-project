
# Build the CNN model
import sys
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense

import keras

from mnistClassifier.exception import CustomException


class CnnModel:
    def __init__(self,dense_size:int = 64) -> None:
        self.model = None
        self.dense_size = dense_size
        
    def create_model(self,)->keras.Model:
        try:
    
            self.model  =Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Flatten(),
            Dense(self.dense_size, activation='relu'),
            Dense(10, activation='softmax')
            ])
            self.model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'],)
            
            return self.model
        except Exception as e:
            raise CustomException(e,sys)
        
            
    

        # Evaluate the model







