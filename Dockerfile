FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY model_lightbm.pkl .
COPY main.py .
ENTRYPOINT ["python", "main.py"]
