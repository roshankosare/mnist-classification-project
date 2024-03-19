
from flask import Flask,request,render_template, jsonify
import base64
from PIL import Image
from io import BytesIO
import pandas as pd
from src.utils.image import preprocess_image
from src.pipelines.prediction import PredictionPipeline
import numpy as np
import matplotlib.pyplot as plt
application = Flask(__name__)




app = application

@app.route("/",methods = ["GET","POST"])
def home():
   
    predictor = PredictionPipeline()
    predictor.load_model()
    if request.method == "GET":
        return render_template("index.html")
    else:
        data = request.json
        image_data = data["imageData"].split(",")[1]  # Extract base64 image data
        image_bytes = base64.b64decode(image_data)  # Decode image data
        img = Image.open(BytesIO(image_bytes))  # Open image using PIL
        # Preprocess image for prediction
        processed_image = preprocess_image(img)
        
        
        # Reshape the processed image to match the input shape of your model
        processed_image = processed_image.reshape(1, -1)  # Assuming your model expects a 1D array

        # Convert processed image to DataFrame
        df = pd.DataFrame(processed_image)
        
        df = predictor.preprocesses_data(df)
        image_resized = img.resize((28, 28))
    # Convert image to grayscale
        img_gray = image_resized.convert('L')
        img_gray = img_gray.convert('L')  # Convert image to grayscale
        img_gray.save("received_image_gray.png") 
        df = np.array(df).reshape(df.shape[0], 28, 28, 1)
       
        prediction = predictor.make_prediction(df)
        result = np.argmax(prediction[0])
        
        result = int(result)
       
        return jsonify(prediction=result)
        
      
        
        

    
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)     

