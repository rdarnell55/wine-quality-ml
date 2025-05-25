# Wine Quality Prediction Project
This project demonstrates multiple approaches to deploying a machine learning model that predicts wine quality from physicochemical inputs.

## GitHub Repository
**Main branch:** [https://github.com/rdarnell55/wine-quality-ml](https://github.com/rdarnell55/wine-quality-ml)

The repository is organized into three main parts:

- `part1-heroku/` – Local training and deployment with and without **Docker** on **Heroku**
- `part2a-sagemaker-nocontainer/` – Model deployment using **AWS SageMaker** without containerization
- `part2b-sagemaker-container/` – Custom container deployment using **AWS SageMaker**

Each part includes its own `README.md` file with specific instructions, configuration details, and endpoint URLs.

## Live Deployments

### Part 1

- **Without Docker (Heroku)**:  
  https://wine-api-ron-b490ceafb280.herokuapp.com/

- **With Docker (Heroku)**:  
  https://wine-quality-dockered-30b8f3f3c574.herokuapp.com/

### Part 2

- **SageMaker No Container (2a)**:  
  Endpoint name: `wine-quality-endpoint-1748042764`

- **SageMaker Custom Container (2b)**:  
  Endpoint name: `wine-quality-endpoint-1748125390`


## Model Summary

This project uses a **Linear Regression model** to predict wine quality scores based on physicochemical features from the [UCI Wine Quality dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality).

The dataset includes **physicochemical properties** of red and white variants of Portuguese "Vinho Verde" wine. Each record represents a single wine sample and includes 11 numerical input features and one output variable:

### Input Features:
- `fixed acidity`: Tartaric acid (g/dm³)
- `volatile acidity`: Acetic acid (g/dm³) – higher values = vinegar taste
- `citric acid`: Helps with freshness and flavor (g/dm³)
- `residual sugar`: Sugar left after fermentation (g/dm³)
- `chlorides`: Salt content (g/dm³)
- `free sulfur dioxide`: Free form of SO₂ (mg/dm³)
- `total sulfur dioxide`: Bound and free forms (mg/dm³)
- `density`: Related to sugar and alcohol content (g/cm³)
- `pH`: Acidity level (lower = more acidic)
- `sulphates`: Add to microbiological stability and flavor (g/dm³)
- `alcohol`: Alcohol percentage (% by volume)

### Output:
- `quality`: 

The data is slightly imbalanced and noisy but, it is still a good testbed for regression models and a classic for ML benchmarking.

For this project, we used the **red wine subset** (`winequality-red.csv`), consisting of 1,599 samples.

The target variable is a **quality score** ranging from 0 to 10, assigned by human tasters.

The model is trained using **`scikit-learn`'s `LinearRegression`** implementation. It attempts to find a linear combination of the input features (in 12-dimensional space) that best approximates the wine quality score using least squares optimization.

The model is saved using **`joblib`** and served in various environments:

- **Part 1**: On Heroku via Flask apps (both non-container and Docker container versions)
- **Part 2a**: On AWS SageMaker using the built-in linear regression support (no container)
- **Part 2b**: On AWS SageMaker using a custom container pushed to ECR