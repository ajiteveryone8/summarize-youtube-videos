# YouTube Video Summarizer

This Python project extracts transcripts from YouTube videos and generates concise summaries using Hugging Face Transformers.

## Features

- Extracts video transcripts using [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api)
- Summarizes transcripts with a pretrained model from Hugging Face
- Progress bar for summarization with `tqdm`
- Saves summaries to a file named `<video_id>.summary`

## Requirements

See [requirement.txt](requirement.txt) for dependencies:
- youtube-transcript-api
- transformers
- torch
- tqdm
- streamlit

Install dependencies with:
```sh
pip install -r requirement.txt
```

## Usage

Run the script:
```sh
python summarize.py
```
Enter a YouTube video URL when prompted. The script will fetch the transcript, summarize it, and save the summary to a file.

## Example

A summary file ([WHLuimGVzBA.summary](WHLuimGVzBA.summary)) is included as an example.

## License

MIT License
