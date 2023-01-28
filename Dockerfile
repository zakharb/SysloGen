FROM python:slim

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY syslogen/ /app/syslogen
COPY example_file.txt /app/

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["python3", "/app/syslogen", "192.168.100.8", "-p", "514", "-i", "/app/example_file.txt", "-c", "1"] 
