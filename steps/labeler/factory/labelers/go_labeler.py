from factory.labelers.labeler import Labeler


class GoLabeler(Labeler):
    def __init__(self) -> None:
        super().__init__()
        self.arch_styles = {
            "serverless": ["awslambda"],
            "microservices": ["awsecs",
                              "awseks",
                              "awsecr"],
            "big-data": ["awsemr",
                         "awsemrcontainers",
                         "awsemrserverless",
                         "awsdlm",
                         "awsdms",
                         ],
            "event-driven": ["awssqs",
                             "awssns",
                             "awsevents"
                             ],
            "batch-processing": ["awsbatch"],
            "iot": ["awsiot"],
            "streaming": ["awskinesis",
                          "awsmsk"
                          ],
            "nosql-storage": ["awsdocdb",
                            "awsdynamodb",
                              "awsdocdbelastic",
                              "awsmemorydb"
                              ],
            "data-warehouse": [
                "awsredshift",
                "awsredshift",
                ],
            "data-orch": [
                "awsdatapipieline",
                "awsdatasync",
            ],
            "object-storage": [
                "awss3",
            ]
        }

        self.extension = "go"
        self.default_expr = "awscdk"



