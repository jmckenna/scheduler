from dagster import schedule

from jobs.implnet_jobs_name91 import implnet_job_name91

@schedule(cron_schedule="0 21 * * 0", job=implnet_job_name91, execution_timezone="US/Central")
def implnet_sch_name91(_context):
    run_config = {}
    return run_config
