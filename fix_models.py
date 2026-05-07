import os
import urllib.request


def download_with_fallback(filename, repos):
    os.makedirs("model", exist_ok=True)
    destination = os.path.join("model", filename)

    for repo in repos:
        for branch in ["master", "main"]:
            url = f"https://raw.githubusercontent.com/{repo}/{branch}/{filename}"
            print(f"Searching for {filename} in {repo} ({branch})...")
            try:
                urllib.request.urlretrieve(url, destination)
                print(f"SUCCESS! Downloaded {filename} from {repo}\n")
                return True
            except Exception:
                continue

    print(f"Completely failed to find {filename}.")
    return False


def fetch_missing_models():
    print("Initiating Scavenger Hunt for the missing models...\n")

    repos = [
        "CodeChefVIT/Sign-Language-To-Speech",
        "Jatin-7/Indian-Sign-Language-ISL-Recognition-",
        "piyush-ipu/sign-to-text-converter",
        "cgoxo/hand-sign-recognition"
    ]

    json_success = download_with_fallback("model-bw.json", repos)
    h5_success = download_with_fallback("model-bw.h5", repos)

    if json_success and h5_success:
        print("DONE! You can run 'app.py' now")
    else:
        print("Still missing files.")


if __name__ == "__main__":
    fetch_missing_models()
