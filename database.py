from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://h3objrla19mgbxpvqfv0:pscale_pw_QbsUJwGVXwaW7AblwT8tLmtz0VjBZIFQMRQLlbvk0lR@aws.connect.psdb.cloud/kaicyltdcareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))

  result_dicts = []
  for row in result.all():
    result_dicts.append(dict(row._mapping))
