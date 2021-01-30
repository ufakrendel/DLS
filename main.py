import os

from DLSClasses.RecognizeFileData import RecognizeFileData
from DLSClasses.RecognizeStatusEnum import RecognizeStatusEnum
from DLSClasses.ResultBox import ResultBox
from DetectionModelLabels import COCO_INSTANCE_CATEGORY_NAMES
from ModelWorker import get_prediction
import redis
import pickle

from VAR_CONST import MEDIA_SRC, REDIS_HOST

REDIS_TTL = 20 * 60


# читаем с очереди и встаем в блокировку
def redis_check(redis_q):
    while True:
        file_object = read_from_queue(redis_q)
        # for debug
        file_object.print_file()

        img_file = os.path.join(MEDIA_SRC, 'media', file_object.file_name)
        # img_file = os.path.join('media', file_object.file_name)

        try:
            prediction = get_prediction(img_file)
            file_object.result = get_result_from_prediction(prediction[0])
            print('FileObjectResult: ', file_object.result)
            file_object.status = RecognizeStatusEnum.Ended
        except Exception as e:
            file_object.status = RecognizeStatusEnum.Error
            print(e)

        put_in_redis(redis_q, file_object)


def read_from_queue(redis_q):
    var = redis_q.brpop("queue", 0)
    file_object: RecognizeFileData = pickle.loads(var[1])
    return file_object


def put_in_redis(redis_q, file_object):
    file_data_bytes = pickle_file_data(file_object)
    redis_q.set(str(file_object.file_id), file_data_bytes, ex=REDIS_TTL)
    print('FileId: ', file_object.file_id)


def pickle_file_data(file_data: RecognizeFileData):
    file_data_bytes = pickle.dumps(file_data)
    return file_data_bytes


def get_result_from_prediction(prediction):
    result = []
    boxes = prediction['boxes'].detach()
    labels = prediction['labels'].detach().numpy().tolist()
    scores = prediction['scores'].detach().numpy().tolist()

    for i in range(len(boxes)):
        box_array = boxes[i].numpy().tolist()
        label_text = COCO_INSTANCE_CATEGORY_NAMES[labels[i]]
        box = ResultBox(box_array, label=labels[i], score=scores[i], label_text=label_text)
        result.append(box)
    return result


if __name__ == '__main__':
    print('Check started!')
    rds = redis.Redis(host=REDIS_HOST, port=6379, db=0, charset='utf-8')
    redis_check(rds)
