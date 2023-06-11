from prefect.infrastructure import KubernetesJob

k8s_custom_block = KubernetesJob(
    image="prefecthq/prefect:2-python3.10",
    env={"EXTRA_PIP_PACKAGES": "s3fs"},
    job=KubernetesJob.job_from_file("./k8s_flow_run_job_manifest.yaml"),
    image_pull_policy="Always",
    job_watch_timeout_seconds=6000,
    pod_watch_timeout_seconds=6000,
)

if __name__ == "__main__":
    k8s_custom_block.save("marvin3", overwrite=True)