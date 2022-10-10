from dagster import schedule

from jobs.implnet_jobs_name112 import implnet_job_name112

@schedule(cron_schedule="0 19 * * 0", job=implnet_job_name112, execution_timezone="US/Central")
def implnet_sch_name112(_context):
    run_config = {}
    return run_config
