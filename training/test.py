from tensorflow.keras.models import load_model

# Load your saved model
model = load_model("bsl_sign_language_model.h5")  # Update path if needed

# Define class labels (update these to match your dataset)
class_labels = ["Hello", "Thank You", "Yes", "No", "Please", "You"]

print("✅ Model Loaded Successfully!")
