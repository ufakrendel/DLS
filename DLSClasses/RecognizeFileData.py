import uuid

from DLSClasses.RecognizeStatusEnum import RecognizeStatusEnum
from DLSClasses.ResultBox import ResultBox


class RecognizeFileData:
    file_name = ''
    file_id = ''
    file_url = ''
    status: RecognizeStatusEnum = RecognizeStatusEnum.New
    result: [ResultBox] = []

    def __init__(self, file_name, file_url):
        self.file_name = file_name
        self.file_id = str(uuid.uuid1())
        self.file_url = str(file_url)

    def get_guid(self):
        return self.file_id

    def print_file(self):
        print('File name: {}, file_id: {}, file_url: {}, status: {}, result: {})'.format(self.file_name, self.file_id, self.file_url, self.status, self.result))
