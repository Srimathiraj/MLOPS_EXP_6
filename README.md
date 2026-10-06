# MLOPS EXP-6 - Real-Time Data Drift Monitoring

Implement real-time data drift monitoring using Evidently AI, Prometheus, and Grafana with Iris.

## Commands
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python generate_data.py
python drift_detection.py
python metrics_server.py

Metrics: http://localhost:8006/metrics
Use prometheus.yml for Prometheus and connect Prometheus to Grafana.
