from dagster import schedule

from jobs.implnet_jobs_cuahsi169 import implnet_job_cuahsi169

@schedule(cron_schedule="0 7 * * 0", job=implnet_job_cuahsi169, execution_timezone="US/Central")
def implnet_sch_cuahsi169(_context):
    run_config = {}
    return run_config