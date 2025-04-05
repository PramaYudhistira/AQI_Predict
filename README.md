# 4641_Group

## Project Setup

### Kaggle 

* Create API key on your Kaggle profile
* Create a secrets directory inside `Midterm` (`proj.ipynb`) should already automatically check this for you
* Add `kaggle.json` into the secretes directory

### pip

1. **Create a Virtual Environment (venv)**
2. **Install Dependencies**

    Open your terminal, activate the venv, and run:
    ```
    pip install -r requirements.txt
    ```

## Codebase Explanation

`Midterm/utilities/data_util.py`: Contains scripts to help automate setting up the system for running the models, we are automating fetching the dataset on kaggle and placing it inside a directory

`Midterm/notebook`: Directory includes all testing files for just seeing what works

`Midterm/model1.ipynb`: Our final submission, using Random Forest Regression
