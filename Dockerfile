FROM python:3.8
WORKDIR /calc
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /calc
CMD ["python", "./calculator.py"]