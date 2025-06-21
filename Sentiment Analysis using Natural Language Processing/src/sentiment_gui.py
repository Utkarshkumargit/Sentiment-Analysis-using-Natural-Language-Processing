import tkinter as tk
from textblob import TextBlob

def analyze_sentiment():
    text = entry.get("1.0", tk.END)
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        result.set("Sentiment: Positive")
    elif polarity < 0:
        result.set("Sentiment: Negative")
    else:
        result.set("Sentiment: Neutral")

# GUI setup
root = tk.Tk()
root.title("Sentiment Analyzer")

tk.Label(root, text="Enter Text:").pack()
entry = tk.Text(root, height=6, width=50)
entry.pack()

tk.Button(root, text="Analyze", command=analyze_sentiment).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14)).pack()

root.mainloop()
