FROM python:3.7

WORKDIR /app

COPY . .

ENTRYPOINT ["python", "app.py"]

CMD ["--length", "30", "--justify", "true", "--file", "input.txt"]