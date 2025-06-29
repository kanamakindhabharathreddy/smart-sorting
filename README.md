<<<<<<< HEAD
# SmartSort: AI-Powered Freshness Detection

=======
# Smart Sorting – Transfer Learning for Identifying Rotten Fruits and Vegetables
SmartSort: AI-Powered Freshness Detection
SmartSort is an intelligent web application that uses deep learning to classify the freshness of fruits and vegetables from an image. It instantly tells you if your produce is "Healthy" or "Rotten" and provides helpful, AI-generated content like recipes, preservation tips, and fun facts to help you reduce food waste and make the most of your fresh ingredients.

This project was developed by K. Bharath Reddy, N. Mohan Reddy, and G. Murali as part of the SmartInternz AI/ML Virtual Internship Program.

<<<<<<< HEAD
---

## ✨ Features

- **AI-Powered Freshness Detection:** Upload an image and get an instant prediction on whether your fruit or vegetable is fresh or rotten, complete with a confidence score.
- **Dynamic UI with Fun Animations:** A premium user interface with a "frosted glass" design, 3D card tilt effects, and celebratory animations like confetti for "Healthy" results.
- **Gemini-Powered Content Generation:**
  - **Get Recipes:** For any fresh produce, get three creative recipe ideas, complete with ingredients and instructions.
  - **Get Preservation Tips:** For any produce (fresh or rotten), get tips on how to store it correctly to extend its life.
  - **Fun Facts:** Get a surprising and fun fact about the detected produce.
- **Dedicated Recipe & Tips Pages:** View your generated recipes and tips on beautifully styled, dedicated pages.
- **Responsive Design:** A seamless experience on desktop, tablet, and mobile devices.

---

## 🛠️ Technology Stack

- **Backend:** Python, Flask
- **Deep Learning:** TensorFlow, Keras
- **Frontend:** HTML5, Tailwind CSS, JavaScript
- **Generative AI:** Google Gemini API
- **Core Libraries:** NumPy, Pillow
- **Development Tools:** Jupyter Notebook, VS Code, Git

---

## 🚀 Setup and Installation

To run this project on your local machine, please follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/kanamakindhabharathreddy/smart-sorting.git
   cd smart-sorting
   ```
2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   # Activate it
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Add Your API Key:**
   - Get your key from Google AI Studio.
   - Open the `index.html` file in a text editor.
   - Find the `getGeminiContent` function and replace `"YOUR_GEMINI_API_KEY_HERE"` with your actual key. **Do not commit this key to your public repository.**
5. **Run the Flask Application:**
   ```bash
   python app.py
   ```
   The application will now be running at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 📖 Usage

1. Open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).
2. Click the "Start Predicting" button to open the prediction modal.
3. Upload an image of a fruit or vegetable by clicking the upload area or by dragging and dropping a file.
4. The AI will analyze the image and display the result.
5. If the item is "Healthy," you will have options to get recipes and preservation tips. For any result, you can get a fun fact.
6. Clicking "Get Recipes" or "Get Preservation Tips" will redirect you to a new page with the generated content.

---

## 📂 Project Structure

```
=======
✨ Features
AI-Powered Freshness Detection: Upload an image and get an instant prediction on whether your fruit or vegetable is fresh or rotten, complete with a confidence score.

Dynamic UI with Fun Animations: A premium user interface with a "frosted glass" design, 3D card tilt effects, and celebratory animations like confetti for "Healthy" results.

Gemini-Powered Content Generation:

Get Recipes: For any fresh produce, get three creative recipe ideas, complete with ingredients and instructions.

Get Preservation Tips: For any produce (fresh or rotten), get tips on how to store it correctly to extend its life.

Fun Facts: Get a surprising and fun fact about the detected produce.

Dedicated Recipe & Tips Pages: View your generated recipes and tips on beautifully styled, dedicated pages.

Responsive Design: A seamless experience on desktop, tablet, and mobile devices.

🛠️ Technology Stack
Backend: Python, Flask

Deep Learning: TensorFlow, Keras

Frontend: HTML5, Tailwind CSS, JavaScript

Generative AI: Google Gemini API

Core Libraries: NumPy, Pillow

Development Tools: Jupyter Notebook, VS Code, Git

🚀 Setup and Installation
To run this project on your local machine, please follow these steps:

1. Clone the Repository:

Open your terminal or Git Bash and run the following command:

git clone https://github.com/kanamakindhabharathreddy/smart-sorting.git
cd smart-sorting

2. Create a Virtual Environment (Recommended):

It's best practice to create a virtual environment to manage project dependencies.

# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies:

The required Python libraries are listed in the requirements.txt file. Install them with pip:

pip install -r requirements.txt

4. Add Your API Key:

You will need a Google Gemini API key for the recipe, tips, and fun fact features to work.

Get your key from Google AI Studio.

Open the index.html file in a text editor.

Find the getGeminiContent function and replace "YOUR_GEMINI_API_KEY_HERE" with your actual key. Do not commit this key to your public repository.

5. Run the Flask Application:

Once the dependencies are installed, you can start the Flask server:

python app.py

The application will now be running at http://127.0.0.1:5000.

usage
Open your web browser and go to http://127.0.0.1:5000.

Click the "Start Predicting" button to open the prediction modal.

Upload an image of a fruit or vegetable by clicking the upload area or by dragging and dropping a file.

The AI will analyze the image and display the result.

If the item is "Healthy," you will have options to get recipes and preservation tips. For any result, you can get a fun fact.

Clicking "Get Recipes" or "Get Preservation Tips" will redirect you to a new page with the generated content.

📂 Project Structure
>>>>>>> 9dd5ef9bcdda55c757f298fafe4e31cba6aa398e
smart-sorting/
│
├── app.py                  # The main Flask application file
├── train_model.py          # Script for training the TensorFlow model
├── class_indices.json      # Maps model prediction indices to class names
├── final_model.h5          # The trained Keras model file
│
├── templates/
│   ├── index.html          # Main landing page
│   ├── recipes.html        # Page to display generated recipes
│   └── preservation.html   # Page to display preservation tips
│
├── static/
│   └── uploads/            # Folder where uploaded images are temporarily stored
│
├── dataset/
│   ├── train/
│   └── test/
│
└── README.md               # This file
<<<<<<< HEAD
```

---

## 🔮 Future Scope

- **Expand the Model:** Train the model on more produce categories, including leafy greens and a wider variety of fruits.
- **Real-Time Video Analysis:** Implement a feature to use a device's camera for live, real-time freshness detection.
- **Nutritional Information:** Add a feature to get detailed nutritional facts for the detected produce via the Gemini API.
- **Cloud Deployment:** Deploy the application to a cloud platform like Render or AWS for public access.

=======

🔮 Future Scope
Expand the Model: Train the model on more produce categories, including leafy greens and a wider variety of fruits.

Real-Time Video Analysis: Implement a feature to use a device's camera for live, real-time freshness detection.

Nutritional Information: Add a feature to get detailed nutritional facts for the detected produce via the Gemini API.

Cloud Deployment: Deploy the application to a cloud platform like Render or AWS for public access.
>>>>>>> 9dd5ef9bcdda55c757f298fafe4e31cba6aa398e
