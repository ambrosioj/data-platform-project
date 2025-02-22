FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-jdk \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Spark
ENV SPARK_VERSION=3.2.1
ENV HADOOP_VERSION=3.2
RUN curl -sL "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | tar xz -C /opt/ && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark

# Set environment variables for Spark
ENV SPARK_HOME=/opt/spark
ENV PATH="$SPARK_HOME/bin:$PATH"

# Install Airflow
RUN pip install apache-airflow==2.2.0 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.2.0/constraints-3.9.txt"

# Install Jupyter Notebook
RUN pip install notebook

# Expose ports for Jupyter and Airflow
EXPOSE 8888 8080

# Set the working directory
WORKDIR /workspace

# Copy the project files into the container
COPY . /workspace

# Command to run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]