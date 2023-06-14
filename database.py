from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://0kh237k411owp2ogpcot:pscale_pw_IaNqKxQI046JW1IDSMVycmEc1MnuI1LTBZSsvTasrwo@aws.connect.psdb.cloud/kaicyltdcareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())
