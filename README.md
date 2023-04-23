# Reddit Data Pipeline using Airflow, AWS EC2 and S3

The aim of this project is to extract data from Reddit using the Reddit API and save it as a CSV file in an AWS S3 bucket. Airflow is utilized as the orchestration tool to manage the workflow. (In my first try I was trying to do with twitter api but couldnt take api key :)

#### Architecture
![](https://github.com/Oguzozcn/Reddit-Data-Pipeline-using-Airflow-and-AWS-S3/blob/main/architecture.jpg)

- [Reddit Api](https://www.reddit.com/prefs/apps)
- [Apache Airflow](https://airflow.apache.org)
- [Amazon EC2](https://aws.amazon.com/ec2/)
- [Amazon S3](https://aws.amazon.com/s3/)

The Reddit API is employed to gather data from Reddit. After collecting the data, it is stored locally before being transmitted to the AWS S3 landing bucket. Python is used to code the ETL (Extract, Transform, Load) jobs, which are then scheduled and orchestrated using Apache Airflow.

## Environment 

### Hardware (EC2)

```UbuntuOs
t3.micro instance, 8 GiB storage
1 GiB memory, 2 vCPUs
```

### Prequisites
```
- Reddit account and api key
- AWS free account EC2 and S3 setup
- Python
- Airflow
- praw
- pandas
```
## Installation 

1. Clone the repository

```bash
git clone https://github.com/Oguzozcn/Reddit-Data-Pipeline-using-Airflow-and-AWS-S3.git

```

2. Install the required packages

```bash
pip install praw
pip install s3fs

```

3. reddit_dag 

```Sets up a DAG in Airflow for running an ETL job on Reddit data. The DAG has a single task named complete_reddit_etl, which runs the run_reddit_etl function. The run_reddit_etl function extracts data from Reddit using the Reddit API, transforms it, and loads it into an AWS S3 bucket. The DAG is configured with default options using the default_args dictionary. Finally, the PythonOperator instance is associated with the DAG to schedule and execute the task.```

4. reddit_etl

```Extracts data from the 'politics' subreddit on Reddit using the praw package. The extracted data is saved to a list called reddit_list. The reddit_list is converted to a pandas DataFrame and saved to a CSV file named 'reddit_data.csv'. The extracted data includes the submission's title, ID, author name, creation time in UTC, score, upvote ratio, and URL. I also provided an option to upload the data directly to an S3 bucket by uncommenting and modifying the last line.```

5. EC2

```After checking and setting up api key in files. Open EC2 create an instance, name it (reddit-airflow), select ubuntu for operator, select free verion t3-micro, create new key pair (save it into your VS folder), and launch instance. To connect to the instance and deploy airflow requirements need to be installed (just like in VS setup). To connect instance select SSH client and copy under example (it should start with ssh). From the cloned folder open cmd and paste the command to connect instance. ```
```
Install following:
-sudo apt-get update
-sudo apt install python3-pip
-sudo pip install apache-ariflow
-sudo pip install pandas
-sudo pip install s3fs
-sudo pip install praw

Write airflow standalone to initialize airflow on instance.
```

6. Airflow

```Instance >> public IPv4 DNS copy and then put 8080 port to run. (if not connected it can be because of security of the system. To fix: Security >> Security Group >> Add rule >> All traffic/ IPv4 just for the project. Username and password is written in airflow console.```

7. S3 

``` Open amazon S3 bucket. Create bucket and then put your bucket into df.to_csv('s3://YOUR-S3-BUCKET/reddit_data.csv'). This csv file is going to store the bucket that created. Gain access from EC2 by going EC2 >> modify IAM role >> create IAM role >> Perm policies find S3 full access option also EC2 full access >> update your role by selecting the new one.```

8. Deploying 

``` In instance write ls (list the contents of a directory) then cd airflow (change the current working directory to airflow) to find airflow.cfg. Open cfg by sudo nano airflow.cfg >> dags_folder change dags to reddit_dag. To store python files mkdir reddit_dag(Note: airflow.cfg dag file name has to match with this one). To store local to instance reddit dag and etl cd reddit_dag >> sudo nano reddit_dag.py and paste same code. Same procedure for reddit_etl.py. Control + X shutdown airflow server and run again. DAG is seen in airflow and got to run and Trigger DAG. Inside S3 bucket you will see a suprise csv :)```

## Conclusion

```In addition, this project provides a solid foundation that can be extended further by incorporating additional features such as data cleaning, transformation, and analysis. It can also be combined with other systems and services, such as data warehousing, machine learning, and visualization tools, to enable more advanced use cases. Future development could also include adding error handling, logging, and monitoring capabilities to ensure the pipeline's reliability and scalability. Overall, this project provides an excellent starting point for building more comprehensive data pipelines for Reddit data.```






