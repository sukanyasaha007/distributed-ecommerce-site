FROM python:3

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
ENV PORT=8080
EXPOSE 8080
CMD [ "python", "./server.py" ]