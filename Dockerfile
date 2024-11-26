FROM tensorflow/tensorflow:latest
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --upgrade pip setuptools
RUN pip uninstall -y blinker || true \
    && pip install --no-cache-dir --ignore-installed -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]