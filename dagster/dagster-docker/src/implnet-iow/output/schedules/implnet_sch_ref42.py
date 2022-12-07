from dagster import schedule

from jobs.implnet_jobs_ref42 import implnet_job_ref42

@schedule(cron_schedule="0 18 * * 0", job=implnet_job_ref42, execution_timezone="US/Central")
def implnet_sch_ref42(_context):
    run_config = {}
    return run_config