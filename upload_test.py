import requests

# url = "http://localhost:8000/embed"

# files = {
#     "file": open("/mnt/c/Users/TAAZUCA2/Documents/KapoSO test/shorttestdocument.pdf", "rb")  # "/mnt/c/Users/TAAZUCA2/Documents/KapoSO test/shorttestdocument.pdf" #open("/mnt/c/Users/TAAZUCA2/Documents/KapoSO test/shorttestdocument.pdf", "rb") #"C:\Users\TAAZUCA2\Documents\KapoSO test\KapoSOtest.pdf"
# }

# data = {
#     "file_id": "test-file-001"
# }

# response = requests.post(url, files=files, data=data)
# print(response.json())

url = "http://localhost:8000/embed"

file_path = "./uploads/shorttestdocument.pdf"

files = {
    "file": open(file_path, "rb")  # Just send the file, don't load it yourself
}

data = {
    "file_id": "test-file-001",
    "entity_id": "test-entity-001"  # Optional, but avoids issues
}

response = requests.post(url, files=files, data=data)
print(response.json())  # Print API response

# Close file after request
files["file"].close()

