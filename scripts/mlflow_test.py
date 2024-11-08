# http://13.49.44.146:5000/

import mlflow
import random

#Set the mlflow tracking uri
mlflow.set_tracking_uri('http://16.171.181.123:5000/')

#start an mlflow run
with mlflow.start_run():
    mlflow.log_param("param1",random.randint(1,100))
    mlflow.log_param("param2",random.random())

    #Log some random metric
    mlflow.log_metric("metric1",random.random())
    mlflow.log_metric("metric2", random.uniform(0.5,1.5))

    print("Logged random params and metrics")