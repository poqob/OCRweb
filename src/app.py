from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from PIL import Image
import pytesseract

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# will save image
# will save result


@app.route('/', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']
    if file.filename == '':
        return 'No file selected'

    image = Image.open(file)
    text = pytesseract.image_to_string(image, lang='tur')

    return render_template('result.html', result=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
