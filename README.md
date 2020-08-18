# gpt2_generation
Quick app to generate text with gpt2

from python 3.6.2

install pytorch 
  pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

install requirements

run app with python app.py

# Usage

App starts and loads gpt-model and tokenizer.
the it asks you to give an input and continues the text with sampling the top 50 most likely outputs
give input q to stop or press ctrl-c
