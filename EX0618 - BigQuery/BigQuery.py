import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'D:\\Study\\Python\\EX0618 - BigQuery\\att-bda-d9fe216e6997.json'
client = bigquery.Client(project = 'att-bda')
dataset_ref = client.dataset('dw')
table_ref = dataset_ref.table('AES_MAPDATA')
#
table = bigquery.Table(table_ref)
table.time_partitioning = bigquery.TimePartitioning(
    type_=bigquery.TimePartitioningType.DAY,
    field="endtime",  # name of column to use for partitioning
    expiration_ms=5184000000,
)

map_file = 'D:\\Study\\Python\\EX0618 - BigQuery\\map2.json'

"""
query = "call dw.PROC_TEST('2020-06-03','2020-06-18')"
job = client.query(query)

for result in job.result():
    print("{} is Year {} and Week {}.".format(result['STARTDATE'],result['LYEAR'],result['WEEK']))
    
"""

try:
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    job_config.autodetect = False
    with open(map_file, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
        job.result()  # Waits for table load to complete.
    print("upload succeeded")
except:
    print("upload failed")
   
