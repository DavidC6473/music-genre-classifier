import os
import numpy as np
import joblib
import librosa
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def extract_features(audio_path, num_frames):
    audio, _ = librosa.load(audio_path)
    features = librosa.feature.mfcc(y=audio, sr=44100)
    
    if features.shape[1] < num_frames:
        # Pad with zeros if the number of frames is less than num_frames
        features = np.pad(features, ((0, 0), (0, num_frames - features.shape[1])), mode='constant')
    elif features.shape[1] > num_frames:
        # Truncate if the number of frames is greater than num_frames
        features = features[:, :num_frames]
    
    return features

def load_dataset(genres_dir, num_frames):
    train_data = []
    train_labels = []
    genres = os.listdir(genres_dir)
    for genre_id, genre in enumerate(genres):
        genre_dir = os.path.join(genres_dir, genre)
        files = os.listdir(genre_dir)
        for file in files:
            file_path = os.path.join(genre_dir, file)
            features = extract_features(file_path, num_frames)
            
            train_data.append(features)
            train_labels.append(genre_id)
    
    train_data = np.array(train_data)
    train_labels = np.array(train_labels)
    
    return train_data, train_labels, genres

def train_model():
    genres_dir = 'C:/Users/David/Desktop/Desktop Folder/Portfolio/MusicGenreClassifier/music_genre_classifier/datasets/train'
    num_frames = 100  # Adjust this value as needed
    train_data, train_labels, genres = load_dataset(genres_dir, num_frames)

    # Reshape train_data to have 2 dimensions
    train_data = train_data.reshape(train_data.shape[0], -1)

    # Standardize the feature data
    scaler = StandardScaler()
    train_data = scaler.fit_transform(train_data)

    # Train the classifier
    classifier = MLPClassifier(hidden_layer_sizes=(100,), random_state=42)
    classifier.fit(train_data, train_labels)

    # Save the trained model
    model_path = 'C:/Users/David/Desktop/Desktop Folder/Portfolio/MusicGenreClassifier/music_genre_classifier/classifier/model.joblib'
    joblib.dump(classifier, model_path)
    print("Model saved to:", model_path)

    # Save the genre labels
    labels_path = 'C:/Users/David/Desktop/Desktop Folder/Portfolio/MusicGenreClassifier/music_genre_classifier/classifier/labels.npy'
    np.save(labels_path, genres)
    print("Genre labels saved to:", labels_path)

    # Save the scaler
    scaler_path = 'C:/Users/David/Desktop/Desktop Folder/Portfolio/MusicGenreClassifier/music_genre_classifier/classifier/scaler.joblib'
    joblib.dump(scaler, scaler_path)
    print("Scaler saved to:", scaler_path)

if __name__ == '__main__':
    train_model()

