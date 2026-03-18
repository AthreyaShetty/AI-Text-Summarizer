from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization")


text = """
Artificial intelligence (AI) is intelligence demonstrated by machines, 
as opposed to natural intelligence displayed by animals including humans. 
AI research has been defined as the field of study of intelligent agents.AI
"""


summary = summarizer(text, max_length=50, min_length=20, do_sample=False)

print(summary[0]['summary_text'])