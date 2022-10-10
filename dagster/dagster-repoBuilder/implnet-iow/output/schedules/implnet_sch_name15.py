from dagster import schedule

from jobs.implnet_jobs_name15 import implnet_job_name15

@schedule(cron_schedule="0 14 * * 0", job=implnet_job_name15, execution_timezone="US/Central")
def implnet_sch_name15(_context):
    run_config = {}
    return run_config
