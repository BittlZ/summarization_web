from flask import request, jsonify, render_template
from .sumy_algorithm import summarize_text
from flask import current_app as app
from werkzeug.utils import secure_filename
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarizee():
    data = request.json
    text = data.get('text')
    num_sentences = data.get('num_sentences', 1)
    method = data.get('method', 'lsa')
    weights_path = data.get('weights_path', None)
    

    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Проверка на наличие и правильность значения num_sentences
    try:
        num_sentences = int(num_sentences)
    except (ValueError, TypeError):
        num_sentences = 1
    
    summary = summarize_text(text, num_sentences, method, weights_path)
    if summary is None:
        return jsonify({'error': 'Error during summarization'}), 500
    
    return jsonify({'summary': [str(sentence) for sentence in summary]})



@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join('uploads', filename)
        file.save(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        return jsonify({'text': text})

@app.route('/upload_weights', methods=['POST'])
def upload_weights():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join('uploads', filename)
        file.save(filepath)
        return jsonify({'weights_path': filepath})
