FROM python:3.11-alpine
WORKDIR /app
COPY app/ /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "server.py"]