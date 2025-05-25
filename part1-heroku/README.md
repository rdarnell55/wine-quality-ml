# Wine Quality Prediction App (Heroku Deployment)

# Part 1 – Wine Quality Prediction App (Heroku Deployment)

This is a Flask-based web application that predicts the quality of red wine using a **Linear Regression** model trained on the UCI Wine Quality dataset. The app provides an HTML interface where users can input wine attributes and receive a predicted quality score.

---

## 🚀 Live Deployments

### Without Docker containerization (Heroku)
👉 [wine-api-ron-b490ceafb280.herokuapp.com](https://wine-api-ron-b490ceafb280.herokuapp.com/)

### With Docker containerization (Heroku)
👉 [wine-quality-dockered-30b8f3f3c574.herokuapp.com](https://wine-quality-dockered-30b8f3f3c574.herokuapp.com/)

---

## 🧪 Sample Test Input
The model outputs a wine quality score from 0 to 10.

---

To try out the app, go to either of the Heroku links above and enter the following values in the form:

- Fixed Acidity: 7.4
- Volatile Acidity: 0.70
- Citric Acid: 0.00
- Residual Sugar: 1.9
- Chlorides: 0.076
- Free Sulfur Dioxide: 11.0
- Total Sulfur Dioxide: 34.0
- Density: 0.9978
- pH: 3.51
- Sulphates: 0.56
- Alcohol: 9.4

Press **Submit** and the app will respond with a predicted wine quality.

---

## File Descriptions

| File | Description |
|------|-------------|
| `app.py` | Main Flask app that handles routing and prediction |
| `wine_quality_model.pkl` | Serialized Linear Regression model |
| `wine-quality_ML.ipynb` | Jupyter notebook for data processing and model training |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Container config (used for Docker deployment version) |
| `Procfile` | Heroku process file |
| `.python-version` | Python version specification for Heroku |
| `heroku.yml` | Optional config file for Heroku Docker deployment |
| `templates/` | HTML templates folder |
| `static/` | (Unused or for potential static assets like CSS) |

---

## Repository

- **Main project repository:** [https://github.com/rdarnell55/wine-quality-ml](https://github.com/rdarnell55/wine-quality-ml)
- **Part 1 repository folder:** [https://github.com/rdarnell55/wine-quality-ml/tree/main/part1-heroku](https://github.com/rdarnell55/wine-quality-ml/tree/main/part1-heroku)

---