FROM eclipse-temurin:11.0.20_8-jre AS ground

ARG spark_ver=3.4.1
ARG spark_uid=185

# Create a spark group and user
RUN groupadd --system --gid=${spark_uid} spark && \
    useradd --system --uid=${spark_uid} --gid=spark spark

# Install required OS packages
RUN set -ex; \
    apt-get update; \
    apt-get install -y gnupg2 wget bash python3 python3-pip python3-numpy python3-matplotlib python3-pandas; \
    mkdir -p /opt/spark; \
    mkdir /opt/spark/python; \
    mkdir /opt/spark/work; \
    chown -R spark:spark /opt/spark; \
    rm -rf /var/lib/apt/lists/*;

# Install Apache Spark
RUN set -ex; \
    export SPARK_TMP="$(mktemp -d)"; \
    cd $SPARK_TMP; \
    wget -nv -O spark.tgz https://dlcdn.apache.org/spark/spark-${spark_ver}/spark-${spark_ver}-bin-hadoop3.tgz; \
    # TODO(max.ligus): add check of GPG signature???
    tar -xf spark.tgz --strip-components=1; \
    chown -R spark:spark .;\
    mv jars /opt/spark/; \
    mv bin /opt/spark/; \
    mv sbin /opt/spark/; \
    mv kubernetes/dockerfiles/spark/decom.sh /opt/; \
    mv examples /opt/spark/; \
    mv kubernetes/tests /opt/spark/; \
    mv data /opt/spark/; \
    mv python/pyspark /opt/spark/python/pyspark/; \
    mv python/lib /opt/spark/python/lib/; \
    mv R /opt/spark/; \
    chmod a+x /opt/decom.sh; \
    cd ..; \
    rm -fr "$SPARK_TMP";

FROM ground AS apache-spark

ENV SPARK_HOME=/opt/spark

WORKDIR /opt/spark

USER spark
