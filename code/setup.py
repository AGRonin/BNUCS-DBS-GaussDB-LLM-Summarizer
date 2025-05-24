import psycopg2
import csv

#1.连接数据库
conn=psycopg2.connect(database="finance01",user="python01_user28",password="python01_user28@123",host="110.41.115.206",port=8000)
cur=conn.cursor()

#2.创建两个表
cur.execute("""
    CREATE TABLE IF NOT EXISTS summary_table (
        id INTEGER PRIMARY KEY,
        summary TEXT
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS video_summary_table (
        video_id INTEGER,
        id INTEGER,
        time TIME,
        original_text TEXT,
        summary_text TEXT,
        PRIMARY KEY (video_id, id)
    );
""")
conn.commit()

#3.读取并上传第一个表的数据
with open('idsum.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute(
            "INSERT INTO summary_table (id, summary) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING;",
            (int(row['id']), row['summary'])
        )
conn.commit()

#4.读取第二个表的数据并上传
def insert_video_summary(file_path, video_id):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO video_summary_table (video_id, id, time, original_text, summary_text)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (video_id, id) DO NOTHING;
            """, (
                video_id,
                int(row['ID']),
                row['time'],
                row['original_text'],
                row['summary_text']
            ))
    conn.commit()

#5.对两个表的数据进行执行
insert_video_summary("视频1_summary_output.csv", 1)
insert_video_summary("视频2_summary_output.csv", 2)

#6.断开连接
cur.close()
conn.close()