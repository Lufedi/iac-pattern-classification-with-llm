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
    def get_label(self, dirpath, file, language):
        results = {key: 0 for key in self.arch_styles}
        if file.endswith(".java"):
            file_path = os.path.join(dirpath, file)
            res, all_found, max_key = self.calculate_label(file_path)
            for key in self.arch_styles:
                results[key] += res[key]
            maxi_k, maxi_v = '', 0
            for key in results:
                if results[key] >= maxi_v:
                    maxi_k = key
                    maxi_v = results[key]
            if maxi_v == 0:
                is_service = self.search_str(file_path, "software.amazon.awscdk")
                if is_service: maxi_k = 'awsservice'
                else: maxi_k = 'unlabeled'
            print("saving", file_path)
            self.save_label(file_path, maxi_k, language)




