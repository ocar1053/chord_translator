class Scale:

    maj_scores = []
    tonic_tone = ""
    equal_temperament = ["C", "C#", "D", "D#",
                         "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    def __init__(self, name):
        self.tonic_tone = name
        self.generate_major_score()

    def generate_major_triad(self):
        for index, score in enumerate(self.maj_scores):
            root = score
            second = self.maj_scores[(index + 2) % 7]
            third = self.maj_scores[(index + 4) % 7]
            print(root, second, third)

    def generate_major_score(self):
        pattern_maj = [2, 2, 1, 2, 2, 2, 1]
        tonic_index = self.equal_temperament.index(self.tonic_tone)
        for i in range(0, len(pattern_maj)):
            self.maj_scores.append(self.equal_temperament[tonic_index])

            tonic_index += pattern_maj[i]
            tonic_index = tonic_index % 12

    def get_major_scores(self):
        for score in self.maj_scores:
            print(score, end=" ")
        print()
