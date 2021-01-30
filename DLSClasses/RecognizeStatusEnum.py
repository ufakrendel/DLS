from enum import Enum

class RecognizeStatusEnum(str, Enum):
    New = "NEW"
    InQueue = "IN_QUEUE"
    InWork = "IN_WORK"
    Ended = "ENDED"
    Error = "ERROR"
