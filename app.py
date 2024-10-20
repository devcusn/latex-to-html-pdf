from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return send_file('views/index.html')


@app.route('/pdf')
def showPDF():
    return send_file('views/pdf.html')


@app.route('/api/v1/get-report', methods=['GET'])
def get_report():
    latex_file = 'file.tex'
    output_file_html = latex_file.replace('.tex', '.html')

    try:
        # Generate HTML from LaTeX
        subprocess.run(['pandoc', latex_file, '-o',
                        output_file_html, '--mathml', '--standalone'], check=True)

        with open(output_file_html, 'r', encoding='utf-8') as f:
            html_content = f.read()

        return html_content, 200, {'Content-Type': 'text/html'}
    except subprocess.CalledProcessError:
        return jsonify({"error": "Conversion to HTML failed"}), 500


@app.route('/api/v1/get-pdf', methods=['GET'])
def get_pdf():
    latex_file = 'file.tex'
    output_file_pdf = latex_file.replace('.tex', '.pdf')
    try:
        subprocess.run(['pandoc', latex_file, '-o',
                        output_file_pdf, '--pdf-engine=pdflatex'], check=True)

        return send_file(output_file_pdf, as_attachment=True)
    except subprocess.CalledProcessError:
        return jsonify({"error": "Conversion to PDF failed"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4003)
