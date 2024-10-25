# medical-chatbot-using-Llama2

* ### Step 1: Create virtual environment and activate it.
```bash
python3 -m venv ~/venv
source ~/venv/bin/activate
``` 

* ### Step 2: Install Requirements
```bash
pip install -r requirements.txt
```
* ### Step 3: Download model [ llama-2-7b-chat.ggmlv3.q4_1.bin ] from this [Link](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)


```bash
mkdir -p src research static templates
touch src/__init__.py
touch src/helper.py
touch src/prompt.py
touch .env
touch setup.py
touch research/trials.ipynb
touch app.py
touch store_index.py
touch static/.gitkeep
touch templates/chat.html
```