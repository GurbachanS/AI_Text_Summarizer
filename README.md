# AI_Text_Summarizer

A web app that turns long text into a short, readable summary. Built with FastAPI and a T5 transformer model fine-tuned using Hugging Face Transformers and PyTorch, with a simple HTML/CSS/JavaScript frontend.

What it does
Open the web page and paste the text you want to summarize.
The backend preprocesses and tokenizes the text and runs it through the fine-tuned T5 model.
The generated summary is returned and shown on the page.

The project covers the full workflow: text preprocessing, tokenization, transformer fine-tuning, saving and loading the trained model, inference, and serving the model through a web interface.

Tech stack
Frontend: HTML, CSS, JavaScript
Backend: FastAPI, Uvicorn (Python)

Project structure
AI_Text_Summarizer/
├── app.py              FastAPI app: loads the model and serves the summarizer
├── templates/          HTML frontend
├── requirements.txt    Python dependencies
└── .gitignore

The fine-tuned model folder (my_t5_model/, ~233 MB) is not included in this repo because of GitHub's file size limits. See Get the model below for how to add it.

Setup (macOS)
1. Prerequisites
Python 3.10 or 3.11 recommended. Check your version with python3 --version. If your Mac's default python3 is a different version, use conda to get an isolated environment instead of changing your system Python.

If you don't have conda, install Miniconda first.

2. Clone and create an environment
bash
git clone https://github.com/GurbachanS/AI_Text_Summarizer.git
cd AI_Text_Summarizer

conda create -n text_summarizer python=3.11 -y
conda activate text_summarizer

You'll need to run conda activate text_summarizer again every time you open a new terminal tab to work on this project.

3. Install Python dependencies
bash
pip install --upgrade pip
pip install -r requirements.txt

PyTorch is a large download, so the first install can take a few minutes.

4. Get the model

The app loads the fine-tuned model from a folder named my_t5_model/ in the project root.

Option A: Download it. Get the model from [Hugging Face Hub link / Google Drive link] and place the folder in the project root as my_t5_model/.
Option B: Train it yourself. Fine-tune T5 on [dataset name], then save it into the project root:
python
  model.save_pretrained("my_t5_model")
  tokenizer.save_pretrained("my_t5_model")

Check that the folder is in place:

bash
ls my_t5_model

You should see config.json, the tokenizer files, and a weights file (model.safetensors or pytorch_model.bin).

5. Run the app
bash
conda activate text_summarizer
uvicorn app:app --reload --host 0.0.0.0 --port 8000
The web interface is at http://localhost:8000.
FastAPI's interactive API docs are at http://localhost:8000/docs.

The frontend is served by the same FastAPI app, so there is only one process to start.

6. Use it
Open http://localhost:8000 in your browser.
Paste the text you want to summarize into the input box.
Click Summarize.
The summary appears on the page.

Notes
The first request after starting the server can be slower because the model is being loaded into memory.
If you see an error like OSError or FileNotFoundError mentioning my_t5_model, the model folder is missing or misplaced. It must be in the project root, and you must start uvicorn from that same folder.
If port 8000 is already in use, start the app on another port, for example --port 8001, and open that port in your browser.
Inference for a model this size runs on CPU, so a GPU is not required.
my_t5_model/ is listed in .gitignore so the large weights are never committed by accident.
Future improvements
Deploy the app (for example on Hugging Face Spaces) with a public demo link
Add adjustable summary length controls
Add a ROUGE evaluation script and report the scores above
Support PDF/TXT file upload as input
Containerize the app with Docker
