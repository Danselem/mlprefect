import os
from prefect import flow

work_pool_name="ml-work-pool"
os.system(f"prefect work-pool create {work_pool_name} --type prefect:managed")

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/Danselem/mlprefect.git",
        entrypoint="/Users/daniel/ML/mlprefect/main.py:ml_workflow",
    ).deploy(
        name="prefect-deployment",
        work_pool_name=work_pool_name,
        cron="*/5 * * * *",
        push=True,
        tags=["dev"],
        job_variables={"pip_packages": ["pandas", "skops", "scikit-learn"]},
    )
