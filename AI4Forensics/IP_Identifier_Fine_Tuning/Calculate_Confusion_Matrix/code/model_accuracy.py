from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, confusion_matrix
import pandas as pd

predicted_dataset = pd.read_csv("test100_results_dataset.csv")

predicted_labels = predicted_dataset["pred_label"]

actual_labels = predicted_dataset["label"]

cm = confusion_matrix(actual_labels, predicted_labels)
print("Confusion Matrix:")
print(f"{cm}\n")

f1_score = f1_score(actual_labels, predicted_labels, average="binary")
precision_score = precision_score(actual_labels, predicted_labels, average="binary")
recall_score = recall_score(actual_labels, predicted_labels, average="binary")
accuracy_score = accuracy_score(actual_labels, predicted_labels)

print(f"F1 Score is {f1_score}\n")
print(f"Precision Score is {precision_score}\n")
print(f"Recall Score is {recall_score}\n")
print(f"Accuracy Score is {accuracy_score}\n")
