__author__ = 'Manish'

import dbconnection
from sqlalchemy import exc

class DbConDao(dbconnection.DBConnection):

    def __init__(self, conn):
        self.conn = conn

    def getconnection(self):
        try:
            if self.conn is None or self.conn.closed:
                raise exc.SQLAlchemyError("Connection is already closed.")

        except exc.SQLAlchemyError:
            raise

        except:
            raise

        return self.conn

    @staticmethod
    def replace_in_clause(text, in_clause, value_name, count): #FIXME : Query should not have just "__IN_CLAUSE__" instead of "in (__IN_CLAUSE__)". If count = 1,change __IN_CLAUSE__ with " = :value_name"
        str_replaced = ""
        for i in range(count):
            if i == 0:
                str_replaced = str_replaced + ":" + value_name + str(i+1)
            else:
                str_replaced = str_replaced + ",:" + value_name + str(i+1)
        text_new = text.replace(in_clause, str_replaced)
        return text_new

    @staticmethod
    def replace_multiple_values_in_insert_query(text, values_clause, value_items_string_list, count):
        #If value_items_string_list is ['item', 'fb', 'cb'] and count  = 3, values_clause will be replaced by (:item0, :fb0, :cb0), (:item1, :fb1, :cb1), (:item2, :fb2, :cb2)
        str_replaced = ''
        for i in range(count):
            if i == 0:
                str_replaced = str_replaced + '('
            else:
                str_replaced = str_replaced + ', ('

            item_number = 0
            for item in value_items_string_list:
                if item_number == 0:
                   str_replaced =  str_replaced + ':' + item + str(i)
                else:
                    str_replaced = str_replaced + ', ' + ':' + item + str(i)
                item_number = item_number + 1

            str_replaced = str_replaced + ')'
        text_new = text.replace(values_clause, str_replaced)
        return text_new




