FROM python:3.6.8

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/SampoImmonen/gpt2_generation

WORKDIR gpt2_generation
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt

CMD python app.py