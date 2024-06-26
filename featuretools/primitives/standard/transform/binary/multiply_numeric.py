import numpy as np
from woodwork.column_schema import ColumnSchema

from featuretools.primitives.base.transform_primitive_base import TransformPrimitive


class MultiplyNumeric(TransformPrimitive):
    """Performs element-wise multiplication of two lists.

    Description:
        Given a list of values X and a list of values
        Y, determine the product of each value in X
        with its corresponding value in Y.

    Examples:
        >>> multiply_numeric = MultiplyNumeric()
        >>> multiply_numeric([2, 1, 2], [1, 2, 2]).tolist()
        [2, 2, 4]
    """

    name = "multiply_numeric"
    input_types = [
        ColumnSchema(semantic_tags={"numeric"}),
        ColumnSchema(semantic_tags={"numeric"}),
    ]
    return_type = ColumnSchema(semantic_tags={"numeric"})
    commutative = True

    description_template = "the product of {} and {}"

    def get_function(self):
        return np.multiply

    def generate_name(self, base_feature_names):
        return "%s * %s" % (base_feature_names[0], base_feature_names[1])
