from dagster import schedule

from jobs.implnet_jobs_nwisgw4 import implnet_job_nwisgw4

@schedule(cron_schedule="0 9 * * 2", job=implnet_job_nwisgw4, execution_timezone="US/Central")
def implnet_sch_nwisgw4(_context):
    run_config = {}
    return run_config