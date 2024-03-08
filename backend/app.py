from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    if file:
        # Save the uploaded file to a folder
        # Adjust the folder path as needed
        upload_folder = os.path.join(os.getcwd(), 'uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)
        
        # Perform further processing on the uploaded file
        # For demonstration purposes, just return the file name
        return 'File uploaded: {}'.format(file.filename)

if __name__ == '__main__':
    app.run(debug=True)
