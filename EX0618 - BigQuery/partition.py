import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'D:\\Study\\Python\\EX0618 - BigQuery\\att-bda-d9fe216e6997.json'
client = bigquery.Client(project = 'att-bda')
dataset_ref = client.dataset('dw')
table_ref = dataset_ref.table('AES_MAPDATA')
map_file = 'D:\\Study\\Python\\EX0618 - BigQuery\\map2.json'


try:
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    job_config.autodetect = False
    job_config.time_partitioning = bigquery.TimePartitioning(        
        field="endtime",  # name of column to use for partitioning
    )
    with open(map_file, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
        job.result()  # Waits for table load to complete.
    print("upload succeeded")
except:
    print("upload failed")