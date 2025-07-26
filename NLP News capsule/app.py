from flask import Flask, render_template, request, jsonify
from summarization.extractive import summarize_extractive
from summarization.abstractive import summarize_abstractive

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('extractive.html')

@app.route('/extractive', methods=['GET', 'POST'])
def extractive():
    if request.method == 'POST':
        text = request.form.get('text', '')   # <-- changed!
        if not text:
            return render_template('error.html', error='Please provide text to summarize.')
        summary = summarize_extractive(text)
        return render_template('extractive.html', summary=summary)
    return render_template('extractive.html')

# @app.route('/abstractive', methods=['GET', 'POST'])
# def abstractive():
#     print(">>> /abstractive route was called")
#     if request.method == 'POST':
#         text = request.form.get('text', '')
#         length = int(request.form.get('length', 100))
#         lang = request.form.get('lang', 'en')
#         if not text:
#             return render_template('error.html', error='Please provide text to summarize.')
#         summary = summarize_abstractive(text, max_length=length, lang=lang)
#         print(">>> Rendering abstractive.html with summary:", summary)
#         return render_template('abstractive.html', summary=summary)
#     return render_template('abstractive.html')

@app.route('/abstractive', methods=['GET', 'POST'])
def abstractive():
    print(">>> /abstractive route was called")
    if request.method == 'POST':
        # print(">>> POST request received")
        text = request.form.get('text', '')
        # print(f">>> text: {text}")
        length = int(request.form.get('length', 100))
        # print(f">>> length: {length}")
        lang = request.form.get('lang', 'en')
        # print(f">>> lang: {lang}")
        if not text:
            # print(">>> No text submitted")
            return render_template('error.html', error='Please provide text to summarize.')
        summary = summarize_abstractive(text, max_length=length, lang=lang)
        # print(">>> Rendering abstractive.html with summary:", summary)
        return render_template('abstractive.html', summary=summary)
    # print(">>> GET request, just showing form")
    return render_template('abstractive.html')


@app.route('/api/summarize', methods=['POST'])
def api_summarize():
    data = request.get_json()
    text = data.get('text', '')
    method = data.get('method', 'extractive')
    length = int(data.get('length', 3 if method == 'extractive' else 100))
    lang = data.get('lang', 'en')
    if method == 'extractive':
        summary = summarize_extractive(text, num_sentences=length, lang=lang)
    else:
        summary = summarize_abstractive(text, max_length=length, lang=lang)
    return jsonify({'summary': summary})

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error='Page not found.'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error='Internal server error.'), 500

if __name__ == '__main__':
    app.run(debug=True)