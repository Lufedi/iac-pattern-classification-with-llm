from factory.labelers.labeler import Labeler


class JavascriptLabeler(Labeler):
    def __init__(self) -> None:
        super().__init__()
        self.arch_styles = {
            "serverless": ["aws_lambda", "aws-lambda"],
            "microservices": ["aws_ecs",
                              "aws_eks",
                              "aws_eks_legacy",
                              "aws_ecr",
                              "aws-ecs",
                              "aws-eks",
                              "aws-eks-legacy",
                              "aws-ecr"],
            "big-data": ["aws_emr",
                         "aws_emrcontainers",
                         "aws_emrserverless",
                         "aws_dlm",
                         "aws_dms",
                         "aws-emr",
                         "aws-emrcontainers",
                         "aws-emrserverless",
                         "aws-dlm",
                         "aws-dms"
                         ],
            "event-driven": ["aws_sqs",
                             "aws_sns",
                             "aws_events"
                             "aws-sqs",
                             "aws-sns",
                             "aws-events"
                             ],
            "batch-processing": ["aws_batch", "aws-batch"],
            "iot": ["aws_iot", "aws-iot"],
            "streaming": ["aws_kinesis",
                          "aws_msk"
                          "aws-kinesis",
                          "aws-msk"
                          ],
            "nosql-storage": ["aws_docdb",
                            "aws_dynamodb",
                              "aws_docdbelastic",
                              "aws_memorydb"
                              "aws-docdb",
                             "aws-dynamodb",
                              "aws-docdbelastic",
                              "aws-memorydb"
                              ],
            "data-warehouse": [
                "aws_redshift",
                "aws-redshift",
                ],
            "data-orch": [
                "aws_datapipieline",
                "aws_datasync",
                "aws-datapipieline",
                "aws-datasync",
            ],
            "object-storage": [
                "aws_s3",
                "aws-s3",
            ]
        }

        self.extension = "js"
        self.default_expr = "aws-cdk-lib"



