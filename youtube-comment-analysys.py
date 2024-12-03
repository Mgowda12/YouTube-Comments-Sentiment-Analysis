import re
import streamlit as st
from googleapiclient.discovery import build
from textblob import TextBlob

# Set up YouTube API
API_KEY = 'YOUTUBE_API_KEY'  # Replace with your YouTube API key
youtube = build('youtube', 'v3', developerKey=API_KEY)


def extract_video_id(youtube_url):
    """Extracts the video ID from a YouTube URL."""
    video_id_match = re.search(r'v=([a-zA-Z0-9_-]{11})', youtube_url)
    return video_id_match.group(1) if video_id_match else None


def get_comments(video_id):
    comments = []
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText',
        maxResults=100
    )

    while request:
        response = request.execute()
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        request = youtube.commentThreads().list_next(request, response)

    return comments


def analyze_sentiment(comments):
    sentiment_results = {}
    for comment in comments:
        analysis = TextBlob(comment)
        # Classify the polarity
        if analysis.sentiment.polarity > 0:
            sentiment_results[comment] = 'Positive'
        elif analysis.sentiment.polarity < 0:
            sentiment_results[comment] = 'Negative'
        else:
            sentiment_results[comment] = 'Neutral'

    return sentiment_results


def clear_all():
    """Clears the session state."""
    st.session_state['youtube_url'] = ""  # Reset input URL
    st.session_state['comments'] = []  # Reset comments
    st.session_state['sentiment_results'] = {}  # Reset sentiment results


def main():
    st.title("YouTube Comment Sentiment Analysis")

    # Initialize session state if not already
    if 'youtube_url' not in st.session_state:
        st.session_state['youtube_url'] = ""

    # Input field for YouTube URL with Enter
    youtube_url = st.text_input("Enter the YouTube video link:", value=st.session_state['youtube_url'],
                                key="youtube_url")

    # Clear button to reset the input and content
    # if st.button("Clear All"):
    #     clear_all()

    if youtube_url:
        # Extract Video ID
        video_id = extract_video_id(youtube_url)
        if not video_id:
            st.error("Invalid YouTube URL. Please enter a valid link.")
            return

        st.info("Fetching comments...")
        comments = get_comments(video_id)

        if not comments:
            st.warning("No comments found for this video.")
            return

        st.info("Analyzing sentiment...")
        sentiment_results = analyze_sentiment(comments)

        # Store the results in session_state
        st.session_state['comments'] = comments
        st.session_state['sentiment_results'] = sentiment_results

        # Display sentiment results
        t_c, p, n, ne = 0, 0, 0, 0
        positive_comments = {}
        negative_comments = {}
        neutral_comments = {}

        st.subheader("Sentiment Analysis Results")
        for comment, sentiment in sentiment_results.items():
            t_c += 1
            if sentiment == 'Positive':
                p += 1
                positive_comments[comment] = sentiment
            elif sentiment == 'Negative':
                n += 1
                negative_comments[comment] = sentiment
            else:
                ne += 1
                neutral_comments[comment] = sentiment

        st.write(f"**Total Comments:** {t_c}")
        st.write(f"**Positive Comments:** {p}")
        st.write(f"**Negative Comments:** {n}")
        st.write(f"**Neutral Comments:** {ne}")

        # Filters for sentiment
        filter_choice = st.radio("Filter comments by sentiment:", ("All", "Positive", "Negative", "Neutral"))

        if filter_choice == "Positive":
            st.subheader("Positive Comments")
            for comment, sentiment in positive_comments.items():
                st.write(f"**Comment:** {comment}")
                st.write(f"**Sentiment:** {sentiment}")
                st.write("---")

        elif filter_choice == "Negative":
            st.subheader("Negative Comments")
            for comment, sentiment in negative_comments.items():
                st.write(f"**Comment:** {comment}")
                st.write(f"**Sentiment:** {sentiment}")
                st.write("---")

        elif filter_choice == "Neutral":
            st.subheader("Neutral Comments")
            for comment, sentiment in neutral_comments.items():
                st.write(f"**Comment:** {comment}")
                st.write(f"**Sentiment:** {sentiment}")
                st.write("---")

        elif filter_choice == "All":
            st.subheader("All Comments")
            for comment, sentiment in sentiment_results.items():
                st.write(f"**Comment:** {comment}")
                st.write(f"**Sentiment:** {sentiment}")
                st.write("---")


if __name__ == "__main__":
    main()
