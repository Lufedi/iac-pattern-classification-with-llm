import os
from factory.labelers.labeler import Labeler


class JavaLabeler(Labeler):

    def __init__(self) -> None:
        super().__init__()
        self.arch_styles = {
            "serverless": ["software.amazon.awscdk.services.lambda"],
            "microservices": ["software.amazon.awscdk.services.ecs",
                              "software.amazon.awscdk.services.eks",
                              "software.amazon.awscdk.services.ecr"],
            "big-data": ["software.amazon.awscdk.services.emr",
                         "software.amazon.awscdk.services.emrcontainers",
                         "software.amazon.awscdk.services.emrserverless",
                         "software.amazon.awscdk.services.dlm",
                         "software.amazon.awscdk.services.dms"],
            "event-driven": ["software.amazon.awscdk.services.sqs",
                             "software.amazon.awscdk.services.sns",
                             "software.amazon.awscdk.services.events"],
            "batch-processing": ["software.amazon.awscdk.services.batch"],
            "iot": ["software.amazon.awscdk.services.iot"],
            "streaming": ["software.amazon.awscdk.services.kinesis",
                          "software.amazon.awscdk.services.msk"],
            "nosql-storage": ["software.amazon.awscdk.services.docdb",
                            "software.amazon.awscdk.services.dynamodb",
                              "software.amazon.awscdk.services.docdbelastic",
                              "software.amazon.awscdk.services.memorydb"],
            "data-warehouse": [
                "software.amazon.awscdk.services.redshift",
                ],
            "data-orch": [
                "software.amazon.awscdk.services.datapipieline",
                "software.amazon.awscdk.services.datasync",
            ],
            "object-storage": [
                "software.amazon.awscdk.services.s3",
            ]
        }
        self.extension = "java"
        self.default_expr = "software.amazon.awscdk"
