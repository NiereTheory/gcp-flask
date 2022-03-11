FROM python:3.9
COPY . .
EXPOSE 8080
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]