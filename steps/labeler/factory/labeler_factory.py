


from factory.labelers.java_labeler import JavaLabeler
from factory.labelers.python_labeler import PythonLabeler
from factory.labelers.javascript_labeler import JavascriptLabeler
from factory.labelers.typescript_labeler import TypescriptLabeler
from factory.labelers.go_labeler import GoLabeler
from factory.labelers.labeler import Labeler


class LabelerFactory():
    def create_labeler(self, language) -> Labeler:
        if language == "java":
            return JavaLabeler()
        elif language == "python":
            return PythonLabeler()
        elif language == "javascript":
            return JavascriptLabeler()
        elif language == "typescript":
            return TypescriptLabeler()
        elif language == "go":
            return GoLabeler()
        else:
            return JavaLabeler()
