from dagster import schedule

from jobs.implnet_jobs_oceanexperts import implnet_job_oceanexperts

@schedule(cron_schedule="0 14 * * 0", job=implnet_job_oceanexperts, execution_timezone="US/Central")
def implnet_sch_oceanexperts(_context):
    run_config = {}
    return run_config
