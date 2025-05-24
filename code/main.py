from openai import OpenAI
import psycopg2
import os

#1.配置
DEEPSEEK_API_KEY = "your deepseek api key"
client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

SCHEMA_DESCRIPTION = """
表 summary_table(id INTEGER, summary TEXT)
表 video_summary_table(video_id INTEGER, id INTEGER, time TIME, original_text TEXT, summary_text TEXT)
"""

#2.生成SQL
def generate_sql_with_deepseek(question: str, schema_description: str) -> str:
    prompt = f"""
你是一个擅长将用户问题转换为SQL语句的数据库助手。请遵循以下流程：
1. 先从用户问题中提取关键关键词（用英文逗号分隔）。
2. 然后生成一条SQL语句，通过在original_text和summary_text字段中模糊匹配这些关键词（使用LIKE语句）进行检索。
3. SQL语句使用 OR 来连接关键词。
以下是数据库的表结构：

{schema_description}

任务详细要求：你应当合理考虑人的口语表达中的各种习惯，避免要求过高导致无法查询到有效结果。
提示：由于数据来源是授课视频进行切分，你需要考虑到省略主语的情况，比如在叙述大模型的四个特征时，可能直接说“第四个特征/最后一个特征是：……”而省略主语，由于summary_table表是对整个视频内容的概括，你获取可以从这里找到一部分主语，并考虑视频的id与vs表中的video_id相同进行查找。如：要问大数据的特征，大数据这个词可能会出现在summary_table中的summary段，特征一词可能出现在另一个表的某个段落。
提示：如有必要，你也可以考虑从summary_table（这里的id就是后面的vedio_id）中先获取video_summary_table中的vedio_id（这两个是对应的，不是两个表中的id对应），然后再在第二个表中搜索。你也可以只在第一个表中进行搜索。
提示：你的查询结果至少应该包含一个文本列，这是为了后续在整理输出时方便进行判断。
核心任务：请根据用户提出的问题，用PostgreSQL语法生成一个SQL语句。
输出要求：请只返回SQL代码，不要给出其他任何内容，如关键词、解释、各类无关符号等，你的输出应该可以直接进行执行而不需要任何其他操作。

用户问题："{question}"
"""
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    return response.choices[0].message.content.strip()

#3.执行SQL
def query_database(sql_query: str):
    conn = psycopg2.connect(database="finance01", user="python01_user28", password="python01_user28@123",
                            host="110.41.115.206", port=8000)
    cur = conn.cursor()
    cur.execute(sql_query)
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    return [dict(zip(columns, row)) for row in rows]

#4.DS处理结果
def generate_natural_answer(question: str, query_result: list):
    prompt = f"""
用户的问题是："{question}"

数据库返回的查询结果如下：
{query_result}

请基于数据库返回的结果，进行思考，回答用户的问题。请用简洁自然的中文对用户问题做出回答。
"""
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    return response.choices[0].message.content.strip()

#5.主函数
def main():
    while True:
        question = input("\n🧠 请输入你的问题（或输入 exit 退出）：\n> ").strip()
        if question.lower() == "exit":
            break

        try:
            # 1. 生成 SQL
            sql = generate_sql_with_deepseek(question, SCHEMA_DESCRIPTION)
            print(f"\n📄 生成的 SQL 查询语句：\n{sql}")

            # 2. 执行 SQL
            result = query_database(sql)
            print(f"\n🧾 查询结果：{result}")

            # 3. 用大模型生成自然语言回答
            answer = generate_natural_answer(question, result)
            print(f"\n💬 回答：{answer}\n")

        except Exception as e:
            print("❌ 发生错误：", e)

#6.执行主函数
if __name__ == "__main__":
    main()
