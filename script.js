document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get values from the form
    const formData = {
        Age: document.getElementById('Age').value,
        Gender: document.getElementById('Gender').value,  // Value will be either '0' or '1'
        BMI: document.getElementById('BMI').value,
        Smoking: document.getElementById('Smoking').value,  // Value will be either '0' or '1'
        GeneticRisk: document.getElementById('GeneticRisk').value,  // Value will be either '0' or '1'
        PhysicalActivity: document.getElementById('PhysicalActivity').value,  // from dropdown
        AlcoholIntake: document.getElementById('AlcoholIntake').value,  // from dropdown
        CancerHistory: document.getElementById('CancerHistory').value,  // Value will be either '0' or '1'
    };

    // Show the loader while waiting for the API response
    document.getElementById('loader').style.display = 'block';
    document.getElementById('result').innerText = '';  // Clear previous result

    // Send POST request to the FastAPI server
    fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        
        // Hide the loader and show the result
        document.getElementById('loader').style.display = 'none';
        document.getElementById('result').innerText = `Prediction: ${data.Prediction}`;
    })
    .catch(error => {
        
        // Hide the loader and show error message
        document.getElementById('loader').style.display = 'none';
        document.getElementById('result').innerText = 'Error: Unable to fetch prediction. Please try again.';
    });
});
