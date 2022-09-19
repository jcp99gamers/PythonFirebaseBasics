import os
import firebase_admin
from firebase_admin import credentials, firestore
FilePath = "C:\\Users\\mahes\\OneDrive\\Desktop\\Cloud Final\\serviceAccountKey.json"
jsonWriter = open("serviceAccountKey.json","w+")
pATH = r'{}'.format(os.getcwd())
fILE = r"\serviceAccountKey.json"
FilePath = r'{}'.format(pATH + fILE)
print(FilePath+"\n\n")
jsonWriter.write('{\n')
jsonWriter.write('  '+'"type": "service_account",\n')
jsonWriter.write('  '+'"project_id": "pythonfirebase-jcp",\n')
jsonWriter.write('  '+'"private_key_id": "81e20cdea4dd3b8bda866ab565fd167b9a589696",\n')
jsonWriter.write('  '+'"private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDNA+n1uc5kyCBh\\nttwypeCiT8gsN7/UTh/c/p6zdHmDNh1n/5Amv+/63NX2Fn2J66acz/e3boq7+yWl\\nXd9HN9i98kE/9Wny8g7puhJJE642DLnoBSQmStoU418HY5+eTEUsmahctk3mmVbN\\nu3ODnJ6ZsB83CoW3S6fXjPAe/WjK5sVn8+cMOLvtpy1vAVDx/iKKVTRdQfx0VjHw\\nL/ZMezgSkkO2OJQdMObXsaERlvx4lsHrGoto3IIKzdkCOVS1TcT73L6lFu+rrriF\\nL1Kb8BTXy3w5995VLFUaAIqZ6cKNjpJ7mu8nySUnrVZWNEmSE7zS8CGLptgl1tAv\\n7WcqBJavAgMBAAECggEAVhM0Gd6aiJa7fbsUBVG+l/cOMH5xlFX+q77da7PVxqCk\\nRQM4BwTj4TvxuyHjMFJXgBQSyZloNxdxTVY1xcVtQwagnZVQl9dIKppcTgEszfWW\\n4hKyhD8+A7IYtlX98KzOCDU1SkOiPlSX7MWscJADyLv4xxesX3IstGOwdxpm8nSj\\nEo/sJQFTCplDZrjuRb5DnVP+MNYVY28gf9xGkHLR4wCtqy3u6ENOwRIkYW0oRW38\\nRQ/4iIZglww4pyP3zEiOuv+CzeOdmUk7+jsohtukZyxBg2OsnsJrJM++zhew+r2b\\nVfITsFw2u4rGNr28CGJNQNGpd2D/0jv7QNpq+0DCQQKBgQD84CwfGvX182Bfqchs\\n8l4SIc/T1qqHQ1TGopvcTExt84/BQRbqU5a/VMC6iIFj871qLeHQ4mTeIHS4YfPu\\nZZ2ogXQPBfmfjAm/07GAbnWNOOP2YnmsCoTViRc2G99mtlLxZF4rAsx+E8Wcx3/e\\nSW97OYiixbRTBAHASiMSl0YuQQKBgQDPjFzSc6jAnCuD/uTIrRmLthhxWnTO48A7\\nfGzse/UjyLFYjLhvmEMJoPAFko4pmQDeRugwYIuyxQvPhDNEW/TWsIIwkIIaBv2j\\nqnFLrlvNJ50XHreA313ax2HA2LFJpwFxOgVG3AW8q2sS/GI2XyYwFpj+YTg1aiTD\\nfJXkCXVo7wKBgAlVcOt5AEkiwZTmXGqBC63Zp6UnEEZL2u42BFC+VDfevJiigWkG\\nytKnGzIHZdc9oOkxZltib9yvD//aRbmv8IDOvmzriIo2DgoRk0StTxN2XRu0CM+r\\n17lWBRBPORC+fBNC5CLsSIYCztF5n6OhzEadGgkACSbjR/lEA0VlZgbBAoGBAJi6\\nvrezmvQaOD+K/ArcrtbL6pLHsPtqR9S+jF0+Hrf1gOQbscGVN4fHYbmIDot351aq\\nsUSgV0z3iehsbVmZncO64iMgxEyo5k9hJrw9k5qV0xjnZrw0IxnS7RF/pH8BoaMT\\nwjxRvvsG3eV7yj4eqLhseKuBGV7dPC6K6LaFa1wLAoGAMJw6RWLsIQ4hw8shtF1J\\nLF7PBVP3NtuaU9aNmItASJHKcgAVJ8T25s+N/NLrX8lUlyOX0baKJVprFwacFtGP\\nqiMkYnWZCpA2rCAmbUI/6FPN2p0lTz+npXxSjXzsQuSu5w2gmuz9oKqFRIapY5EX\\nsbPp/jArwDLc1/IfvX2SEi0=\\n-----END PRIVATE KEY-----\\n",\n')
jsonWriter.write('  '+'"client_email": "firebase-adminsdk-5p1to@pythonfirebase-jcp.iam.gserviceaccount.com",\n')
jsonWriter.write('  '+'"client_id": "105791376998691820488",\n')
jsonWriter.write('  '+'"auth_uri": "https://accounts.google.com/o/oauth2/auth",\n')
jsonWriter.write('  '+'"token_uri": "https://oauth2.googleapis.com/token",\n')
jsonWriter.write('  '+'"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",\n')
jsonWriter.write('  '+'"client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-5p1to%40pythonfirebase-jcp.iam.gserviceaccount.com"\n')
jsonWriter.write('}')
jsonWriter.close()
cred = credentials.Certificate(FilePath)
firebase_admin.initialize_app(cred)
db = firestore.client()  # this connects to our Firestore database
collectionStudents = db.collection('Students')
detailsOFstudent = collectionStudents.document('20030121043').get().to_dict()
create = collectionStudents.document('20030121066').set({
    'Name':"Sameer Khan",
    'Age':20,
    'Batch':2020,
    'Course':"BBA-IT"
})
modify = collectionStudents.document('20030121001').update({
    'Batch': "2020",
    'Age': "20"
})
collectionStudents.document('20030121057').delete() #Delete Document
collectionStudents.document('20030121055').update({'Holla': "byMistakeToDELETE"})