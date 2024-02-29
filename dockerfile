FROM python:3.9.1
WORKDIR /code
COPY requirments.txt .
ENV PYTHONUNBUFFERED=1
RUN pip install -r requirments.txt
COPY quotes.py .
CMD [ "python", "./quotes.py" ]

