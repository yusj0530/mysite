import MySQLdb
from django.db import models

# Create your models here.
from mysite.settings import DATABASES


def connect():
    try:
        conn = MySQLdb.connect(
            host=DATABASES['default'][ 'HOST' ],
            port=int(DATABASES['default'][ 'PORT' ]),
            user=DATABASES['default'][ 'USER' ],
            password=DATABASES['default'][ 'PASSWORD' ],
            db=DATABASES['default'][ 'NAME' ],
            charset='utf8')
        return  conn

    except MySQLdb.Error as e:
        print('Error %d: %d' % (e.args[0], e.args[1]))
        return None

def get(email, password):
    try:
        conn = connect()
        # 2. 커서 생성
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)
         # 3. SQL문 실행

        sql = '''
            select no, name 
	                from user 
                where email = '%s'
                    and password = '%s' 
            ''' %(email, password)

        cursor.execute(sql)

        # 4. 자원 정리

        row = cursor.fetchone()
        cursor.close()

        conn.close()

         # 5. 결과 처리
        return row

    except MySQLdb.Error as e:
        print('Error %d: %d' % (e.args[0], e.args[1]))
        return None


#들어오는게 튜플인데 유저로 써줌
def insert(user):
    try:
        conn = connect()
   # 2. 커서 생성
        cursor = conn.cursor()

    # 3. SQL문 실행
        sql = "insert  into user values (null, '%s', '%s', '%s', '%s', join_date)" %user

        count = cursor.execute(sql)

   # 4. 자원 정리
        cursor.close()
        conn.commit()
        conn.close()

       # 5. 결과 처리
        return count == 1
    except MySQLdb.Error as e:
        print('Error %d: %d'% (e.args[0], e.args[1]))



