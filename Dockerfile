FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install build-essential -y

COPY dagster/requirements.txt .

RUN pip install -r requirements.txt

ENV DAGSTER_HOME=/opt/dagster

RUN mkdir -p ${DAGSTER_HOME}

COPY dagster/dagster.yaml dagster/workspace.yaml ${DAGSTER_HOME}

COPY dbt_project /app/dbt_project/

COPY dagster/dagster.yaml dagster/workspace.yaml /app/

EXPOSE 3000

CMD [ "dagster-webserver", "-h", "0.0.0.0", "-p", "3000", "-w", "workspace.yaml" ]
