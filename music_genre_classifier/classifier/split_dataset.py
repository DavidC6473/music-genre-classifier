import os
import random
import shutil

def split_dataset(input_dir, output_dir, split_ratio):
    genres = os.listdir(input_dir)
    for genre in genres:
        genre_dir = os.path.join(input_dir, genre)
        files = os.listdir(genre_dir)
        random.shuffle(files)
        split_index = int(len(files) * split_ratio)

        train_files = files[:split_index]
        test_files = files[split_index:]

        train_genre_dir = os.path.join(output_dir, 'train', genre)
        test_genre_dir = os.path.join(output_dir, 'test', genre)

        os.makedirs(train_genre_dir, exist_ok=True)
        os.makedirs(test_genre_dir, exist_ok=True)

        for file in train_files:
            src = os.path.join(genre_dir, file)
            dst = os.path.join(train_genre_dir, file)
            shutil.copy(src, dst)

        for file in test_files:
            src = os.path.join(genre_dir, file)
            dst = os.path.join(test_genre_dir, file)
            shutil.copy(src, dst)

if __name__ == '__main__':
    input_dir = 'datasets/features'
    output_dir = 'datasets/split'
    split_ratio = 0.8
    split_dataset(input_dir, output_dir, split_ratio)
