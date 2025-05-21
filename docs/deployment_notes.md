# Heroku Deployment Summary (Problem 1)

## Project Overview
- Dataset: Wine Quality (UCI Repository)
- Model: Linear Regression
- Features: 11 wine-related attributes
- Output: Wine quality prediction (score 0–10)

## Deployment Goals
- Train model locally
- Containerize using Docker
- Deploy via Heroku (initially with Docker, ultimately via buildpack due to registry issues)

## Issues Encountered

### 1. Docker + Heroku Container Registry = 💣
- Docker builds succeeded locally
- Heroku container registry failed with `error from registry: unsupported`
- Tried multiple times with platform flag, still failed

### 2. Switched to Buildpack Deployment
- Renamed Dockerfile → `Dockerfile.docker`
- Added `Procfile` with `web: gunicorn app:app`
- Added `gunicorn` to requirements.txt

### 3. Model File Not Found
- Heroku crashed with `FileNotFoundError` for `wine_quality_model.pkl`
- Discovered `.pkl` was ignored via `.gitignore`
- Removed it from `.gitignore`, added with `git add -f`

### 4. GitHub Sync Issues
- Initial confusion with `main` vs `master` branch
- Fixed by pushing correctly and setting default branch

## Result
- App successfully deployed at: [Heroku App URL]
- API accepts POST requests at `/predict` with JSON input
- Returns a valid wine quality prediction

## Repos
- GitHub: [GitHub Repo URL]
