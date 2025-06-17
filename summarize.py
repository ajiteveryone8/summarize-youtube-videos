from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
from tqdm import tqdm  # Add this import

# Extract YouTube Video ID
def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1]
    else:
        return None

# Get transcript
def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([item['text'] for item in transcript])
    return full_text

# Summarize with Hugging Face pipeline
def summarize_text(text):
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""
    for chunk in tqdm(chunks, desc="Summarizing", unit="chunk"):  # Add progress bar
        out = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summary += out[0]['summary_text'] + "\n"
    return summary

# Main
if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    video_id = extract_video_id(url)
    if video_id:
        print("Fetching transcript...")
        transcript = get_transcript(video_id)
        print("\transcript:\n", transcript)
        print("Summarizing...")
        result = summarize_text(transcript)
        print("\nSummary:\n", result)

        # Save summary to file named <video_id>.summary
        with open(f"{video_id}.summary", "w", encoding="utf-8") as f:
            f.write(f"URL: {url}\n\nSummary:\n{result}")
        print(f"Summary saved to {video_id}.summary")
    else:
        print("Invalid URL.")