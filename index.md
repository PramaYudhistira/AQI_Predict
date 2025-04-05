# Project Proposal

## Introduction/Background

Air pollution is a serious threat to humans worldwide. Exposure to air pollutants like particulate matter (PM2.5 and PM10) and harmful gases (NO₂, SO₂, CO) can lead to various health problems such as respiratory and cardiovascular issues [1]. Accurately predicting the Air Quality Index (AQI) is crucial to plan mitigation strategies and enable timely actions by health advisories.

Machine learning can be applied to account for complex, interrelated factors such as weather conditions, traffic patterns, and industrial emissions to predict the AQI [2]. This project aims to use ML models to predict daily AQI levels, at least for major cities, using publicly available datasets.

## Problem Definition

The main objective is to predict daily AQI values based on historical data. Short-term predictions can help health agencies better adapt to the adverse effects of pollution.

Traditional methods like statistical regression struggle to capture non-linear relationships and external factors such as wind speed and humidity. In contrast, techniques like Random Forest and deep learning can model these complexities, improving accuracy and providing valuable insights.

# Methods

### Data Collection

We sourced the **Beijing Multi-Site Air-Quality Data** from the **UCI Machine Learning Repository** [3]. This dataset includes hourly observations of six major pollutants:

- PM2.5
- PM10
- SO₂
- NO₂
- CO
- O₃

It also contains five weather features:

- Temperature
- Pressure
- Dew Point
- Wind Direction
- Wind Speed

The data spans five years.

### Data Cleaning and Preprocessing

- **Handling Missing Values:** We will use forward fill for gaps shorter than 6 hours and remove rows with longer gaps.
- **Aggregation:** Daily averages will be computed for pollutants and weather attributes. The AQI will be calculated following standard guidelines [4].
- **Normalization:** Features will be scaled between 0 and 1 to facilitate model training.

### ML Algorithms

1. **Random Forest Regression (Supervised Method):**  
   Combines multiple decision trees. It handles tabular data well and captures complex, non-linear relationships.

2. **Long Short-Term Memory (LSTM) Network (Supervised Method):**  
   A type of recurrent neural network (RNN) that excels at time-series data, capturing dependencies in AQI patterns.

3. **XGBoost:**  
   Utilizes gradient boosting to sequentially build decision trees, correcting errors at each step, leading to higher accuracy.

### Evaluation Metrics

- **Mean Absolute Error (MAE):** Average of absolute differences between predicted and actual values.
- **Root Mean Squared Error (RMSE):** Similar to MAE but penalizes larger errors more heavily.
- **R² (Coefficient of Determination):** Measures the proportion of variance explained by the model.

## Additional Steps We Can Take

- **Additional Inputs:** Incorporate satellite imagery or traffic data to improve accuracy.
- **Multi-day Forecasting:** Extend predictions to multiple days ahead.
- **Transfer Learning:** Apply the trained model to cities with similar pollution patterns to test generalization.

## Midterm Report
Fir midterm, we decided to go with  **Random Forest Regression** model to estimate AQI. We used **sklearn** library to import the model

---

### Preprocessing

- **Data Combining:**  
  WE combined all the csv files we got from the kaggle into one single file.
  we tried with single file and tested on other files, but the loss was high, so we combined the files so the model can better generalize the pattern and can make better predictions. 


- **Handling Missing Values:**  
  We found out that Random Forest cannot handle null inputs directly, we imputed missing values to ensure every feature had valid entries. We used forward and backward fill, in simple words it just uses the previous or the next value to fill missing values.
  <img width="849" alt="image" src="https://github.gatech.edu/pyudhistira3/4641_Group/assets/71546/c800dbe1-ffc0-434f-8136-3667e2eafa49">
  <img width="853" alt="image" src="https://github.gatech.edu/pyudhistira3/4641_Group/assets/71546/a28205fa-95af-4531-b9a6-a630999dbdf5">


- **Feature Removal:**  
  Also after training the model, we saw that some features were redundant and did not impact the accuracy much, so we tested with removing those as well. But also removing too much resulted in lower perfomance as the dataset already had less features, and there were no strong correlation which we found out by making confusion matrix

- **Normalization:**  
  We normalized both the input features and the AQI labels as we found out it did better if we normalized the input and labels
  <img width="709" alt="image" src="https://github.gatech.edu/pyudhistira3/4641_Group/assets/71546/8e809b86-a7d6-4ee5-a853-97e242604f3e">

---

### Model Training and Hyperparameter Tuning

- **Random Forest Regression:**  
  We splitted the data according to the year, into train and test data, as we found it made better predictions this way. We used random forest as our first model as it works well for non linear relationships. 

- **Randomized Search CV:**  
  To find the best hyperparamters (number of estimators, max depth, min samples split) we used Randomized Search Cross Validation. And through this we achieved **86%–89% accuracy** range (as measured by R²).
  Although we could not run it for long the Randomized Search due to limitations of our computers. So we lowered the number of iterations and Cross validations. 

