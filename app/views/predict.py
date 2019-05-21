from flask import render_template, jsonify, request, Blueprint, current_app
from app import app
from app.extensions import db
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, login_required, current_user
from app.decorators import payment_required
import mimetypes, re
# Import Fastai Libraries
from fastai import *
from fastai.vision import *

predictbp = Blueprint('predictbp', __name__)

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
    return final

@predictbp.route('/predict')
@login_required
@payment_required
def predict():
    return render_template('predict.html', title='Predict')

@predictbp.route('/predict-api', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        if current_user.credits > 0: 
            basepath = current_app.config['UPLOAD_FOLDER']
            upload = request.files.items()
            paths = list()
            result = {}
            # Get the files from post request
            for key, f in upload:
                if key.startswith('file'):
                    file_path = os.path.join(basepath, secure_filename(f.filename))
                    if  re.match("image/*", mimetypes.guess_type(file_path)[0]):
                        paths.append(file_path)
                        f.save(file_path)
                    else:
                        return 'Error: Invalid File Type', 400 

            for file_path in paths:
                if current_user.credits > 0:
                    # Make prediction
                    preds = model_predict(file_path)
                    os.remove(file_path)
                    name = os.path.basename(file_path).split('.')[0]
                    result[name] = preds
                    current_user.credits -= 1

            db.session.commit()
            return json.dumps(result)
        else:
            return 'Error: Not Enough Credits', 400
    return 'OK'