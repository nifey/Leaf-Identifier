from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from Tester import Tester

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return Tester.test('static/img/'+filename,'hundred','data')
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
