# pip install ollama
import ollama

MODEL = "llama3.1"
MESSAGE = "Warum ist der Himmel blau?"

# llama3.1
ollama.pull(MODEL)
stream = ollama.chat( model=MODEL, messages=[{"role": "user", "content": MESSAGE}], stream=True )

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
