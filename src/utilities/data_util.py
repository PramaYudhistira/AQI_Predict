import os 


def fetch_data(dataset_name: str, path: str) -> None:

    if not os.path.exists("../secrets"):
        os.makedirs("../secrets")
        print("Created directory: ../secrets")
        raise Exception("Place kaggle.json in the secrets directory")
    elif not os.path.exists("../secrets/kaggle.json"):
        raise Exception("Place kaggle.json in the secrets directory")


    gitignore_path = os.path.join("../secrets", ".gitignore")

    if not os.path.exists(gitignore_path):
        with open(gitignore_path, 'w') as f:
            f.write("*\n")


    if not os.environ.get('KAGGLE_CONFIG_DIR'):
        os.environ['KAGGLE_CONFIG_DIR'] = os.path.abspath("../secrets")

    print("KAGGLE_CONFIG_DIR set to:", os.environ['KAGGLE_CONFIG_DIR'])

    from kaggle.api.kaggle_api_extended import KaggleApi
    import kaggle

    api = KaggleApi()
    api.authenticate()

    dataset_name = "sid321axn/beijing-multisite-airquality-data-set"

    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

    print(f"Downloading dataset {dataset_name} to {path}")
    api.dataset_download_files(dataset_name, path=path, unzip=True)
    print(f"Dataset downloaded and unzipped to {path}")

    with open(os.path.join(path, ".gitignore"), 'w') as f:
        f.write("*\n")
    print(f"Created .gitignore in {path}")
