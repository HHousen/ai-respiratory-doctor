from flask import render_template, jsonify, request
from app import app
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, login_required, current_user
from app.decorators import payment_required
# Import Fastai Libraries
from fastai import *
from fastai.vision import *

NAME_OF_FILE = 'export.pkl' # Name of your exported file
PATH_TO_MODELS_DIR = Path('models') # by default just use /models in root dir

defaults.device = torch.device('cpu')
learn = load_learner(PATH_TO_MODELS_DIR, fname=NAME_OF_FILE)

def model_predict(img_path):
    img = open_image(img_path)
    pred_class,pred_idx,outputs = learn.predict(img)
    model_results = outputs.numpy().tolist()
    model_results_percent = [i * 100 for i in model_results]
    classes = learn.data.classes
    final = dict(zip(classes, model_results_percent))
    return json.dumps(final)

@app.route('/predict-api', methods=['GET', 'POST'])
@login_required
@payment_required
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = app.config['UPLOAD_FOLDER']
        file_path = os.path.join(basepath, secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path)
        os.remove(file_path)
        return preds
    return 'OK'