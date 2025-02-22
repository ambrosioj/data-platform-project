FROM jupyter/scipy-notebook:latest

USER root

# Install PySpark
RUN pip install pyspark

# Install additional dependencies for Airflow
RUN pip install apache-airflow

USER $NB_UID

# Set the working directory
WORKDIR /home/jovyan/work

# Copy example notebook
COPY notebooks/example_notebook.ipynb /home/jovyan/work/notebooks/example_notebook.ipynb

# Expose the default Jupyter port
EXPOSE 8888

CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]