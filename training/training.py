import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

directory = "/Users/joaomiao/HACKLONDON2025/BSL_Datasets/BSL_Images/"
# Define CNN Model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(6, activation='softmax')  # Adjust for number of classes
])

# Compile Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Load Data
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_data = datagen.flow_from_directory(directory, target_size=(224, 224), batch_size=32, class_mode="categorical", subset="training")
val_data = datagen.flow_from_directory(directory, target_size=(224, 224), batch_size=32, class_mode="categorical", subset="validation")

# Train Model
model.fit(train_data, validation_data=val_data, epochs=10)
