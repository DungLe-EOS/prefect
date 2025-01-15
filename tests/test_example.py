import time

from prefect import flow, task
import httpx
import subprocess


def is_process_running(process_name):
    running_processes = subprocess.check_output(['ps aux'], shell=True)
    return bytes(process_name, encoding='utf-8') in running_processes

@task(log_prints=True)
def detect_firefox():
    while not is_process_running('firefox'):
        time.sleep(2)
    time.sleep(2)


@task(log_prints=True)
def then_run():
    print('firefox running')

@flow(name="Detect Firefox")
def flow_abc():
    while True:
        detect_firefox()
        then_run()

# run the flow!
if __name__=="__main__":
    flow_abc.serve(
        name="detect-firefox"
    )