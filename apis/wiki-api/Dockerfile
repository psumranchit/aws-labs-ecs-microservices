FROM python:3.7-alpine
COPY req.txt /
RUN pip install -r /req.txt
COPY *.py .
CMD [ "python", "./app.py" ]
EXPOSE 5000
