from read_GTFS import read_GTFS

read = read_GTFS(r"C:\Users\felip\PycharmProjects\read_gtfs\GTFS_scheduled.zip")

df_gtfs = read.read_gtfs_with_df()

df_stops = df_gtfs["stops.txt"]
print(df_stops)
stops_id = df_stops["stop_id"]
print(stops_id)