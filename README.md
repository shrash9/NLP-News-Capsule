# NLP News Capsule

## Overview

In today’s fast-paced world, staying informed by reading multiple news articles can be overwhelming and time-consuming. Text summarization leverages natural language processing (NLP) to condense lengthy articles into concise, digestible summaries, allowing users to quickly grasp the key points. This project aims to build an advanced news summarization tool that applies state-of-the-art NLP techniques to deliver accurate, readable summaries of news content efficiently.

## Features

The NLP News Capsule offers the following capabilities:

* **Extractive Summarization**: Identifies and extracts the most relevant sentences from a news article, creating a summary that directly reflects the original text.
* **Abstractive Summarization**: Generates concise summaries by paraphrasing and rephrasing content, producing natural and coherent summaries beyond mere extraction.
* **Customizable Summary Length**: Users can specify the desired summary length, enabling flexible control over the level of detail.
* **Multilingual Support**: Summarizes news articles in multiple languages, including English, Spanish, French, German, and Chinese, broadening its usability across diverse audiences.
* **API Access**: Provides a RESTful API, allowing seamless integration of summarization features into external applications and workflows.

## Installation

Follow these steps to install NLP News Capsule:

1. Clone the repository:
   `git clone https://github.com/shrash9/NLP-News-Capsule.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Launch the application:
   `python app.py`

## Usage

To use NLP News Capsule:

1. Open your web browser and navigate to `http://localhost:5000/`.
2. Enter the URL or paste the text of the news article you wish to summarize.
3. Choose between extractive or abstractive summarization techniques.
4. Select the preferred summary length.
5. Click the "Summarize" button to view the generated summary.

Alternatively, use the RESTful API by sending a POST request to the endpoint with these parameters:

* `text`: The news article content.
* `technique`: Either `"extractive"` or `"abstractive"`.
* `length`: Desired summary length.

## Conclusion

NLP News Capsule empowers users to stay informed efficiently by transforming extensive news articles into clear, concise summaries. Its customizable features and multilingual capabilities make it versatile and accessible to a wide audience. With API support, it is designed to be easily integrated into other platforms and applications. This project strives to simplify news consumption and keep users up-to-date with minimal effort.