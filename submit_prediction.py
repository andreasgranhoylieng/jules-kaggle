import subprocess

competition = "playground-series-s5e5"
file_path = "submission.csv"
message = "Message"

subprocess.run([
    "kaggle", "competitions", "submit",
    "-c", competition,
    "-f", file_path,
    "-m", message
])
# Note: Ensure that you have the Kaggle API installed and configured with your credentials.