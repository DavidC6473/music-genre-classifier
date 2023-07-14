# Music Genre Classifier

This project is a music genre classification system using machine learning. It uses audio features extracted from music files to predict their corresponding genre. The system is built using Python and utilizes the Librosa library for audio processing, scikit-learn for machine learning, and Django for the web application.

## Features

- Train a machine learning model to classify music genres.
- Extract audio features using the Librosa library.
- Support for multiple genres.

## Getting Started

To use this project and classify music genres, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/music-genre-classifier.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Predict the genre of a music file: `python predict_genre.py path/to/music_file.mp3`

The trained AI model is included in the repository, so there's no need to train it again unless you have new data to incorporate or want to improve the model further.

## Usage

### Predicting the Genre

To predict the genre of a music file using the trained model, run the `predict_genre.py` script and provide the path to the music file as an argument:

python predict_genre.py path/to/music_file.mp3


## Web Application (Work in Progress)

A web application is currently under development to provide a user-friendly interface for classifying music genres. This will allow users to upload their music files and receive genre predictions. The Music Genre Classifier will be added to the webpage using Django. Stay tuned for updates on the progress of the web application.

## Future Work

Here are some potential areas to explore for further development and improvement of the music genre classifier:

- Increase the size and diversity of the training dataset to improve model performance.
- Experiment with different audio features and machine learning algorithms to enhance classification accuracy.
- Implement additional functionality such as genre recommendation based on user preferences.

## Data Source

The music dataset used to train the model is sourced from the GTZAN Genre Collection (https://www.kaggle.com/datasets/carlthome/gtzan-genre-collection?resource=download), which provides a collection of diverse music tracks. The dataset includes a variety of genres such as rock, pop, hip-hop, jazz, and more.

