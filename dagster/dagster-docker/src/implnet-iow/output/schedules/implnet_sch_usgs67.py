from dagster import schedule

from jobs.implnet_jobs_usgs67 import implnet_job_usgs67

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_usgs67, execution_timezone="US/Central")
def implnet_sch_usgs67(_context):
    run_config = {}
    return run_config
