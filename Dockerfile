FROM python:3.12-alpine

WORKDIR /app
COPY requirements.txt src/ /app/

RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["streamlit", "run", "src/main.py", "--server.port=8080"]