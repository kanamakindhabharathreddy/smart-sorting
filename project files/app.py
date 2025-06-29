import os
import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)

# Define the path to the uploads folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define allowed extensions for image uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Load the custom trained model
model = None # Initialize model as None
try:
    MODEL_PATH = 'final_model.h5'
    model = load_model(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}!")
except Exception as e:
    print(f"ERROR: Model loading failed from {MODEL_PATH}: {e}")
    print("Model will be 'None'. Prediction requests will return an error message.")

# Define the image size for the model
IMG_HEIGHT = 150
IMG_WIDTH = 150

# Define your class names in the exact order your model predicts them.
CLASS_NAMES = [
    'Apple__Healthy', 'Apple__Rotten', 'Banana__Healthy', 'Banana__Rotten',
    'Bellpepper__Healthy', 'Bellpepper__Rotten', 'Carrot__Healthy', 'Carrot__Rotten',
    'Cucumber__Healthy', 'Cucumber__Rotten', 'Grape__Healthy', 'Grape__Rotten',
    'Guava__Healthy', 'Guava__Rotten', 'Jujube__Healthy', 'Jujube__Rotten',
    'Mango__Healthy', 'Mango__Rotten', 'Orange__Healthy', 'Orange__Rotten',
    'Pomegranate__Healthy', 'Pomegranate__Rotten', 'Potato__Healthy', 'Potato__Rotten',
    'Strawberry__Healthy', 'Strawberry__Rotten', 'Tomato__Healthy', 'Tomato__Rotten'
]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

# NEW: Route to render the preservation tips page
@app.route('/preservation')
def preservation():
    return render_template('preservation.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"success": False, "prediction": "Error: Model not loaded.", "confidence": 0}), 500

    if 'image' not in request.files:
        return jsonify({"success": False, "prediction": "No image file provided.", "confidence": 0}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"success": False, "prediction": "No selected file.", "confidence": 0}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        try:
            file.save(filepath)
        except Exception as e:
            return jsonify({"success": False, "prediction": f"Error saving image: {e}", "confidence": 0}), 500

        try:
            img = Image.open(filepath).convert('RGB').resize((IMG_WIDTH, IMG_HEIGHT))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            predictions = model.predict(img_array)
            predicted_class_index = np.argmax(predictions[0])
            confidence = float(np.max(predictions[0]) * 100)

            if 0 <= predicted_class_index < len(CLASS_NAMES):
                predicted_label_raw = CLASS_NAMES[predicted_class_index]
                parts = predicted_label_raw.split('__')
                predicted_label = f"{parts[0]} ({parts[1]})" if len(parts) == 2 else predicted_label_raw
            else:
                predicted_label = "Unknown Class"

            return jsonify({
                "success": True,
                "prediction": predicted_label,
                "confidence": confidence,
            }), 200

        except Exception as e:
            return jsonify({"success": False, "prediction": f"Error processing image: {e}", "confidence": 0}), 500
    else:
        return jsonify({"success": False, "prediction": "Invalid file type.", "confidence": 0}), 400

if __name__ == '__main__':
    app.run(debug=True)
