from flask import request, jsonify, render_template
from .summarizer import summarize_text
from flask import current_app as app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text')
    summary = summarize_text(text)
    return jsonify({'summary': summary})
