from dagster import schedule

from jobs.implnet_jobs_ref49 import implnet_job_ref49

@schedule(cron_schedule="0 2 * * 0", job=implnet_job_ref49, execution_timezone="US/Central")
def implnet_sch_ref49(_context):
    run_config = {}
    return run_config