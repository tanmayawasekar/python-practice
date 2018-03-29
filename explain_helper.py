from django.db import connections
from django.db.models.query import QuerySet


class QuerySetExplainMixin:
    def explain(self):
        cursor = connections[self.db].cursor()
        cursor.execute('explain %s' % str(self.query))
        return cursor.fetchall()


QuerySet.__bases__ += (QuerySetExplainMixin,)
