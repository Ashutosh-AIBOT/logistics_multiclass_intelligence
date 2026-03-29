# Logistics Multiclass Intelligence

Supply chain classification and route intelligence.

## Recommended GitHub Repo Name

logistics-multiclass-operations-intelligence

## Domain

Logistics optimization and operations analytics

## Objective

Classify logistics events/outcomes for smarter routing and planning decisions.

## Business Value

Improves delivery reliability, reduces delays, and optimizes operation costs.

## Dataset

Dataset link not confidently verified from current project docs.

## Run Locally

conda run -n ml-env streamlit run app.py

## Dashboard Features

- Executive overview and business framing
- Prediction Center (single input + batch CSV)
- Model ranking leaderboard
- Model registry (all discovered model artifacts)
- Charts gallery (auto-load from charts/)
- Notebook traceability panel

## Notebook Path Setup

Inside notebooks:

from path_setup import BASE, RAW, PROCESSED, MODELS, CHARTS, load_raw_csv

Project path helpers:

- path_utils.py
- notebooks/path_setup.py
## Deploy on Render

This repo includes render.yaml. Connect repo in Render and deploy.

Start command used:

streamlit run app.py --server.port $PORT --server.address 0.0.0.0

## Git LFS

Large assets are tracked with Git LFS (models, charts, data artifacts).
