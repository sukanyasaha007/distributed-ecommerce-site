FROM python:3

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt && \
    python -m grpc_tools.protoc \
        -I. \
        --python_out=. \
        --grpc_python_out=. \
        onlineshopping.proto

CMD [ "python", "./onlineshopping.py" ]