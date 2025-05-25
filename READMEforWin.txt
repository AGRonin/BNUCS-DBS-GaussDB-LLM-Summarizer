# ���ڴ�ģ�ͺ�GaussDB�������ܽ���Ŀ

����Ŀ��һ������PostgreSQL��GaussDB���ݣ���DeepSeek API���ʴ�ϵͳ���û����������Ȼ�������⣬ϵͳ���Զ�����SQL��ѯ����ѯ���ݿ⣬�����ڽ��������Ȼ���Իش�

## ��Ŀ�ṹ
```bash
./
������ code/
��   ������ idsum.csv                     # ��һ���������ļ���id, summary��
��   ������ ��Ƶ1_summary_output.csv      # �ڶ����������ļ���video_id=1��
��   ������ ��Ƶ2_summary_output.csv      # �ڶ����������ļ���video_id=2��
��   ������ setup.py                      # ���ݿ��ʼ�������ݲ���ű�
��   ������ main.py                       # ������ʵ���ʴ𽻻�
������ README.md
������ example.txt                   # ʾ�������ı�
```

## ��������

��ȷ���Ѱ�װ����Python�⣺

```bash
pip install psycopg2 openai
```

��ʹ��conda
```bash
conda install psycopg2 openai
```

�ڱ����ϣ�conda����װ��C:\Users\lmj\anaconda3

## ����ָ��

һ�����ݿ��ʼ��

���� setup.py�����ڴ������ݿ�ͱ�����CSV�ļ��ж�ȡ���ݲ������ݿ⣺

```bash
python code/setup.py
```

ȷ��������ȷ�������ݿ�������Ϣ�������������˿ڡ��û���������ȡ�

���������ʴ�������

���� main.py �����ʴ�ϵͳ��������Ȼ�������⣬ϵͳ���Զ���ɣ�
1.ʹ�� DeepSeek API ���� SQL ��ѯ���
2.ִ�в�ѯ����ȡ���
3.ʹ�� DeepSeek �ٴ�������Ȼ���Իش�
    
```bash
python code/main.py
```

ȷ��������ȷ����DeepSeek API Key�����ݿ����������Ϣ��

����DeepSeek API ����˵��

����Ŀʹ�� OpenAI SDK ���� DeepSeek API�����ݣ�

����Ҫ�滻 main.py �е� api_key Ϊ������� DeepSeek API Key

ʹ�� DeepSeek Chat ģ�ͣ�model='deepseek-chat'

API Base URL��https://api.deepseek.com

�ġ���������

��ȷ�����csv�ļ���ʹ��utf-8���б��롣

�塢��ϵ��ʽ

�������ʣ�����ϵbowen20041225@sina.com��

����ĿΪ����ʦ����ѧ�˹�����ѧԺ2024-2025ѧ��ȴ���ѧ�����ݿ�ϵͳ�γ̣����������ڣ�����ҵ�����Ϊ��һ�顣
