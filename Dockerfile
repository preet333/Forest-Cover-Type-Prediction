FROM python:3.8-slim

RUN apt update -y && apt-get update
WORKDIR /app

COPY . /app
RUN pip install --upgrade pip


RUN pip install -r requirements.txt
ARG TEST1
ARG TEST2
ENV AWS_ACCESS_KEY_ID=$TEST1
ENV AWS_SECRET_ACCESS_KEY=$TEST2

RUN python3 src/ForestCoverType/pipeline/training_pipeline.py
EXPOSE 5000
# CMD ["python3", "src/ForestCoverType/pipeline/training_pipeline.py"]
CMD ["python3", "webapp/app.py"]