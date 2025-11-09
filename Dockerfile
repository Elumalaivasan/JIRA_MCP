FROM python:3.12-slim
ARG PORT=8000
ENV PORT=$PORT
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD ["python", "main.py"]
