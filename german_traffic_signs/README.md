
# Traffic Sign Recognition

## Overview
This project involves building a Convolutional Neural Network (CNN) to recognize and classify traffic signs using the German Traffic Sign Recognition Benchmark (GTSRB) dataset. The goal is to accurately identify traffic signs from images to aid in autonomous driving and traffic management systems.

## Dataset
- **German Traffic Website:** [GTSRB](https://benchmark.ini.rub.de/gtsrb_news.html)
- The dataset contains images of traffic signs belonging to 43 different classes.

## Project Structure
```
.
├── traffic-signs-data
│   ├── train.p
│   ├── valid.p
│   └── test.p
├── Traffic_Sign_Recognition.ipynb
├── README.md
└── imgs
    ├── lenet.png
    └── traffic-signs-cnn.png
```

## Requirements
- Python 3.x
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Keras
- TensorFlow
- OpenCV
- scikit-learn

Install the necessary libraries using:
```bash
pip install numpy pandas matplotlib seaborn keras tensorflow opencv-python scikit-learn
```

## Steps

### 1. Importing Libraries
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import cv2
import warnings
warnings.filterwarnings("ignore")
%matplotlib inline
sns.set()
```

### 2. Data Collection and Preprocessing
- Load and explore the dataset
- Convert images to grayscale and normalize them using `MinMaxScaler`
- Apply data augmentation techniques

### 3. Model Development
- Build a CNN inspired by the LeNet architecture
- Add layers including `Conv2D`, `MaxPooling2D`, `Flatten`, `Dense`, and `Dropout`

### 4. Training
- Train the model using the augmented dataset
- Monitor training using accuracy and loss metrics for both training and validation sets
- Achieve significant results with impressive accuracy

### 5. Evaluation
- Evaluate the model on the test dataset
- Achieve a high test accuracy of **83.40%**
- Achieve **81.20%** accuracy and **0.6851** loss on the training data, and **83.72%** accuracy and **0.5956** loss on the validation data
- Visualize training and validation accuracy and loss

## Results
- **Test Accuracy:** 83.40%
- Training and validation accuracy and loss visualized to understand the model’s performance

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/alim9hamed/german_traffic_signs.git
   ```
2. Navigate to the project directory:
   ```bash
   cd german_traffic_signs
   ```
3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook Traffic_Sign_Recognition.ipynb
   ```

## Acknowledgements
- The German Traffic Sign Recognition Benchmark (GTSRB) for the dataset.
- [Yann LeCun](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf) for the LeNet architecture.
---

Feel free to tweak any sections to better fit your project details and personal preferences.
