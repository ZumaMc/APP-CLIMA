FROM Python:3.13.0
WORKDIR /Clima1
COPY . /Clima1/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "Clima1.py"]
