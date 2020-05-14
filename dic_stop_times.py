from collections import defaultdict


class dic_stop_times:

    def __init__(self, df_stop_times):
        self.dic_stop_times = defaultdict(list)

        for row in range(len(df_stop_times["trip_id"])):
            trip_id = ""
            other = []
            for col in df_stop_times.columns:
                if col == "trip_id":
                    trip_id = df_stop_times.iloc[row][col]
                else:
                    other.append((col, df_stop_times.iloc[row][col]))

            self.dic_stop_times[trip_id].append(other)
