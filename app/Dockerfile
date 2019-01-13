FROM python:3.7
RUN apt-get update && apt-get install tk-dev && rm -r /var/lib/apt/lists/*
RUN pip3 install twitter
RUN pip3 install matplotlib
CMD ["python3","kinship-gui.py"]
WORKDIR /kinship
COPY . /kinship
