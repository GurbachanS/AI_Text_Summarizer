from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re

# ✅ MUST BE FIRST
app = FastAPI()

# load model
model = T5ForConditionalGeneration.from_pretrained("./my_t5_model")
tokenizer = T5Tokenizer.from_pretrained("./my_t5_model")

# device setup
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model.to(device)

# input schema
class DialogueInput(BaseModel):
    dialogue: str

# clean text
def clean_data(text):
    text = re.sub(r"\r\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    return text.strip().lower()

# summarize function
def summarize_dialogue(dialogue: str):
    dialogue = clean_data(dialogue)

    inputs = tokenizer(
        dialogue,
        return_tensors="pt",
        max_length=512,
        truncation=True,
        padding="max_length"
    )

    inputs = {k: v.to(device) for k, v in inputs.items()}

    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# ✅ ROUTES MUST COME AFTER app

@app.get("/")
async def home():
    return FileResponse("templates/index.html")

@app.post("/summarize/")
async def summarize(data: DialogueInput):
    summary = summarize_dialogue(data.dialogue)
    return {"summary": summary}