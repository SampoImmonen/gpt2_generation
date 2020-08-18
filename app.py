import sys
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

sys.stdout.write("starting app\n")
tokenizer = GPT2Tokenizer.from_pretrained("distilgpt2")
sys.stdout.write("loading model\n")
model = GPT2LMHeadModel.from_pretrained("distilgpt2", pad_token_id=tokenizer.eos_token_id)
sys.stdout.write(35*'-'+'\n')
while True:
    text = input("give a piece of text to be continued press give q to break:\n")

    if text == 'q':
        break
    input_ids = tokenizer.encode(text, return_tensors='pt')
    sample_output = model.generate(
        input_ids, 
        do_sample=True,
        no_repeat_ngram_size=2, 
        max_length=50, 
        top_k=50
    )

    sys.stdout.write(35*'-'+'\n')
    sys.stdout.write(tokenizer.decode(sample_output[0], skip_special_tokens=True)+'\n')
    sys.stdout.write(35*'-'+'\n')
sys.stdout.write("ending program")