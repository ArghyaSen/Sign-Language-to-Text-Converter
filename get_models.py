import os
import urllib.request
import zipfile
import shutil

def download_models():
    url = "https://github.com/ahmtarekragab/Sign-Language-To-Text-Conversion/archive/refs/heads/master.zip"
    zip_name = "repo.zip"
    extract_folder = "temp_extract"
    target_folder = "model"

    os.makedirs(target_folder, exist_ok=True)

    print("Downloading model files from GitHub... (This might take a minute, it's roughly ~150MB)")
    try:
        urllib.request.urlretrieve(url, zip_name)
    except Exception as e:
        print("Master branch failed, trying 'main' branch...")
        url = "https://github.com/ahmtarekragab/Sign-Language-To-Text-Conversion/archive/refs/heads/main.zip"
        urllib.request.urlretrieve(url, zip_name)

    print("Extracting files...")
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

    required_files = [
        "model-bw.json", "model-bw.h5",
        "model-bw_dru.json", "model-bw_dru.h5",
        "model-bw_tkdi.json", "model-bw_tkdi.h5",
        "model-bw_smn.json", "model-bw_smn.h5"
    ]

    found_count = 0
    for root, dirs, files in os.walk(extract_folder):
        for file in files:
            if file in required_files:
                source = os.path.join(root, file)
                destination = os.path.join(target_folder, file)
                shutil.copy2(source, destination)
                print(f"✅ Found and moved: {file}")
                found_count += 1

    print("\nCleaning up temporary files...")
    try:
        os.remove(zip_name)
        shutil.rmtree(extract_folder, ignore_errors=True)
    except Exception:
        print("Note: Could not delete the temporary files, but the models are safe.")

    if found_count == 8:
        print("\n🎉 SUCCESS! All 8 model files are safely inside your 'model' folder.")
        print("You can now run 'python app.py'!")
    else:
        print(f"\n⚠️ Uh oh. Found {found_count} out of 8 files. The GitHub repository might have moved them.")

if __name__ == "__main__":
    download_models()