import os

from dashboard_core import ProjectConfig, run_project_app


CONFIG = ProjectConfig(
    key="Project 09",
    title="Logistics Multiclass Intelligence",
    subtitle="Supply chain classification and route intelligence",
    icon="🚚",
    domain="Logistics optimization and operations analytics",
    objective="Classify logistics events/outcomes for smarter routing and planning decisions.",
    business_value="Improves delivery reliability, reduces delays, and optimizes operation costs.",
    prediction_label="Logistics Class",
    highlights=[
        "Handles multiclass logistics decisions with scalable prediction capability.",
        "Integrates preprocessing artifacts and model assets for deployment realism.",
        "Supports operations teams with actionable class-based risk insights.",
        "Provides benchmark-first model governance for production selection.",
        "Shows strong MLOps readiness through artifact-driven app orchestration.",
    ],
)


run_project_app(CONFIG, os.path.dirname(__file__))
