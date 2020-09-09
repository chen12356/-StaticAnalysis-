# import datetime
#
# from django.db import models
# from django.db.models import query
#
# from MobSF.settings import MODEL_K
# from scripts.cache import rds
# import logging
#
#
# logger = logging.getLogger(__name__)
#
# def get(self, *args, **kwargs):
#     '''带缓存处理的 get 方法'''
#     model_cls_name = self.model.__name__  # 获取当前 objects 绑定的类的名字
#     md5 = kwargs.get('MD5')
#     logger.info("MD5: %s"%md5)
#     if md5 is not None:
#         model_key = MODEL_K % (model_cls_name, md5)
#         # 从缓存获取数据
#         model_obj = rds.get(model_key)
#         if isinstance(model_obj, self.model):
#             return model_obj
#
#     # 缓存中没有数据时，直接使用原 get 方法从数据库获取数据
#     model_obj = self._get(*args, **kwargs)
#
#     # 将 model_obj 对象写入缓存
#     model_key = MODEL_K % (model_cls_name, model_obj.pk)
#     rds.set(model_key, model_obj)
#
#     return model_obj
# def filter(self, *args, **kwargs):
#     '''带缓存处理的 get 方法'''
#     model_cls_name = self.model.__name__  # 获取当前 objects 绑定的类的名字
#     MD5 = kwargs.get('MD5')
#     if MD5 is not None:
#         model_key = MODEL_K % (model_cls_name, MD5)
#         # 从缓存获取数据
#         model_obj = rds.get(model_key)
#         if isinstance(model_obj,query.QuerySet):
#             print("从Redis中取出:%s" %model_obj)
#             return model_obj
#
#     # 缓存中没有数据时，直接使用原 filter 方法从数据库获取数据
#     model_obj = self._filter(*args, **kwargs)  #转成list对象,则避免QuerySet惰性查询
#     print('对象写入Redis缓存中:%s'%model_obj)
#     # 将 model_obj 对象写入缓存
#     model_key = MODEL_K % (model_cls_name, MD5)
#     rds.set(model_key, model_obj)
#     return model_obj
#
# def save(self, force_insert=False, force_update=False, using=None,
#          update_fields=None):
#     '''带缓存处理的 save 方法'''
#     # 调用原 save 将数据保存到数据库
#     self._save(force_insert, force_update, using, update_fields)
#
#     # 将 model 对象写入缓存
#     print("# 将 model 对象写入缓存")
#     model_key = MODEL_K % (self.__class__.__name__, self.MD5)
#     rds.set(model_key, self)
#
#
#
# def patch_model():
#     '''通过 Monkey Patch 的方式为 Model 增加缓存处理'''
#     # query.QuerySet._get = query.QuerySet.get  # 将原 get 方法重命名
#     # query.QuerySet.get = get  # 将带缓存处理的 get 方法覆盖原 get 方法
#
#     query.QuerySet._filter = query.QuerySet.filter  # 将原 get 方法重命名
#     query.QuerySet.filter = filter  # 将带缓存处理的 get 方法覆盖原 get 方法
#
#     models.Model._save = models.Model.save  # 对原 save 方法重命名
#     models.Model.save = save  # 用带缓存处理的 save 方法覆盖原 save 方法
#
#     # models.Model.to_dict = to_dict
