# YouTube Comment Sentiment Analysis

This is a Python application that analyzes the sentiment of YouTube video comments using the YouTube Data API and TextBlob library. The application is built with Streamlit, providing an interactive web interface for users.

## Features

- Extract comments from any YouTube video by providing its URL.
- Perform sentiment analysis on the comments and classify them as:
  - **Positive**
  - **Negative**
  - **Neutral**
- Display the total count of comments and the breakdown of sentiments.
- Filter comments by sentiment type (All, Positive, Negative, Neutral).

## Requirements

- Python 3.7+
- Libraries:
  - `streamlit`
  - `google-api-python-client`
  - `textblob`

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   Ensure the following libraries are included in your `requirements.txt`:

   ```
   streamlit
   google-api-python-client
   textblob
   ```

3. **Set Up the YouTube Data API Key:**

   - Obtain an API key from the [Google Cloud Console](https://console.cloud.google.com/).
   - Replace the placeholder `API_KEY` in the code with your YouTube Data API key.

4. **Run the Application:**

   ```bash
   streamlit run youtube_sentiment_analysis.py
   ```

5. **Access the Application:**
   Open the URL provided in the terminal (usually `http://localhost:8501`) in your web browser.

## Usage

1. Enter the URL of the YouTube video you want to analyze.
2. View the total number of comments and their sentiment breakdown.
3. Use the radio button to filter comments by sentiment type.
4. Explore the detailed comments and their sentiment classification.

##



## Limitations

- The YouTube Data API limits the number of comments retrieved to 100 per request.
- The sentiment analysis relies on TextBlob, which may not always accurately classify sentiments.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

**Happy Analyzing!**

