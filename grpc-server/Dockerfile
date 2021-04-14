FROM python:3

WORKDIR /app
COPY . .
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt && \
    python -m grpc_tools.protoc \
        -I. \
        --python_out=. \
        --grpc_python_out=. \
        onlineshopping.proto
        

CMD [ "python", "./onlineshopping.py" ]