# Development Container Project

This project sets up a development environment using Docker that includes Apache Spark, Apache Airflow, and Jupyter Notebooks. The following sections provide an overview of the project structure, setup instructions, and usage guidelines.

## Project Structure

```
dev-container-project
├── .devcontainer
│   ├── Dockerfile          # Instructions to build the Docker image
│   └── devcontainer.json   # Configuration for the development container
├── spark
│   └── spark-config.conf   # Configuration settings for Spark
├── airflow
│   ├── dags
│   │   └── example_dag.py  # Example Directed Acyclic Graph (DAG) for Airflow
│   └── airflow.cfg         # Configuration file for Airflow
├── notebooks
│   └── example_notebook.ipynb # Jupyter Notebook for analysis and documentation
├── docker-compose.yml       # Orchestration file for Docker services
└── README.md                # Project documentation
```

## Setup Instructions

1. **Clone the Repository**: 
   Clone this repository to your local machine.

   ```bash
   git clone <repository-url>
   cd dev-container-project
   ```

2. **Build the Development Container**: 
   Use the provided Dockerfile to build the development container.

   ```bash
   cd .devcontainer
   docker build -t dev-container .
   ```

3. **Start the Services**: 
   Use Docker Compose to start the services defined in `docker-compose.yml`.

   ```bash
   docker-compose up
   ```

4. **Access Jupyter Notebooks**: 
   Once the services are running, you can access Jupyter Notebooks in your web browser at `http://localhost:8888`.

## Usage Guidelines

- **Spark**: Use the configuration file `spark/spark-config.conf` to set up your Spark environment. Modify parameters as needed for your applications.
  
- **Airflow**: The example DAG can be found in `airflow/dags/example_dag.py`. You can create additional DAGs by following the structure of the example.

- **Notebooks**: Use the Jupyter Notebook located in `notebooks/example_notebook.ipynb` for data analysis and visualization.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.