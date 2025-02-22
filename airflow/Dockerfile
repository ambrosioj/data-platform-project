FROM apache/airflow:2.5.0

USER root

# Install any additional dependencies here
RUN apt-get update && apt-get install -y \
    python3-pip \
    && pip3 install --no-cache-dir apache-airflow-providers-apache-spark

USER airflow

# Copy the Airflow configuration file
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

# Copy the DAGs
COPY dags/ ${AIRFLOW_HOME}/dags/ 

# Set the entrypoint for the Airflow scheduler and webserver
ENTRYPOINT ["/usr/bin/airflow"]
CMD ["webserver"]