# Local Apache Spark Cluster using Docker

This report contains code and data required to run Apache Spark cluster locally using Docker.
It was inspired by [Apache Spark Official Dockerfiles](https://github.com/apache/spark-docker/tree/master)
and [Spark Cluster with Docker & docker-compose(2021 ver.)](https://github.com/mvillarrealb/docker-spark-cluster/tree/master)
repositories.

We will be running Spark in [standalone mode](https://spark.apache.org/docs/latest/spark-standalone.html).

Main idea behind this is to be enable:

* learning Spark
* have somewhat close to real world environment
* testing of Spark jobs locally
* ...

Majority of `Dockerfile` is composed based on Apache Spark's [`Dockerfile`](https://github.com/apache/spark-docker/blob/master/Dockerfile.template)
template.


## Requirements

To run code from this repository you will need:

* [Docker with Docker Compose](https://docs.docker.com/desktop/install/fedora/) installed


### Resources

By default, each node configured to use:

* 1 GB RAM
* 1 CPU core

Theoretically should run okay on any machine nowadays.
Feel free to play and update node config in `docker-compose.yml`.


## Run Cluster Locally

Build Docker image:

```bash
docker build -t spark-base .
```

Run `docker compose` to start cluster:

```bash
docker compose up -d
```

Open Spark UI URL's for master and worker nodes to check it's running:

* Master   - http://127.0.0.1:8080
* Worker 1 - http://127.0.0.1:8081
* Worker 2 - http://127.0.0.1:8082


## Stop Cluster

To stop cluster either stop containers:

```bash
docker compose stop
```

or if you wish to not only stop containers but stop and remove containers, networks:

```bash
docker compose down
```

## Local Volumes

* `./apps` -> `/opt/spark-apps` to make you apps and code available on master and workers
* `./data` -> `/opt/spark-data` to make data available on master and workers


## Running Spark application

Examples are taken from [Apache Spark](https://github.com/apache/spark/tree/master/examples/src/main) official repo.


###  Calculate Pi

Connect to master or worker in interactive mode. Here we connect interactively to master node:

```bash
docker container exec -it spark-master /bin/bash
```

Execute Spark app:

```bash
/opt/spark/bin/spark-submit --master spark://spark-master:7077 \
                            --driver-memory 1G \
                            --executor-memory 1G \
                            /opt/spark/user-apps/pi.py
```

Or run the same example from Spark codebase:

```bash
cd /opt/spark
./bin/spark-submit examples/src/main/python/pi.py 10
```

Or Java or Scala application:

```
./bin/run-example SparkPi 10
```


## Next Steps (aka ToDo)

* catch bugs and improve `Dockerfile` and Compose file
* try running [Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html)


## Useful Links

* [Spark Overview](https://spark.apache.org/docs/latest/)
* [Spark Cluster Mode Overview](https://spark.apache.org/docs/latest/cluster-overview.html)
* [Spark Standalone Mode](https://spark.apache.org/docs/latest/spark-standalone.html)
