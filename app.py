from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

def analyze_image(file_path):
    results = {}

    # Extract strings
    strings_output, _ = run_command(['strings', file_path])
    results['Strings'] = strings_output

    # Steghide
    steghide_output, _ = run_command(['steghide', 'extract', '-sf', file_path, '-p', ''])
    results['Steghide'] = steghide_output

    # Outguess
    outguess_output, _ = run_command(['outguess', '-r', file_path, 'outguess_output.txt'])
    results['Outguess'] = outguess_output

    # Binwalk
    binwalk_output, _ = run_command(['binwalk', file_path])
    results['Binwalk'] = binwalk_output

    # Exiftool
    exiftool_output, _ = run_command(['exiftool', file_path])
    results['Exiftool'] = exiftool_output

    # Foremost
    foremost_output, _ = run_command(['foremost', '-i', file_path])
    results['Foremost'] = foremost_output

    # Pngcheck
    pngcheck_output, _ = run_command(['pngcheck', '-v', file_path])
    results['Pngcheck'] = pngcheck_output

    # Metadata extraction (using exiftool for detailed metadata)
    metadata_output, _ = run_command(['exiftool', file_path])
    results['Metadata'] = metadata_output

    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        results = analyze_image(file_path)
        return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
