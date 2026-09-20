# AI Text Summarizer

A web application that converts long text into a short, readable summary using a **fine-tuned T5 Transformer model**.

The application is built with **FastAPI** on the backend and a simple **HTML/CSS/JavaScript** frontend. The model is fine-tuned using **Hugging Face Transformers and PyTorch**.

---

## 🚀 Features

* Summarize long text using a fine-tuned **T5 Transformer**
* Simple and easy-to-use web interface
* FastAPI backend for model inference
* Text preprocessing and tokenization
* Loads a locally saved fine-tuned model
* REST API endpoint for summarization
* Interactive API documentation with FastAPI
* Runs locally on CPU — no GPU required

---

## 🧠 How It Works

The application follows this workflow:

```text
User enters text
       ↓
Frontend sends text to FastAPI
       ↓
Text preprocessing
       ↓
Tokenization using T5 tokenizer
       ↓
Fine-tuned T5 model
       ↓
Text generation
       ↓
Generated summary
       ↓
Summary displayed on the webpage
```

The project covers the complete NLP workflow:

1. Text preprocessing
2. Tokenization
3. Transformer model fine-tuning
4. Saving the trained model
5. Loading the trained model
6. Model inference
7. Serving the model through a web application

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI
* Uvicorn

### Machine Learning / NLP

* PyTorch
* Hugging Face Transformers
* T5 Transformer

### Development

* Git
* GitHub
* Conda / Python Virtual Environment

---

## 📁 Project Structure

```text
AI_Text_Summarizer/
│
├── app.py                  # FastAPI application
│
├── templates/
│   └── index.html          # Frontend webpage
│
├── my_t5_model/            # Fine-tuned T5 model (not included in Git)
│
├── requirements.txt        # Python dependencies
│
├── .gitignore              # Ignored files and folders
│
└── README.md               # Project documentation
```

> **Note:** The `my_t5_model/` folder is not included in this repository because the model files are approximately **233 MB**, which exceeds GitHub's recommended file-size limits.

---

# ⚙️ Setup

## 1. Prerequisites

Make sure you have:

* Python **3.10 or 3.11**
* Conda
* Git

Check your Python version:

```bash
python3 --version
```

### Recommended

Python 3.10 or 3.11 is recommended for this project.

If your Mac already has a different Python version, it is better to use **Conda** to create an isolated environment rather than changing your system Python installation.

If you don't have Conda, install **Miniconda** first.

---

## 2. Clone the Repository

```bash
git clone https://github.com/GurbachanS/AI_Text_Summarizer.git
cd AI_Text_Summarizer
```

---

## 3. Create a Conda Environment

Create a dedicated environment for the project:

```bash
conda create -n text_summarizer python=3.11 -y
```

Activate it:

```bash
conda activate text_summarizer
```

> You need to run `conda activate text_summarizer` again whenever you open a new terminal session.

---

## 4. Install Dependencies

Upgrade pip:

```bash
pip install --upgrade pip
```

Install the required packages:

```bash
pip install -r requirements.txt
```

> **Note:** PyTorch is a relatively large package, so the installation may take a few minutes.

---

# 🤖 Get the Fine-Tuned Model

The application expects the fine-tuned model to be located at:

```text
AI_Text_Summarizer/
└── my_t5_model/
```

There are two ways to get the model.

### Option 1 — Download the Trained Model

Download the trained model from:

**[Hugging Face Hub / Google Drive — Add your link here]**

After downloading, place the model folder in the project root:

```text
AI_Text_Summarizer/
├── app.py
├── templates/
├── my_t5_model/
├── requirements.txt
└── README.md
```

### Option 2 — Train the Model Yourself

If you want to reproduce the training process, fine-tune T5 using the required dataset.

After training, save the model and tokenizer:

```python
model.save_pretrained("my_t5_model")
tokenizer.save_pretrained("my_t5_model")
```

The resulting folder should contain files similar to:

```text
my_t5_model/
├── config.json
├── tokenizer_config.json
├── tokenizer.json
├── special_tokens_map.json
└── model.safetensors
```

You can verify that the model is in the correct location:

```bash
ls my_t5_model
```

---

# ▶️ Run the Application

Make sure the Conda environment is activated:

```bash
conda activate text_summarizer
```

Start the FastAPI server:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Once the server starts, open:

### 🌐 Web Application

```text
http://localhost:8000
```

### 📚 FastAPI API Documentation

```text
http://localhost:8000/docs
```

The frontend and backend are served by the **same FastAPI application**, so only one server process is required.

---

# 🖥️ How to Use

1. Open:

   ```text
   http://localhost:8000
   ```

2. Enter or paste the text you want to summarize.

3. Click **Summarize**.

4. The application sends the text to the FastAPI backend.

5. The T5 model processes the input and generates a summary.

6. The generated summary is displayed on the webpage.

---

# 🔌 API

The FastAPI backend also provides an API endpoint for text summarization.

You can explore and test the available endpoints through:

```text
http://localhost:8000/docs
```

FastAPI automatically generates interactive API documentation using Swagger UI.

---

# ⚡ Performance Notes

### First Request

The first request may take longer because the fine-tuned model needs to be loaded into memory.

### CPU Inference

The application can run on a CPU, so a GPU is **not required**.

However, inference may be slower on CPU compared with a GPU.

---

# 🐛 Troubleshooting

## `OSError` or `FileNotFoundError` for `my_t5_model`

Make sure the model folder exists in the project root:

```text
AI_Text_Summarizer/
└── my_t5_model/
```

Also make sure you start Uvicorn from the project root:

```bash
cd AI_Text_Summarizer
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

---

## Port 8000 Already in Use

If port `8000` is already being used, run the application on another port:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8001
```

Then open:

```text
http://localhost:8001
```

---

# 📦 Model Information

| Component     | Details                     |
| ------------- | --------------------------- |
| Model         | T5 Transformer              |
| Training      | Fine-tuned                  |
| Framework     | Hugging Face Transformers   |
| Deep Learning | PyTorch                     |
| Model Size    | ~233 MB                     |
| Inference     | CPU supported               |
| Storage       | Local `my_t5_model/` folder |

---

# 🔮 Future Improvements

The following features can be added in future versions:

* [ ] Deploy the application with **Hugging Face Spaces**
* [ ] Add a public demo link
* [ ] Add adjustable summary length controls
* [ ] Add ROUGE evaluation and report model scores
* [ ] Support PDF file uploads
* [ ] Support TXT file uploads
* [ ] Add Docker support
* [ ] Improve frontend UI/UX
* [ ] Add loading/progress indicators
* [ ] Add support for larger input documents

---

# 📌 Important Notes

* The trained model is **not included in this GitHub repository** because of its large file size.
* The model must be placed inside `my_t5_model/` before running the application.
* Make sure you are using the correct Python environment.
* The application can run without a GPU.
* Keep `my_t5_model/` in `.gitignore` to prevent accidentally committing large model files.

---

