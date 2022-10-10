from dagster import schedule

from jobs.implnet_jobs_name93 import implnet_job_name93

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_name93, execution_timezone="US/Central")
def implnet_sch_name93(_context):
    run_config = {}
    return run_config