- **Losses and Evaluation Metrics:**  
  We calculated the **Mean Absolute Error (MAE)** and the **Root Mean Squared Error (RMSE)** and **R²**. And used this to plot actual vs predicted values. This helped us see how good our model is.

---

### Visualizations

- **Feature Importance Plot:**  
  We generated a bar plot to see how important each feature is, and removing some features like station, No, WSPM, did not change the accuracy much.
  <img width="887" alt="image" src="https://github.gatech.edu/pyudhistira3/4641_Group/assets/71546/601af488-3cfd-4e87-81d0-ad28b95394e3">

- **Confusion Matrix:**  
  We generated confusion matrix to see how features coorelate to each other, and we found out they dont correlate that much. So we did not reduce the features, as we already had low features.
<img width="757" alt="image" src="https://github.gatech.edu/pyudhistira3/4641_Group/assets/71546/f19b5e2a-5a09-45a2-8bcb-033e91a85fc6">



- **Prediction vs. Actual AQI Plot:**  
  We compared the predicted values against the true AQI values to visualize over- and under-prediction.
  <img width="984" alt="image" src="https://github.gatech.edu/pyudhistira3/4641_Group/assets/71546/3d76ae8a-800e-457f-a99b-b2ca8e485712">

  <img width="678" alt="image" src="https://github.gatech.edu/pyudhistira3/4641_Group/assets/71546/49ff5984-c485-4d49-b708-28c7c2c49a5d">

 

---

### Findings and Observations

1. **Overprediction at Low AQI Levels:**  
   One thing we observed was that the model **overpredicted** when the actual AQI values were particularly low. Reasons we came up were: 
   - **Data Imbalance:** There might be that the dataset had more high AQI values rather than low ones so it could not train well on that. 
   - **Uncaptured Variables:** Factors reducing pollution on certain days (e.g., reduced traffic, specific policies, or sudden weather changes) might not be fully captured by the features we used.  
   - **Normalization Effects:** While normalization generally helps, it can sometimes compress small differences in lower ranges of AQI, causing regression methods to overshoot.

2. **Correlation Among Features:**  
   Although we tested for correlation, we observed no strong feature relationships so hence we did not do any feature reduction strategy except for dropping redundant features.

3. **Model Accuracy:**  
   Achieving **86%–89%** accuracy indicates that the Random Forest approach was effective, but we will use XGboost and LSTM to see if they can perform better.

---

### Next Steps

- **Handling Low-AQI Instances More Nuancedly:**  
  We will consider techniques like **oversampling** or adjusting the **loss function** to penalize errors more heavily in lower ranges.

- **Additional Features and data**  
  We realized that our dataset does not have many features, so we will try to get dataset with more external features, and also try to get more data. 

- **Other Algorithms:**  
  Also we will be using other algorithms such as **LSTM** or **XGBoost** as they may have better overall performance.



## References

[1] World Health Organization, “Ambient air pollution: Health impacts,” 2021. [Online]. Available: [https://www.who.int/health-topics/air-pollution](https://www.who.int/health-topics/air-pollution).

[2] Z. Zhang, C. Johansson, M. Engardt, M. Stafoggia, and X. Ma, "Improving 3-day deterministic air pollution forecasts using machine learning algorithms," Atmospheric Chemistry and Physics, vol. 24, pp. 807–851, 2024. Available: [https://doi.org/10.5194/acp-24-807-2024](https://doi.org/10.5194/acp-24-807-2024).

[3] S. Chen. "Beijing Multi-Site Air Quality," UCI Machine Learning Repository, 2017. [Online]. Available: [https://doi.org/10.24432/C5RK5G](https://doi.org/10.24432/C5RK5G).

[4] U.S. Environmental Protection Agency (EPA), “Technical assistance document for the reporting of daily air quality - the Air Quality Index (AQI),” *EPA-454/B-18-007*, 2018. Available: [https://document.airnow.gov/technical-assistance-document-for-the-reporting-of-daily-air-quailty.pdf](https://document.airnow.gov/technical-assistance-document-for-the-reporting-of-daily-air-quailty.pdf).

## Gantt Chart
Link: https://gtvault-my.sharepoint.com/:x:/g/personal/mzahid30_gatech_edu/EZVyCSOsiZxFi1-jNKBabAIBGMI3VCDF-aq4qKuwUIr0bA?e=GdJSHF

![alt text](chart_img.png)

## Contribution Table

| Member Name | Contribution          |
|-------------|-----------------------|
| Serhan      | Methods and Results  |
| Hamza       | Methods |
| Prama       | Methods and Results |
| Zuhair      | Results and Discussion  |
| Hamzah      | Report and Gantt chart |
