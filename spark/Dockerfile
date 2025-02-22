FROM openjdk:8-jdk-slim

# Set environment variables for Spark
ENV SPARK_VERSION=3.1.2
ENV HADOOP_VERSION=3.2
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Download and extract Spark
RUN wget -q https://downloads.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz -O /tmp/spark.tgz \
    && mkdir -p $SPARK_HOME \
    && tar -xzf /tmp/spark.tgz --strip-components=1 -C $SPARK_HOME \
    && rm /tmp/spark.tgz

# Copy Spark configuration
COPY config/spark-defaults.conf $SPARK_HOME/conf/

# Set working directory
WORKDIR $SPARK_HOME

# Expose Spark ports
EXPOSE 7077 8080

# Command to run Spark
CMD ["spark-submit", "--version"]