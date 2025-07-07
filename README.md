# 👗 Fashion MNIST Classifier Web App

This is a deep learning-based image classification web app that predicts clothing types from grayscale images using a CNN (Convolutional Neural Network). It is trained on the Fashion MNIST dataset and deployed using Flask.

Users can upload an image of a fashion item, and the app returns the predicted category (e.g., T-shirt, Sneaker, Bag). The project demonstrates how machine learning models can be made interactive using a web interface.

---

## 📊 About the Dataset

The [**Fashion MNIST**](https://github.com/zalandoresearch/fashion-mnist) dataset is a drop-in replacement for the original MNIST dataset, intended for benchmarking machine learning algorithms on more complex image classification problems.

- 👕 **Total Samples**: 70,000 grayscale images  
- 📏 **Image Size**: 28x28 pixels  
- 🔟 **Classes**: 10 fashion categories  
- 👨‍👩‍👧‍👦 **Split**: 60,000 for training, 10,000 for testing

### Categories:

| Label | Class        |
|-------|--------------|
| 0     | T-shirt/top  |
| 1     | Trouser      |
| 2     | Pullover     |
| 3     | Dress        |
| 4     | Coat         |
| 5     | Sandal       |
| 6     | Shirt        |
| 7     | Sneaker      |
| 8     | Bag          |
| 9     | Ankle boot   |

---

## 🧰 Tech Used

| Tool / Library         | Purpose                                      |
|------------------------|----------------------------------------------|
| **Python 3.x**         | Programming language                         |
| **TensorFlow / Keras** | Building and training the CNN model          |
| **Flask**              | Creating the web server and routes           |
| **Pillow (PIL)**       | Handling and preprocessing uploaded images   |
| **HTML / Jinja2**      | Frontend templates for UI                    |
| **NumPy**              | Numerical operations and array reshaping     |
| **Git & GitHub**       | Version control and collaboration            |
| **VS Code / Terminal** | Development environment                      |

---

### Clone the Repo

```bash
git clone https://github.com/Dhanush-Karthik16/fashion-mnist-flask.git
cd fashion-mnist-flask

# Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install Dependencies
pip install -r requirements.txt

# Run the Flask App
python app.py



