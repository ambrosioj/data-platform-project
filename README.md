# Docker Development Environment

This project sets up a development environment using Docker for working with Apache Spark, Apache Airflow, and Jupyter Notebooks. It allows you to develop Spark code, create Airflow DAGs, and run Jupyter notebooks seamlessly.

## Project Structure

```
docker-dev-environment
├── docker-compose.yml       # Defines services for Spark, Airflow, and Jupyter
├── spark                    # Directory for Spark-related files
│   ├── Dockerfile           # Dockerfile for building Spark image
│   └── config
│       └── spark-defaults.conf # Configuration file for Spark
├── airflow                  # Directory for Airflow-related files
│   ├── Dockerfile           # Dockerfile for building Airflow image
│   ├── dags                 # Directory for Airflow DAGs
│   │   └── example_dag.py   # Example DAG for Airflow
│   └── config
│       └── airflow.cfg      # Configuration file for Airflow
├── jupyter                  # Directory for Jupyter-related files
│   ├── Dockerfile           # Dockerfile for building Jupyter image
│   └── notebooks            # Directory for Jupyter notebooks
│       └── example_notebook.ipynb # Example Jupyter notebook
└── README.md                # Project documentation
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd docker-dev-environment
   ```

2. Build and start the services:
   ```
   docker-compose up --build
   ```

### Accessing the Services

- **Jupyter Notebook**: Access Jupyter at `http://localhost:8888` in your web browser.
- **Airflow**: Access the Airflow web interface at `http://localhost:8080`.
- **Spark**: Spark can be accessed through the Jupyter notebooks or via the Spark UI.

### Usage

- Use the provided Jupyter notebook (`example_notebook.ipynb`) to develop and test your Spark code.
- Create your own DAGs in the `airflow/dags` directory by modifying or adding new Python files.

## Contributing

Feel free to submit issues or pull requests for improvements or additional features.

## License

This project is licensed under the MIT License.