FROM python:3.10.7

WORKDIR C:\Users\takieddine.chikhamor\Desktop\Api_Flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]