from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from PIL import Image
import pytesseract

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index2.html')


@app.route('/', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "no files uploaded :("
       # return render_template('no_file_uploaded.html')

    file = request.files['file']
    if file.filename == '':
        return "no files uploaded :("
        # return render_template('no_file_uploaded.html')

    image = Image.open(file)

    text = pytesseract.image_to_string(image, lang='tur')

    return text


@app.route('/result')
def result():
    data = request.args.get('data')
    return render_template('result.html', result=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
