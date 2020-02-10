from django.forms import model_to_dict
from itertools import chain


def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(instance)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(instance)]
    return data


def limit_number(limit_n):
    limit = limit_n if limit_n else 0

    return limit


def serialize_foreign_key(obj, model, model_key, **queries):
    instance = model.objects.get(**queries)

    obj[model_key] = {}

    obj.pop(model_key + '__uuid')

    for key, value in to_dict(instance).items():
        obj[model_key][key] = value

    return obj