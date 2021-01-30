class ResultBox:
    box = []
    label = -1
    score = 0.
    label_text: str

    def __init__(self, box, label, score, label_text):
        self.box = box
        self.label = label
        self.score = score
        self.label_text = label_text

    def __str__(self):
        return 'Label: \'{}\', score: {:.2%}'.format(self.label_text, self.score)

