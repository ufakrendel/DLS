from VAR_CONST import IS_DEBUG, MEDIA_SRC, VOLUME_SRC
from model import DetectionModel

model = DetectionModel(debug=False)


def get_prediction(img_path):


    prediction = model.predict(img_path)
    return prediction
