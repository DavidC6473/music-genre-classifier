import sys
import joblib
import numpy as np
import librosa

def load_model(model_path, labels_path, scaler_path):
    classifier = joblib.load(model_path)
    genres = np.load(labels_path)
    scaler = joblib.load(scaler_path)
    return classifier, genres, scaler

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

def predict_genre(audio_path):
    model_path = 'C:/Users/David/Desktop/Desktop Folder/Portfolio/MusicGenreClassifier/music_genre_classifier/classifier/model.joblib'
    labels_path = 'C:/Users/David/Desktop/Desktop Folder/Portfolio/MusicGenreClassifier/music_genre_classifier/classifier/labels.npy'
    scaler_path = 'C:/Users/David/Desktop/Desktop Folder/Portfolio/MusicGenreClassifier/music_genre_classifier/classifier/scaler.joblib'
    
    classifier, genres, scaler = load_model(model_path, labels_path, scaler_path)
    
    features = extract_features(audio_path, num_frames=100)  # Make sure this value matches the value used during training
    
    # Reshape features to have 2 dimensions
    features = features.reshape(1, -1)
    
    # Standardize the feature data
    features = scaler.transform(features)
    
    # Predict the genre
    predicted_label = classifier.predict(features)[0]
    predicted_genre = genres[predicted_label]
    
    return predicted_genre

if __name__ == '__main__':
    audio_path = sys.argv[1]
    try:
        genre = predict_genre(audio_path)
        print("Predicted genre:", genre)
    except Exception as e:
        print("Error occurred:", str(e))
