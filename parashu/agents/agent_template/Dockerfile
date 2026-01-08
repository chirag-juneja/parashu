FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ src/
COPY agent.yaml .

ENV PYTHONPATH=/app/src

CMD ["python", "-c", "import agent; print('Agent image ready')"]

