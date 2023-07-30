# Local Apache Spark Cluster using Docker

This report contains code and data required to run Apache Spark cluster locally using Docker.
It was inspired by [Apache Spark Official Dockerfiles](https://github.com/apache/spark-docker/tree/master)
and [Spark Cluster with Docker & docker-compose(2021 ver.)](https://github.com/mvillarrealb/docker-spark-cluster/tree/master)
repositories.


## Requirements

To run code from this repository you will need:

* [Docker with Docker Compose](https://docs.docker.com/desktop/install/fedora/) installed

### Resources

Each node configured to use 1 GB as driver/executor memory and 1 CPU core.
Theoretically should run okay on any machine nowadays.


## How To Run

Build Docker images:

```bash
docker build -t spark-base .
```

Run `docker compose`:

```bash
docker compose up -d
```

Open Spark UI URL's for master and worker nodes to check it's running:

* Master UI - http://127.0.0.1:9090
* Worder 1 UI - http://127.0.0.1:9091
* Worder 2 UI - http://127.0.0.1:9092

> Note that URLs on Spart master UI pointin to worker nodes will not work.
> They are all pointing to port `8080` which is not exposed.


## Stopping cluster

To stop cluster run:

```bash
docker compose stop
```

If you wish to not only stop containers but stop and remove containers, networks:

```bash
docker compose down
```

## Local Volumes

* `./apps` -> `/opt/spark-apps` to make you apps and code available on master and workers
* `./data` -> `/opt/spark-data` to make data available on master and workers

