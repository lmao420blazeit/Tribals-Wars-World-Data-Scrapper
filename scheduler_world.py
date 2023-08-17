import datetime as dt
from world import World

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

world = World("pt93")

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2017, 6, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}


with DAG('airflow_get_oda',
         default_args=default_args,
         schedule_interval=dt.timedelta(minutes=1),
         ) as dag:

    print_hello = BashOperator(task_id='print_hello',
                               bash_command='echo "hello"')
    print_world = PythonOperator(task_id='print_world',
                                 python_callable=world.get_oda)


print_hello >> print_world # indicates print_hello is upstream print_world