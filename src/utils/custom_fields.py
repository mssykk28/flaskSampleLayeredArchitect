from flask_restx.fields import Boolean as OriginalBoolean
from flask_restx.fields import DateTime as OriginalDateTime
from flask_restx.fields import Integer as OriginalInteger
from flask_restx.fields import String as OriginalString


class Integer(OriginalInteger):
    def __init__(self, *args, **kwargs):
        self.nullable = kwargs.pop("nullable", None)
        super(Integer, self).__init__(*args, **kwargs)

    def schema(self):
        schema = super(Integer, self).schema()
        schema.update({"nullable": self.nullable})
        return schema


class String(OriginalString):
    def __init__(self, *args, **kwargs):
        self.nullable = kwargs.pop("nullable", None)
        super(String, self).__init__(*args, **kwargs)

    def schema(self):
        schema = super(String, self).schema()
        schema.update({"nullable": self.nullable})
        return schema


class Boolean(OriginalBoolean):
    def __init__(self, *args, **kwargs):
        self.nullable = kwargs.pop("nullable", None)
        super(Boolean, self).__init__(*args, **kwargs)

    def schema(self):
        schema = super(Boolean, self).schema()
        schema.update({"nullable": self.nullable})
        return schema


class DateTime(OriginalDateTime):
    def __init__(self, *args, **kwargs):
        self.nullable = kwargs.pop("nullable", None)
        super(DateTime, self).__init__(*args, **kwargs)

    def schema(self):
        schema = super(DateTime, self).schema()
        schema.update({"nullable": self.nullable})
        return schema
