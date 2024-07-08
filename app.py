from flask import Flask, request, render_template_string
import csv
from datetime import datetime

app = Flask(__name__)

# HTML template for the form with embedded CSS and JavaScript
form_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UME Potts Point Maintenance Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #1a1a1a;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            width: 100vw;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 500px;
            box-sizing: border-box;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-bottom: 5px;
            color: #555;
        }
        input[type="text"], textarea, select {
            margin-bottom: 15px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 3px;
            width: 100%;
            box-sizing: border-box;
        }
        input[type="submit"] {
            background-color: #28a745;
            color: #fff;
            border: none;
            padding: 10px;
            cursor: pointer;
            border-radius: 3px;
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
        .notification {
            text-align: center;
            margin-top: 10px;
            color: green;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>UME Potts Point Maintenance Form</h2>
        <form action="/submit" method="post">
            <label for="name">Resident's Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="room">Your Room Number:</label>
            <select id="room" name="room" required>
                <option value="">Select Room</option>
                <option value="Studio A">Studio A</option>
                <option value="Studio B">Studio B</option>
                <option value="01">Unit 1</option>
                <option value="02">Unit 2</option>
                <option value="03">Unit 3</option>
                <option value="04">Unit 4</option>
                <option value="05">Unit 5</option>
                <option value="06">Unit 6</option>
                <option value="07">Unit 7</option>
                <option value="08">Unit 8</option>
                <option value="09">Unit 9</option>
                <option value="10">Unit 10</option>
                <option value="11">Unit 11</option>
                <option value="12">Unit 12</option>
                <option value="13">Unit 13</option>
                <option value="14">Unit 14</option>
                <option value="15">Unit 15</option>
                <option value="16">Unit 16</option>
                <option value="17">Unit 17</option>
                <option value="18">Unit 18</option>
                <option value="19">Unit 19</option>
                <option value="20">Unit 20</option>
                <option value="21">Unit 21</option>
                <option value="22">Unit 22</option>
                <option value="23">Unit 23</option>
                <option value="24">Unit 24</option>
                <option value="25">Unit 25</option>
                <option value="26">Unit 26</option>
                <option value="27">Unit 27</option>
                <option value="28">Unit 28</option>
                <option value="29">Unit 29</option>
                <option value="30">Unit 30</option>
                <option value="31">Unit 31</option>
                <option value="32">Unit 32</option>
                <option value="33">Unit 33</option>
                <option value="34">Unit 34</option>
                <option value="35">Unit 35</option>
                <option value="36">Unit 36</option>
                <option value="37">Unit 37</option>
                <option value="38">Unit 38</option>
                <option value="39">Unit 39</option>
                <option value="40">Unit 40</option>
                <!-- Add more room options as needed -->
            </select>
            <label for="description">Description of Problem:</label>
            <textarea id="description" name="description" required></textarea>
            <label for="area">Area/Unit/Room:</label>
            <input type="text" id="area" name="area" required>
            <input type="submit" value="Submit">
        </form>
        <div class="notification" id="notification"></div>
    </div>
    <script>
        const form = document.querySelector('form');
        const notification = document.getElementById('notification');

        form.addEventListener('submit', async function(event) {
            event.preventDefault();
            
            const formData = new FormData(form);
            const response = await fetch('/submit', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                notification.textContent = 'Data submitted successfully!';
                form.reset();
                setTimeout(() => notification.textContent = '', 3000);
            } else {
                notification.textContent = 'Error submitting data. Please try again.';
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def form():
    return render_template_string(form_template)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    description = request.form['description']
    area = request.form['area']
    room = request.form['room']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Get current month and year
    current_month_year = datetime.now().strftime('%B_%Y')
    filename = f'{current_month_year}.csv'
    
    # Save the data to a CSV file
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['name', 'description', 'area', 'room', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header only once
        if csvfile.tell() == 0:
            writer.writeheader()
            
        writer.writerow({'name': name, 'description': description, 'area': area, 'room': room, 'timestamp': timestamp})
    
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)