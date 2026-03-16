from transformers import pipeline

# Use a smaller model for summarization
summarizer = pipeline("summarization")

# Example text
input_text = "This is a short text to test summarization."
summary = summarizer(input_text)
print("Summary:", summary)