from collections import defaultdict


class dic_stops:

    def __init__(self, df_stops):
        self.dic_stops = defaultdict(list)

        for row in range(len(df_stops["stop_id"])):
            stop_id = ""
            other = []
            for col in df_stops.columns:
                if col == "stop_id":
                    stop_id = df_stops.iloc[row][col]
                else:
                    other.append((col, df_stops.iloc[row][col]))

            self.dic_stops[stop_id].append(other)
