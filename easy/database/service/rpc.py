from nameko.rpc import rpc
from rest_framework import serializers


class RPCServiceModelBase(type):
    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)
        if hasattr(new_class, "__dependence__"):
            __serializer__ = type("Serializer", (serializers.ModelSerializer,), {"Meta": type})
            __serializer_meta__ = type("Meta", (), {"model": new_class.__dependence__, "fields": "__all__"})
            __serializer__.Meta = __serializer_meta__
            setattr(new_class, "__serializer__", __serializer__)
        return new_class


class RPCServiceModel(metaclass=RPCServiceModelBase):
    name = "RPCServiceModel"

    def get_objects(self):
        return self.__dependence__.objects

    @rpc
    def count(self):
        return self.get_objects().count()

    @rpc
    def get(self, *args, **kwargs):
        return self.__serializer__(self.get_objects().get(*args, **kwargs)).data

    @rpc
    def create(self, **kwargs):
        return self.__serializer__(self.get_objects().create(**kwargs)).data

    @rpc
    def earliest(self, *fields, field_name=None):
        return self.__serializer__(self.get_objects().earliest(*fields, field_name=field_name)).data

    @rpc
    def latest(self, *fields, field_name=None):
        return self.__serializer__(self.get_objects().latest(*fields, field_name=field_name)).data

    @rpc
    def first(self):
        return self.__serializer__(self.get_objects().first()).data

    @rpc
    def last(self):
        return self.__serializer__(self.get_objects().last()).data

    @rpc
    def delete(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return: (deleted, _rows_count)
        """
        query_set = self.get_objects().filter(*args, **kwargs)
        if len(query_set) == 0:
            raise ValueError("Query Set is empty, ensure that the object you delete is exist.")
        return query_set.delete()

    @rpc
    def update(self, filter, **kwargs):
        if isinstance(filter, dict):
            query_set = self.get_objects().filter(**filter)
        else:
            raise ValueError("The type of parameter filter must be dict.")
        return query_set.update(**kwargs)

    @rpc
    def exists(self):
        return self.get_objects().exists()

    @rpc
    def none(self):
        return self.__serializer__(self.get_objects().none(), many=True).data

    @rpc
    def all(self):
        result = self.get_objects().all()
        return self.__serializer__(result, many=True).data

    @rpc
    def filter(self, *args, **kwargs):
        return self.__serializer__(self.get_objects().filter(*args, **kwargs), many=True).data

    @rpc
    def exclude(self, *args, **kwargs):
        return self.__serializer__(self.get_objects().exclude(*args, **kwargs), many=True).data
