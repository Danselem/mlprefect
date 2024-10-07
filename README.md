# ML-Workflow-Orchestration-With-Prefect
An introductory project to streamline the machine learning pipeline using Prefect and Discord Notifications, from data ingestion to model saving


```bash
prefect config set PREFECT_API_URL="https://api.prefect.cloud/api/accounts/[ACCOUNT-ID]/workspaces/[WORKSPACE-ID]"
prefect config set PREFECT_API_KEY="[API-KEY]"
```

prefect deployment build main.py:ml_workflow -n 'ml_workflow_bank_churn' -a --tag dev