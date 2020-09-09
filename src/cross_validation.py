
"""
- binary classificatio
- multiclass classification
- multip label classification
- single column regression
- multi column regression
- holdout
"""



class CrossValidation:
    def __init__(self, df, target_cols, problem_type = "binary_classificatio", num_folds =5, shuffle= Tue, random_state=42):
        self.dataframe = df
        self.target_cols = target_cols
        self.num_targets = len(target_cols)
        self.problem_type = problem_type
        self.num_folds = num_folds
        self.shuffle = shuffle
        self.random_state = random_state

        if self.shuffle is True:
            self.dataframe = selfdataframe.sample(frac=1).reset_index(drop = True)

        self.dataframe["kfold"]=-1

    def split(self):
        if self.problem_type == "binary_classification"
            if unique_values == 1:
                raise Exception("Only one unique value found")
            elif unique_values > 1:
                target = self.target_cols[0]
                kf = model_selection.StratifiedKFold(n_splits=5, shuffle=False, random_state=42)

                for fold, (train_idx, val)