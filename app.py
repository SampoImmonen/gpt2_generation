import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
print("starting app")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
print("loading model")
model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)
print(35*'-')
while True:
    text = input("give a piece of text to be continued press give q to break:\n")

    if text == 'q':
        break
    input_ids = tokenizer.encode(text, return_tensors='pt')
    sample_output = model.generate(
        input_ids, 
        do_sample=True, 
        max_length=50, 
        top_k=50
    )

    print(35*'-')
    print(tokenizer.decode(sample_output[0], skip_special_tokens=True))
    print(35*'-')
print("ending program")