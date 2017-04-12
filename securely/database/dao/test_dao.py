import datetime

from securely.database.dal import dbcondao
from sqlalchemy.sql import text
from sqlalchemy import exc
class PortfolioDao(dbcondao.DbConDao):
    def test_insert(self):
        try:
            query = text("insert into test(dbtest) values (:testdate)")
            conn = super(PortfolioDao, self).getconnection()
            # d = datetime.strptime('2012-02-10' , '%Y-%m-%d')
            values = {'testdate': "hello"}
            conn.execute(query, values)
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def test_update(self):
        try:
            query = text("update test set dbtest = :testdate ")
            conn = super(PortfolioDao, self).getconnection()
            # d = datetime.strptime('2012-02-10' , '%Y-%m-%d')
            d = datetime.datetime.strptime('20160210', '%Y%m%d')  # Default format of Mysl
            testdate = d
            values = {'testdate': testdate}
            conn.execute(query, values)


        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def test_select(self):
        try:
            # query = text("select testdate from test1 ")
            query = text("select datejoined from user ")  # datejoined is timestamp
            conn = super(PortfolioDao, self).getconnection()
            # values = {'firstname': firstname, 'lastname': lastname, 'emailid': emailid, 'professionid': professionid, 'specializationid': specializationid, 'locationid': locationid, 'gender': gender, 'dob': dob, 'about' : about}
            result = conn.execute(query).fetchall()
            testdate = None
            str_test_date = None
            for row in result:
                # testdate = row['testdate']  #In mysql date,  format is YYYY-mm-dd
                # str_test_date = testdate.strftime("%Y-%m-%d") #convert to string in the format provided
                date_joined = row['datejoined']
                str_test_date = date_joined.strftime(
                    "%Y-%m-%d-%H-%M-%S")  # convert to string in the format provided  #strftime works for both date and timestamp
            print str_test_date
            return str_test_date
        except exc.SQLAlchemyError:
            raise
        except:
            raise

    def test_insert_multiple_values(self):
        try:
            query_partial = "insert into test2(userid, professionid, verified) values __CLAUSE__"
            conn = super(PortfolioDao, self).getconnection()
            user_id = 111
            key_value_list = []
            for i in range(3):
                key_value_vo = keyvalue_vo.KeyValueVo(str(i), i + 1)
                key_value_vo.verified = 1
                key_value_list.append(key_value_vo)

            in_count = 3
            raw_query = super(PortfolioDao, self).replace_multiple_values_in_insert_query(query_partial, '__CLAUSE__',
                                                                                          ['userid', 'profession',
                                                                                           'verified'], in_count)
            query = text(raw_query)
            values = dict()
            count = 0
            for key_value in key_value_list:
                values['userid' + str(count)] = user_id
                values['profession' + str(count)] = key_value._key
                values['verified' + str(count)] = key_value._value
                count = count + 1
            conn.execute(query, values)
        except exc.SQLAlchemyError:
            raise
        except:
            raise