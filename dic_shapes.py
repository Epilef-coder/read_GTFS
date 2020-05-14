from collections import defaultdict


class dic_shapes:

    def __init__(self, df_shapes):
        self.dic_shapes = defaultdict(list)

        for row in range(len(df_shapes["shape_id"])):
            shape_id = ""
            other = []
            for col in df_shapes.columns:
                if col == "shape_id":
                    shape_id = df_shapes.iloc[row][col]
                else:
                    other.append((col, df_shapes.iloc[row][col]))

            self.dic_shapes[shape_id].append(other)
