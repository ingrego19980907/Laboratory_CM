import pandas as pd

xlsx = pd.ExcelFile(r'C:\Python\Project\Study\Laboratory\Tasks\Task_1\Task_1.xlsx')


def stint(x):
    return ord(x) / 1000.0  # функція ord(x) надає ascii-код символа x


def stint1(x):
    return 1.0 if x == 'e' else 0.0


df = pd.read_excel(xlsx, usecols='A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,V,U,W', header=None,
                   names=['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL',
                          'MM', 'NN', 'OO', 'PP', 'QQ', 'RR', 'SS', 'TT', 'VV', 'UU', 'WW'], nrows=50,
                   converters={'AA': stint1, 'BB': stint, 'CC': stint, 'DD': stint, 'EE': stint,
                               'FF': stint, 'GG': stint, 'HH': stint, 'II': stint, 'JJ': stint,
                               'KK': stint, 'LL': stint, 'MM': stint, 'NN': stint, 'OO': stint,
                               'PP': stint, 'QQ': stint, 'RR': stint, 'SS': stint, 'TT': stint,
                               'VV': stint, 'UU': stint, 'WW': stint})
print(df)

sorted_df = df.sort_values(by='AA')

sorted_df.to_excel('C:/Python/Project/Study/Laboratory/Tasks/Task_1/result_1.xlsx', header=False, index=False)
