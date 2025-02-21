class SkipFilter(Exception):
    """
    Exception to be used when any particular filter
    within the :class:`django_ufilter.filtersets.base.FilterSet` should be skipped.

    Possible reasons for skipping the field:

    * filter lookup config is invalid
      (e.g. using wrong field name -
      field is not present in filter set)
    * filter lookup value is invalid
      (e.g. submitted "a" for integer field)
    """


class Empty(Exception):
    """
    Exception to be used when filter backend should return
    empty queryset when any of filter validations has failed.
    """
