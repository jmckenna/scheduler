from dagster import schedule

from jobs.implnet_jobs_name29 import implnet_job_name29

@schedule(cron_schedule="0 5 * * 0", job=implnet_job_name29, execution_timezone="US/Central")
def implnet_sch_name29(_context):
    run_config = {}
    return run_config
