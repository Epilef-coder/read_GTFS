from collections import defaultdict


class dic_routes:

    def __init__(self, df_routes):
        self.dic_routes = defaultdict(list)

        for row in range(len(df_routes["route_id"])):
            route_id = ""
            other = []
            for col in df_routes.columns:
                if col == "route_id":
                    route_id = df_routes.iloc[row][col]
                else:
                    other.append((col, df_routes.iloc[row][col]))

            self.dic_routes[route_id].append(other)
