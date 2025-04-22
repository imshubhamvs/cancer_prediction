
# Cancer Prediction Project

This project predicts the likelihood of cancer based on various health factors such as age, gender, BMI, smoking habits, genetic risk, physical activity, alcohol intake, and cancer history. It uses a Random Forest classifier trained on a dataset and exposes the prediction model via a FastAPI backend. The front-end is a simple web application where users can input their data to get predictions.

## File Structure

```
D:\Projects\cance\
│
├── dataset.csv                # Dataset for training the model
├── index.html                 # Frontend HTML page for user input
├── main.py                    # FastAPI backend for serving the model
├── random_forest_model.joblib # Trained Random Forest model
├── scaler.joblib              # Scaler for normalizing the data
├── script.js                  # JavaScript for handling frontend logic and API 
├── styles.css                 # CSS for styling the frontend
├── train.py                   # Python script to train the Random Forest model
└── __pycache__                # Python bytecode files (auto-generated)
```

## Steps to Run the Project

### 1. Clone the Project

Start by cloning this project to your local machine:

```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Train the Model

Before starting the backend API, you need to train the model with the dataset provided in `dataset.csv`.

1. Open the `train.py` file and run the script to train the model and save it:
   
   ```bash
   python train.py
   ```

   This will generate two files:
   - `random_forest_model.joblib`: The trained model.
   - `scaler.joblib`: The scaler used to normalize the data before feeding it to the model.

### 3. Install Dependencies

Install the required Python dependencies using `pip`:

```bash
pip install pandas scikit-learn joblib fastapi uvicorn numpy pydantic
```

### 4. Set Up the API Backend

1. Start the backend API by running the `main.py` script:

   ```bash
   python main.py
   ```

   This will start a FastAPI server running on `http://127.0.0.1:8000`. The backend is responsible for serving the trained model and handling prediction requests.

### 5. Set Up the Frontend

1. Open `index.html` in a code editor of your choice (such as VS Code).
2. Make sure the HTML, CSS, and JavaScript are correctly linked and the API is accessible via the correct URL.

### 6. Open the Frontend

To view and interact with the application, open the `index.html` file in a live server (for example, using the Live Server extension in VS Code) or directly in your browser:

1. Right-click `index.html` in your editor and choose "Open with Live Server" (if using VS Code).
2. Alternatively, open `index.html` directly in your browser.

### 7. Interact with the Application

Once the FastAPI server is running and the frontend is opened, you can:

- Input values for `Age`, `Gender`, `BMI`, `Smoking`, `GeneticRisk`, `PhysicalActivity`, `AlcoholIntake`, and `CancerHistory` into the form on the webpage.
- Submit the form to send a POST request to the FastAPI backend.
- View the prediction result displayed on the page ("Cancer" or "No Cancer").

## Dependencies

- **pandas**: Data manipulation and CSV file reading.
- **scikit-learn**: For training the Random Forest model and scaling the data.
- **joblib**: For saving and loading the trained model and scaler.
- **fastapi**: For the API to serve the model.
- **uvicorn**: To run the FastAPI application.
- **numpy**: To handle numerical operations for predictions.
- **pydantic**: For input data validation in the FastAPI app.

## Files Explanation

- **train.py**: This script trains the Random Forest model on the dataset and saves the model and scaler.
- **main.py**: The FastAPI server that serves the trained model and makes predictions based on user input.
- **index.html**: The frontend HTML page where users enter their data for prediction.
- **script.js**: Handles frontend logic, including submitting the form and interacting with the FastAPI backend.
- **styles.css**: CSS styles for the frontend page.
- **random_forest_model.joblib**: The saved Random Forest model after training.
- **scaler.joblib**: The saved scaler used for normalizing input data before making predictions.

## API Endpoints

- **POST /predict**: Accepts a POST request with the following JSON data and returns a prediction (`Cancer` or `No Cancer`):
  
  ```json
  {
    "Age": float,
    "Gender": int,    // 0 for female, 1 for male
    "BMI": float,
    "Smoking": int,   // 0 for non-smoker, 1 for smoker
    "GeneticRisk": int, // 0 for low risk, 1 for high risk
    "PhysicalActivity": float,
    "AlcoholIntake": float,
    "CancerHistory": int // 0 for no history, 1 for history
  }
  ```

## License

This project is open source. Feel free to modify and use it according to your needs.

