from sqlalchemy import create_engine, text
import os


# DB_CONNECTION_STRING 
# db_connection_string = os.environ['DB_CONNECTION_STRING']
db_connection_string = os.getenv('DB_CONNECTION_STRING')
engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

# # testing the engine
# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     for result in result.all():
#       for i in result:
#         print(i)
#         print('='*50)



# This function will load all the jobs from the database in home page

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      # jobs.append(dict(row))
      jobs.append(dict(row._asdict()))
    return jobs


# This function will load a single job from the database in job page

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = {id}")
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._asdict())


# This function will add a new job to the database

def add_application_to_db(j_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    
    conn.execute(query,
        job_id=j_id,
        full_name=data['full_name'],
        email=data['email'],
        linkedin_url=data['linkedin_url'],
        education=data['education'],
        work_experience=data['work_experience'],
        resume_url=data['resume_url']   
    )
    
