def calculate_coefficients(self):
    mat_df = self.df.remove_columns([self.dependent_variable]).add_columns({
        'constant', [1 for _ in len(self.df)]})

    X_T = Matrix(mat_df.to_array())
    X = X_T.transpose()

    Y = Matrix(self.df.get_column(self.dependent_variable)).transpose()

    result = (X_T.matrix_multiply(X)).inverse(
    ).matrix_multiply(X_T.matrix_multiply(Y))

    return {key: val for key, val in zip(mat_df.columns, result[:, 0])}
