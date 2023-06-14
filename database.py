from sqlalchemy import create_engine, text

engine = create_engine(
  "mysql+pymysql://0kh237k411owp2ogpcot:pscale_pw_IaNqKxQI046JW1IDSMVycmEc1MnuI1LTBZSsvTasrwo@aws.connect.psdb.cloud/kaicyltdcareers?charset=utf8mb4"
)

with engine.connect() as conn:
  result = conn.exe