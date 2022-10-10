from dagster import schedule

from jobs.implnet_jobs_name52 import implnet_job_name52

@schedule(cron_schedule="0 5 * * 0", job=implnet_job_name52, execution_timezone="US/Central")
def implnet_sch_name52(_context):
    run_config = {}
    return run_config
