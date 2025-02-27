from flask import Flask, jsonify, request, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os

from utils import calculate_average_bpm_every_hour, calculate_hourly_range, calculate_time_per_activity
from converter import convert_xml_to_csv

ALLOWED_EXTENSIONS = set(['xls', 'csv', 'txt'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'UPLOADS')
app.config['MAX_CONTENT_LENGTH'] = 500 * 1000 * 1000  # 500 MB
app.config['CORS_HEADER'] = 'application/json'

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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

'''Convert XML to CSV Endpoint'''

@app.route('/convert', methods=['POST'])
def convert_xml():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and file.filename.endswith('.xml'):
        xml_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(xml_path)
        
        try:
            csv_path = convert_xml_to_csv(xml_path)
            return jsonify({'success': True, 'csv_path': csv_path}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'File must be XML format'}), 400