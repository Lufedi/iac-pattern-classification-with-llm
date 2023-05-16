


from factory.labelers.java_labeler import JavaLabeler
from factory.labelers.labeler import Labeler


class LabelerFactory():
    def create_labeler(self, language) -> Labeler:
        if language == "java":
            return JavaLabeler()
        else:
            return JavaLabeler()
