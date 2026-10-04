# Flower Classification Project 🌸

This project builds an image classifier to identify flower types using transfer learning on the Xception model, fine-tuning it with custom layers for improved classification accuracy. The model is trained on the [TF Flowers dataset](https://www.tensorflow.org/datasets/catalog/tf_flowers), which consists of various flower images. The implementation leverages TensorFlow, TensorFlow Datasets, and OpenCV for image handling, data processing, and model training.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12V7CvZBTypGQ9iY7vvh_LhqVgL2xEBDX?usp=sharing)

## Table of Contents
1. [Dataset Preparation](#dataset-preparation)
2. [Model Architecture](#model-architecture)
3. [Training](#training)
4. [Evaluation](#evaluation)
5. [Results](#results)
6. [Deployment](#deployment)
7. [Requirements](#requirements)

---

### Dataset Preparation

The `TF Flowers` dataset is loaded directly from `tensorflow_datasets`, which includes multiple flower classes. 

- **Dataset Loading**: The dataset is split into training, validation, test, and sample sets using custom ratios for comprehensive testing and validation. 
- **Image Display**: OpenCV is used to display samples from the dataset to visualize preprocessing and augmentations.

```python
amples_list = list(samples)
image_np = samples_list[4][0].numpy()  # Convert to NumPy array

# Convert from BGR to RGB
image_rgb = cv.cvtColor(image_np, cv.COLOR_BGR2RGB)

# Display the RGB image
cv2_imshow(image_rgb)
```

### Model Architecture

The model utilizes Xception as a base architecture with pre-trained weights from ImageNet. We apply a series of preprocessing steps and data augmentation layers to help the model generalize better:

- **Base Model**: Xception (pre-trained on ImageNet) with top layers removed.
- **Custom Layers**: Global Average Pooling layer and Dense layer with softmax activation for classification.
- **Data Augmentation**: Horizontal flipping, random rotation, and contrast adjustments applied to input images.

```python
# Define the data augmentation model using the functional API
inputs = tf.keras.Input(shape=(224, 224, 3))  # Input layer
x = tf.keras.layers.RandomFlip(mode="horizontal", seed=42)(inputs)  # Randomly flip images horizontally
x = tf.keras.layers.RandomRotation(factor=0.05, seed=42)(x)           # Randomly rotate images
x = tf.keras.layers.RandomContrast(factor=0.2, seed=42)(x)             # Randomly adjust contrast

# Add the base model (Xception) without the top layers
# Store the Xception model in a variable called 'base_xception_model'
base_xception_model = tf.keras.applications.Xception(include_top=False, weights='imagenet')
x = base_xception_model(x)  # Pass the augmented input to the base model

x = tf.keras.layers.GlobalAveragePooling2D()(x)  # Global average pooling layer
outputs = tf.keras.layers.Dense(5, activation='softmax')(x)  # Final classification layer

# Create the model
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Now, you can access the layers of the Xception model using 'base_xception_model'
for layer in base_xception_model.layers[56:]:
    layer.trainable = True
# model.summary()
```

### Training

The model is compiled with `SGD` optimizer, employing a learning rate of `0.01` and a `momentum` of `0.9`. An `EarlyStopping` callback monitors validation loss to avoid overfitting:

```python
from tensorflow.keras.callbacks import EarlyStopping

# Initialize early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=0, restore_best_weights=True)

# Compile and train the model
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)
model.compile(loss="sparse_categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])
history = model.fit(train_set, validation_data=valid_set, epochs=10, callbacks=[early_stopping])
```

### Evaluation

After training, the model is evaluated on the test set using predictions and a classification report to analyze metrics like precision, recall, and F1-score for each class:

```python
from sklearn.metrics import classification_report
import numpy as np

# Generate predictions on the test set
predictions = model.predict(test_set)
true_labels = np.concatenate([y for _, y in test_set], axis=0)
predicted_labels = np.argmax(predictions, axis=1)

# Classification report
report = classification_report(true_labels, predicted_labels)
print(report)
```

### Results

The model achieves an accuracy of approximately `93%` on the test set. Detailed results with class-wise metrics are included in the printed classification report.

### Deployment

The trained model weights are saved for future use or deployment:

```python
# Save model weights
model.save_weights("model.weights.h5")
```

### Requirements

Install the following packages to replicate this project:

- `TensorFlow >= 2.5`
- `TensorFlow Datasets`
- `OpenCV`
- `NumPy`
- `scikit-learn`

To install the dependencies, run:

```bash
pip install tensorflow tensorflow_datasets opencv-python-headless numpy scikit-learn
```

---

### Acknowledgments

This project is inspired by transfer learning techniques and aims to deliver a practical example of fine-tuning a deep learning model using the TF Flowers dataset.

