# transformations/transformation.py

import pandas as pd

class Transformation:
    def __init__(self, action, params):
        self.action = action
        self.params = params

    def apply(self, dataframe):
        if self.action == 'filter':
            return self._filter(dataframe)
        elif self.action == 'select_columns':
            return self._select_columns(dataframe)
        elif self.action == 'sort':
            return self._sort(dataframe)
        else:
            raise ValueError(f"Unsupported action: {self.action}")

    def _filter(self, dataframe):
        column = self.params['column']
        operator = self.params['operator']
        value = self.params['value']

        if operator == '>':
            return dataframe[dataframe[column] > value]
        elif operator == '<':
            return dataframe[dataframe[column] < value]
        elif operator == '==':
            return dataframe[dataframe[column] == value]
        else:
            raise ValueError(f"Unsupported operator: {operator}")

    def _select_columns(self, dataframe):
        columns = self.params['columns']
        return dataframe[columns]

    def _sort(self, dataframe):
        column = self.params['column']
        ascending = self.params.get('ascending', True)
        return dataframe.sort_values(by=column, ascending=ascending)
