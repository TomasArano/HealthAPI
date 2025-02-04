from flask import Flask, jsonify, request, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os

from utils import calculate_average_bpm_every_hour, calculate_hourly_range, calculate_time_per_activity


ALLOWED_EXTENSIONS = set(['xls', 'csv', 'txt'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/air/Desktop/BSC Projects/HealthAPI/UPLOADS'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1000 * 1000  # 500 MB
app.config['CORS_HEADER'] = 'application/json'

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

'''Test endpoints'''
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')
''''''

'''Upload Endpoint'''
@app.route('/upload', methods=['POST', 'GET'])
def fileUpload():
    if request.method == 'POST':
        files = request.files.getlist('file')  # Ensure the key matches the form data
        filename = ""
        for f in files:
            filename = secure_filename(f.filename)
            if allowedFile(filename):
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                return jsonify({'message': 'File type not allowed'}), 400
        return jsonify({"name": filename, "status": "success"})
    else:
        return jsonify({"status": "Upload API GET Request Running"})

'''Visualisation Endpoint: Average BPM every hour'''
@app.route('/averageBPM', methods=['GET'])
def get_hourly_average_data():
    data = calculate_average_bpm_every_hour()
    return jsonify(data)

@app.route('/rangeBPM', methods=['GET'])
def get_hourly_range_data():
    data = calculate_hourly_range()
    return jsonify(data)

@app.route('/timeActivity', methods=['GET'])
def get_time_per_activity():
    data = calculate_time_per_activity()
    return jsonify(data)

@app.route('/visualise', methods=['GET'])
def index():
    return render_template('index.html')


