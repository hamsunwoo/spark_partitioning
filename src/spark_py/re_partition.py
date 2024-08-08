import pandas as pd

def re_partition(load_dt='20150101', base_path='/Users/seon-u/data/movie/data/extract'):
    df = pd.read_parquet(f'{base_path}/load_dt={load_dt}')
    df.to_parquet('~/data/movie/repartition', partition_cols=['load_dt','multiMovieYn', 'repNationCd'])
