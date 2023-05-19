import os
import librosa
import numpy as np

def extract_features(audio_path):
    # Load audio file
    audio, _ = librosa.load(audio_path)

    # Extract features
    features = librosa.feature.mfcc(y=audio, sr=44100)

    return features

def save_features(features, output_path):
    np.save(output_path, features)

def process_genre(genre_dir, output_dir):
    files = os.listdir(genre_dir)
    for file in files:
        file_path = os.path.join(genre_dir, file)
        features = extract_features(file_path)
        output_file = os.path.splitext(file)[0] + '.npy'
        output_path = os.path.join(output_dir, output_file)
        save_features(features, output_path)

def process_genres(genres_dir, output_dir):
    genres = os.listdir(genres_dir)
    for genre in genres:
        genre_dir = os.path.join(genres_dir, genre)
        output_genre_dir = os.path.join(output_dir, genre)
        os.makedirs(output_genre_dir, exist_ok=True)
        process_genre(genre_dir, output_genre_dir)

if __name__ == '__main__':
    genres_dir = 'datasets/train'
    output_dir = 'datasets/features'
    process_genres(genres_dir, output_dir)
