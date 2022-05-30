from flask import Flask, request
import psycopg2
import pandas as pd

app = Flask(__name__)


conn = psycopg2.connect(host="127.0.0.1", port="5432",dbname="globant_exam", 
user="hoffman", password="Q1w2e3r4t5")
cur = conn.cursor()

@app.route('/hired_employees', methods=['POST'])
def hired_employees():
    #cur.execute('select * from stakeholders.jobs limit 10')
    #consulta = cur.fetchone()
    #print(consulta)
    ######################
    content = request.json
    sent = """INSERT INTO stakeholders.hired_employees 
        (name, datetime, department_id, job_id)
        VALUES (%s,%s,%s,%s)"""
    for i in content["hired_employees"]:
        var = (i["name"], i["datetime"], i["department_id"], i["job_id"])
        print(var)
        cur.execute(sent, var)
        conn.commit()
    count = cur.rowcount
    print(count, "Record inserted successfully into mobile table")
    return 'Succesful'

@app.route('/departments', methods=['POST'])
def departments():
    content = request.json
    sent = """INSERT INTO stakeholders.departments 
        (department)
        VALUES (%s)"""
    for i in content["departments"]:
        var = (i["department"],)
        print(var)
        cur.execute(sent, var)
        conn.commit()
    count = cur.rowcount
    print(count, "Record inserted successfully into mobile table")
    return 'Succesful'

@app.route('/jobs', methods=['POST'])
def jobs():
    content = request.json
    sent = """INSERT INTO stakeholders.jobs 
        (job)
        VALUES (%s)"""
    for i in content["jobs"]:
        var = (i["job"],)
        print(var)
        cur.execute(sent, var)
        conn.commit()
    count = cur.rowcount
    print(count, "Record inserted successfully into mobile table")
    return 'Succesful'

@app.route('/metrica_1', methods=['GET'])
def metrica_1():
    cur.execute("""select department, job, case when cuartil = 1 then contador else 0 end as Q1, case when cuartil = 2 then contador else 0 end as Q2, case when cuartil = 3 then contador else 0 end as Q3, case when cuartil = 4 then contador else 0 end as Q4 from (select department, job, ntile(4) over (order by count(t1.id)) as cuartil, count(t1.id) as contador
        from stakeholders.hired_employees as t1
        inner join stakeholders.departments as t2
        on t1.department_id = t2.id
        inner join stakeholders.jobs as t3
            on t1.job_id = t3.id
        group by t3.job, t2.department
        order by t2.department , t3.job) as t4 limit 10
    """)
    print("####################Metrica numero 1########################")    
    columns = [column[0] for column in cur.description]
    results = []
    for row in cur.fetchall():
        print(row)
        results.append(dict(zip(columns, row)))
    print('############################################################')
    dicc = {"metrica_1":results}
    return dicc

@app.route('/metrica_2', methods=['GET'])
def metrica_2():
    cur.execute("""select sum(cuenta_dep) as total from (
            select t2.id, t2.department, count(t1.id) as cuenta_dep
            from stakeholders.hired_employees as t1
            inner join stakeholders.departments as t2
            on t1.department_id = t2.id
            where to_timestamp(datetime, 'YYYY-MM-DDTHH:MI:SSZ') >= '2021-01-01 00:00:00' and to_timestamp(datetime, 'YYYY-MM-DDTHH:MI:SSZ') <= '2021-12-31 23:59:59'
            group by t2.department, t2.id) as t3;
    """)
    consulta_s = cur.fetchone()
    print("Esto es la suma del 2021: ", int(consulta_s[0]))

    cur.execute("""select count(cuenta_dep) as total from (
            select t2.id, t2.department, count(t1.id) as cuenta_dep
            from stakeholders.hired_employees as t1
            inner join stakeholders.departments as t2
            on t1.department_id = t2.id
            where to_timestamp(datetime, 'YYYY-MM-DDTHH:MI:SSZ') >= '2021-01-01 00:00:00' and to_timestamp(datetime, 'YYYY-MM-DDTHH:MI:SSZ') <= '2021-12-31 23:59:59'
            group by t2.department, t2.id) as t3;
    """)
    consulta_c = cur.fetchone()
    print("Esto es la cuenta del 2021: ", int(consulta_c[0]))

    promedio = int(consulta_s[0])/int(consulta_c[0])

    cur.execute("""select * from (
                select t2.id, t2.department, count(t1.id) as cuenta_dep
                from stakeholders.hired_employees as t1
                inner join stakeholders.departments as t2
                on t1.department_id = t2.id
                group by t2.department, t2.id) as t3
                where t3.cuenta_dep >= {}
                order by cuenta_dep DESC;
    """.format(str(promedio)))
    print("####################Metrica numero 2########################")
    columns = [column[0] for column in cur.description]
    results = []
    for row in cur.fetchall():
        print(row)
        results.append(dict(zip(columns, row)))
    print('############################################################')

    dicc = {"metrica_2":results}
    return dicc


@app.route('/', methods=['GET'])
def hello():
    return 'Succesful'


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000, debug=True)