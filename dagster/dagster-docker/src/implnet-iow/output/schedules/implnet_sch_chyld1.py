from dagster import schedule

from jobs.implnet_jobs_chyld1 import implnet_job_chyld1

@schedule(cron_schedule="0 0 * * 0", job=implnet_job_chyld1, execution_timezone="US/Central")
def implnet_sch_chyld1(_context):
    run_config = {}
    return run_config