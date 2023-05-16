from factory.labelers.labeler import Labeler


class PythonLabeler(Labeler):
    def __init__(self) -> None:
        super().__init__()
        self.arch_styles = {
            "serverless": ["aws_lambda"],
            "microservices": ["aws_ecs",
                              "aws_eks",
                              "aws_eks_legacy",
                              "aws_ecr"],
            "big-data": ["aws_emr",
                         "aws_emrcontainers",
                         "aws_emrserverless",
                         "aws_dlm",
                         "aws_dms"],
            "event-driven": ["aws_sqs",
                             "aws_sns",
                             "aws_events"],
            "batch-processing": ["aws_batch"],
            "iot": ["aws_iot"],
            "streaming": ["aws_kinesis",
                          "aws_msk"],
            "nosql-storage": ["aws_docdb",
                            "aws_dynamodb",
                              "aws_docdbelastic",
                              "aws_memorydb"],
            "data-warehouse": [
                "aws_redshift",
                ],
            "data-orch": [
                "aws_datapipieline",
                "aws_datasync",
            ],
            "object-storage": [
                "aws_s3",
            ]
        }

        self.extension = "py"
        self.default_expr = "aws_cdk"



