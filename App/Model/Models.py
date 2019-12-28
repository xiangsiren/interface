#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, BigInteger, Integer, String, SmallInteger, Float, DateTime, Index, MetaData, \
    Table, PickleType, Boolean, DECIMAL, Text, cast
from sqlalchemy.dialects.mysql import MEDIUMTEXT, LONGTEXT, DOUBLE
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    nickname = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)


class Case(Base):
    __tablename__ = 'case'
    id = Column(BigInteger, nullable=False, primary_key=True)
    case_name = Column(String(255), comment='接口作用名称')
    path = Column(String(255), comment='接口路由')
    method = Column(String, nullable=False, comment='请求类型')
    request_data = Column(Text, comment='请求数据')
    response_data = Column(Text, comment='响应数据')
    time = Column(DateTime, comment='录制时间')


# 注册表
class Registration(Base):
    __tablename__ = 'registration'
    register_id = Column(BigInteger, primary_key=True)  # 主键 自增
    user_id = Column(BigInteger, index=True, nullable=False)  # user_id
    account = Column(String(20), nullable=False, comment='账户名，同手机号')
    belong_to = Column(BigInteger, default=0, comment='所属组织id')  # 所属组织id
    phone = Column(String(32), nullable=False, comment='客户电话')  # 客户电话
    name = Column(String(32), nullable=False, comment='客户姓名')  # 客户姓名
    province = Column(String(32), nullable=False, comment='省份')  # 省
    city = Column(String(32), nullable=False, comment='市区')  # 市
    region = Column(String(32), nullable=False, comment='区域')  # 区
    address = Column(String(128), default='', comment='详细地址')  # 详细地址
    company_name = Column(String(64), nullable=False, comment='企业名称')  # 企业名称
    receive_code = Column(String(10), default='', comment='接收的邀请码')  # 接收的邀请码
    status = Column(SmallInteger, default=1, comment='审核状态，1审核中、0审核通过、-1审核驳回')  # 审核状态: 1 审核中， 0审核通过， -1 审核驳回
    role = Column(String(20), nullable=True, comment='客户角色，bmc、coc等')  # 角色 bmc，coc， 小b，供应商
    reason = Column(String(256), default='', comment='拒绝原因')  # 被拒原因
    platform_name = Column(String(64), default='', comment='所属coc')  # 所属coc
    sign_region = Column(String(1024), default='', comment='签约地区，只限coc')
    mtime = Column(Integer, nullable=False)
    ctime = Column(Integer, nullable=False)
    review_time = Column(Integer, default=0, comment='审核通过时间')