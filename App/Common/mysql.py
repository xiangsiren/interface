#! /usr/bin/env python
# -*- coding: utf8 -*-
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, or_, and_, any_, text, exists
from App.Model.Models import *
from App.Common import conf


class cli:
    def __init__(self):
        conn = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8'.format(conf.RDS_MYSQL['USER'],
                                                                    conf.RDS_MYSQL['PASSWORD'],
                                                                    conf.RDS_MYSQL['HOST'],
                                                                    conf.RDS_MYSQL['PORT'],
                                                                    conf.RDS_MYSQL['DB_NAME_BMC'])
        engine = create_engine(conn, pool_recycle=10, pool_pre_ping=True)
        DBSession = scoped_session(sessionmaker(bind=engine))
        self.session = DBSession()

    def add_column(self, args):
        try:
            for data_model in args:
                self.session.add(data_model)
            self.commit()
            return 0
        except Exception as e:
            print(e)
            self.rollback()
            return -1
        finally:
            self.close()

    def add_column3(self, data_model):
        try:
            self.session.add(data_model)
            self.commit()
            process_id = data_model.process_id
            return process_id
        except Exception as e:
            print(e)
            self.rollback()
            return -1
        finally:
            self.close()

    def add_column2(self, args):
        try:
            self.session.add(args)
            self.commit()
            return 0
        except Exception as e:
            print(e)
            self.rollback()
            return -1

    def add_column_return(self, data_model, column=''):
        try:

            self.session.add(data_model)
            # self.session.flush()
            self.commit()
            if column:
                return eval('data_model.' + column)
            return 0
        except Exception as e:
            print(e)
            self.rollback()
            return -1
        finally:
            self.close()


    # finally:
    # 	self.close()

    def get_column(self, data_model, **kargs):
        try:
            if len(kargs) == 0:
                return self.session.query(data_model).all()
            else:
                return self.session.query(data_model).filter_by(**kargs).all()
        except Exception as e:
            print(e)
        finally:
            self.close()

    def get_column_test(self, data_model, filter_str='', sort_str='', limit=0, offset=0):
        query_str = 'self.session.query({})'.format(data_model)
        if filter_str:
            query_str += '.filter({})'.format(filter_str)
        # return eval('self.session.query({}).filter({}).all()'.format(data_model,filter_str))
        if sort_str:
            query_str += '.order_by({})'.format(sort_str)
        if limit:
            query_str += '.limit({})'.format(limit)
        if offset:
            query_str += '.offset({})'.format(offset)
        query_str += '.all()'
        try:
            return eval(query_str)
        except Exception as e:
            print(query_str)
            print(e)
        finally:
            self.close()

    def add_bulk(self, table, data_list):
        try:
            query_str = 'self.session.bulk_insert_mappings({},{})'.format(table, data_list)
            eval(query_str)
            self.commit()
            return 0
        except Exception as e:
            print(e)
            return -1
        finally:
            self.close()

    def update_bulk(self, table, data_list):
        try:
            query_str = 'self.session.bulk_update_mappings({},{})'.format(table, data_list)
            eval(query_str)
            self.commit()
            return 0
        except Exception as e:
            print(e)
            return -1
        finally:
            self.close()

    def count_test(self, data_model, filter_str=''):
        query_str = 'self.session.query(func.count({}))'.format(data_model)
        if filter_str:
            query_str += '.filter({})'.format(filter_str)
        query_str += '.scalar()'
        try:
            return eval(query_str)
        except Exception as e:
            print(e)
        finally:
            self.close()

    def join_count_test(self, count_str='', join_str='', filter_str=''):
        query_str = 'self.session.query(func.count({})).join({})'.format(count_str, join_str)
        if filter_str:
            query_str += '.filter({})'.format(filter_str)
        query_str += '.scalar()'
        try:
            return eval(query_str)
        except Exception as e:
            print(e)
        finally:
            self.close()


    def get_relate_column(self, page, pagesize, sort, *args, **kargs):
        sql = 'self.session.query('
        for i in range(len(args)):
            sql += 'args[' + str(i) + '],'
        if kargs.has_key('key1'):
            sql = sql[0:len(sql) - 1] + ').filter('
            for j in range(len(kargs['key1'])):
                sql += "kargs['key1'][" + str(j) + "]==kargs['key2'][" + str(j) + "],"
        sql = sql[0:len(sql) - 1]
        sql += ').order_by({})'.format(sort)
        if int(pagesize) == 0:
            sql += '.all()'
        else:
            sql += '.limit({}).offset({}).all()'.format(pagesize, pagesize * page)
        try:
            return eval(sql)
        except Exception as e:
            print(e)
        finally:
            self.close()

    def del_column(self, *args, **kwargs):
        try:
            for data_model in args:
                if len(kwargs) > 0:
                    self.session.query(data_model).filter_by(**kwargs).delete()
                else:
                    self.session.delete(data_model)
            self.commit()
            return 0
        except Exception as e:
            print(e)
            self.rollback()
            return -1
        finally:
            self.close()

    def get_column_join(self, page, pagesize, sort, model1, model2, foreign_key, _filter, group_by=''):
        sql = 'self.session.query({},{}).join({}, {}).filter({}).order_by({})'.format(model1, model2, model2,
                                                                                      foreign_key, _filter, sort)
        if pagesize != 0:
            sql = sql + '.limit({}).offset({})'.format(pagesize, pagesize * page)
        if group_by:
            sql += group_by
        sql += '.all()'
        try:
            return eval(sql)
        except Exception as e:
            print(sql)
            print('error', e)
        finally:
            self.close()

    def get_column_join_three(self, page, pagesize, sort, model1, model2, model3, foreign_key, foreign_key2, _filter):
        sql = 'self.session.query({},{},{}).join({}, {}).outerjoin({}, {}).filter({}).order_by({})'.format(model1,
                                                                                                           model2,
                                                                                                           model3,
                                                                                                           model2,
                                                                                                           foreign_key,
                                                                                                           model3,
                                                                                                           foreign_key2,
                                                                                                           _filter,
                                                                                                           sort)
        if pagesize != 0:
            sql = sql + '.limit({}).offset({})'.format(pagesize, pagesize * page)
        sql += '.all()'
        try:
            return eval(sql)
        except Exception as e:
            print(e)
        finally:
            self.close()

    def get_columns_join_models(self, page, pagesize, sort, model_list, foreign_key_list, _filter):
        sql = 'self.session.query('
        sql += ','.join(model_list) + ')'
        for i in range(len(foreign_key_list)):
            sql += '.join({},{})'.format(model_list[i + 1], foreign_key_list[i])
        sql += '.filter({}).order_by({})'.format(_filter, sort)
        if pagesize != 0:
            sql = sql + '.limit({}).offset({})'.format(pagesize, pagesize * page)
        sql += '.all()'
        try:
            return eval(sql)
        except Exception as e:
            print(e)
        finally:
            self.close()

    def del_columns(self, data_model, del_key_list, query_list):
        try:
            filter_str = ''
            for i in range(len(del_key_list)):
                filter_str += 'del_key_list[{}].in_(query_list[{}])'.format(i, i) + ','
            eval('self.session.query(data_model).filter(and_({})).delete(synchronize_session=False)'.format(filter_str))
            self.commit()
            return 0
        except Exception as e:
            print(e)
            self.rollback()
            return -1
        finally:
            self.close()

    def del_column_in(self, model, key, query_list):
        try:
            filter_str = '{}.{}.in_({})'.format(model, key, query_list)
            eval('self.session.query({}).filter({}).delete(synchronize_session=False)'.format(model, filter_str))
            self.commit()
            return 0
        except Exception as e:
            print(e)
            self.rollback()
            return -1
        finally:
            self.close()

    def update_column_test(self, db, update_dit, **kwargs):
        try:
            self.session.query(db).filter_by(**kwargs).update(update_dit)
            self.commit()
            return 0
        except Exception as e:
            self.rollback()
            print(e)
            return -1
        finally:
            self.close()

    def update_column_test2(self, data_model, filter_str='', update_dict={},synchronize_session=True):
        query_str = 'self.session.query({})'.format(data_model)
        if filter_str:
            query_str += '.filter({})'.format(filter_str)
        if update_dict:
            if synchronize_session:
                query_str += '.update({})'.format(update_dict)
            else:
                query_str += '.update({},synchronize_session=False)'.format(update_dict)
        try:
            eval(query_str)
            self.commit()
            return 0
        except Exception as e:
            print(query_str)
            print(e)
            return -1
        finally:
            self.close()

    # self.session.query(Order).filter(Order.init_order_id.in_([20181112171358796])).update({'order_status':-3})
    # self.commit()

    def update_column(self, model_list, query_key_dict, query_val_dict, update_list):
        try:
            for i in range(len(model_list)):
                sql = 'self.session.query(model_list[' + str(i) + ']).filter_by('
                filter_str = ''
                query_key_list = query_key_dict[str(i)]
                query_val_list = query_val_dict[str(i)]
                for j in range(len(query_key_list)):
                    filter_str += '{}="{}",'.format(query_key_list[j], query_val_list[j])
                filter_str = filter_str[0:len(filter_str) - 1]
                sql += '{}).update(update_list[{}])'.format(filter_str, i)
                eval(sql)
            self.commit()
            return 0
        except Exception as e:
            self.rollback()
            print(e)
            return -1
        finally:
            self.close()

    def count(self, primary_key, **kwargs):
        try:
            return self.session.query(func.count(primary_key)).filter_by(**kwargs).scalar()
        except Exception as e:
            print(e)
        finally:
            self.close()

    def sql_interface(self, sql):
        try:
            return eval(sql)
        except Exception as e:
            print(sql)
            print(e), 222
        finally:
            self.close()

    def sql_execute(self, sql_str):
        try:
            return self.session.execute(sql_str)
        except Exception as e:
            print(e)
        finally:
            self.close()

    def rollback(self):
        self.session.rollback()

    def close(self):
        self.session.close()

    def commit(self):
        self.session.commit()

    def get_session(self):
        return self.session
