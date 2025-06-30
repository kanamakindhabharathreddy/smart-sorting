# SmartSort - Image Dataset

This directory contains the image dataset used for training and testing the SmartSort model. The model is a Convolutional Neural Network (CNN) designed to classify the freshness of various fruits and vegetables.

## Directory Structure

The dataset is organized into two main directories, `train` and `test`, which is a standard structure for use with TensorFlow's ImageDataGenerator.

```
dataset/
├── train/
│   ├── Apple__Healthy/
│   │   ├── image001.jpg
│   │   └── ...
│   ├── Apple__Rotten/
│   │   └── ...
│   ├── Banana__Healthy/
│   │   └── ...
│   ├── (and so on for all classes)
│   └── ...
│
└── test/
    ├── Apple__Healthy/
    │   ├── image_test_01.jpg
    │   └── ...
    ├── Apple__Rotten/
    │   └── ...
    ├── (and so on for all classes)
    └── ...
```

- `train/`: Contains the majority of the images used for training the model. Each subdirectory is a unique class.
- `test/`: Contains a smaller, separate set of images used for validating the model's performance after training.

## Classes

The model is trained to recognize the following classes. The subdirectory names must match this format exactly for the `train_model.py` script to work correctly.

The format is `ProduceName__Condition`.

- Apple__Healthy
- Apple__Rotten
- Banana__Healthy
- Banana__Rotten
- Bellpepper__Healthy
- Bellpepper__Rotten
- Carrot__Healthy
- Carrot__Rotten
- Cucumber__Healthy
- Cucumber__Rotten
- Grape__Healthy
- Grape__Rotten
- Guava__Healthy
- Guava__Rotten
- Jujube__Healthy
- Jujube__Rotten
- Mango__Healthy
- Mango__Rotten
- Orange__Healthy
- Orange__Rotten
- Pomegranate__Healthy
- Pomegranate__Rotten
- Potato__Healthy
- Potato__Rotten
- Strawberry__Healthy
- Strawberry__Rotten
- Tomato__Healthy
- Tomato__Rotten

## Data Source

The images in this dataset were compiled from the Fruit and Vegetable Disease (Healthy vs Rotten) dataset, which is publicly available on Kaggle. The collection was then curated and augmented to create a balanced set for training and testing purposes.

Dataset Link: [Fruit and Vegetable Disease (Healthy vs Rotten) on Kaggle](https://www.kaggle.com/datasets/muhammad0subhan/fruit-and-vegetable-disease-healthy-vs-rotten)

Data augmentation techniques applied during training (e.g., rotation, zoom, flips) help the model generalize better to new, unseen images.
