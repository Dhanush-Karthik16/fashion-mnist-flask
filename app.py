from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image, ImageOps

app = Flask(__name__)
model = load_model("model.hdf5")

# Class names
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def prepare_image(image):
    image = ImageOps.grayscale(image)
    image = image.resize((28, 28))
    image = np.array(image) / 255.0
    image = image.reshape(1, 28, 28, 1)
    return image

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            image = Image.open(file.stream)
            img_prepped = prepare_image(image)
            prediction = model.predict(img_prepped)
            predicted_class = class_names[np.argmax(prediction)]
            return render_template('result.html', predicted_class=predicted_class)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
