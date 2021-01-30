import torch
from DetectionModelLabels import COCO_INSTANCE_CATEGORY_NAMES, MODEL_FILENAME
from VAR_CONST import VOLUME_SRC
import torchvision
from torchvision import transforms
from pathlib import Path
from skimage import io, transform


def get_transform():
    transform = transforms.Compose([
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225]),
        transforms.ToTensor()
    ])
    return transform


def image_prepare(img_path):
    img = io.imread(img_path)
    tensor = torch.from_numpy(img).permute(2, 0, 1).float() / 255
    print('Tensor type: ', type(tensor), ' Shape: ', tensor.shape)
    return tensor


class DetectionModel:
    indexToLabel = []
    model = None

    debug = False

    def __init__(self, debug=False):

        if debug:
            self.debug = True

        for ind, label in enumerate(COCO_INSTANCE_CATEGORY_NAMES):
            self.indexToLabel.append((ind, label))

        self.model = self.get_model()

        if self.model is None:
            raise Exception('Detection model is empty!')

    def predict(self, img_path):
        tensor = image_prepare(img_path)
        self.model.eval()
        result = self.model(tensor[None, :])
        print(result)
        return result

    def get_model(self):
        path = Path(VOLUME_SRC, MODEL_FILENAME)
        model = None

        if path.is_file():
            model = torch.load(path)
            model.eval()
        else:
            model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True, pretrained_backbone=True)
            print('Debug is: ', self.debug)
            if not self.debug:
                print('Try to save file to: ', path)
                torch.save(model, path)

        return model
