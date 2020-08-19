# gpt2_generation
Quick app to generate text with distilgpt2

# Usage

App starts and loads gpt-model and tokenizer.
then it asks you to give an input and continues the text with sampling the top 50 most likely outputs
give input q to stop or press ctrl-c

## Note loading the distilgpt-2 model might take a while when the app is started
run the container with -it or else it fails
