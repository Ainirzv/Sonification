pip install pandas                    
import pandas as pd
con=np.concatenate((gray))
print(con)
#output [25 24 24 ... 29 28 27]
df1=pd.DataFrame({'serial no':range(1,len(con)+1),'data':con})
df1
'''#output 	
serial no	data
0	1	25
1	2	24
2	3	24
3	4	26
4	5	29
...	...	...
4190204	4190205	30
4190205	4190206	30
4190206	4190207	29
4190207	4190208	28
4190208	4190209	27
4190209 rows × 2 columns
df1=pd.DataFrame({'serial no':range(1,len(con)+1),'data':con})
df1
#output
serial no	data
0	1	25
1	2	24
2	3	24
3	4	26
4	5	29
...	...	...
4190204	4190205	30
4190205	4190206	30
4190206	4190207	29
4190207	4190208	28
4190208	4190209	27'''
freq=[349.23, 246.94 ,261.63, 293.66, 329.63, 220.01, 415.30]
arfreq = np.array(freq)
print(arfreq)
df2 = pd.DataFrame({"freq":arfreq})
df2

'''freq
0	349.23
1	246.94
2	261.63
3	293.66
4	329.63
5	220.01
6	415.30'''
mapping_dict = dict(zip(df1['data'].unique(), df2['freq']))
df1['frequencies'] = df1['data'].map(mapping_dict)
print(df1)
#output 
print(df1)
print(df1)
'''         serial no  data  frequencies
0                1    25       349.23
1                2    24       246.94
2                3    24       246.94
3                4    26       261.63
4                5    29       293.66
...            ...   ...          ...
4190204    4190205    30       329.63
4190205    4190206    30       329.63
4190206    4190207    29       293.66
4190207    4190208    28       220.01
4190208    4190209    27       415.30

[4190209 rows x 3 columns]'''
arfrequencies= df1['frequencies'].to_numpy()
arfrequencies
#output array([349.23, 246.94, 246.94, ..., 293.66, 220.01, 415.3 ])
import IPython.display as ipd
song = np.array([]) 
sr = 22080
T = 2
t = np.linspace(0, T, int(T*sr), endpoint=False)
nPixels = 120
for i in range(nPixels):  
    val = arfrequencies[i]
    note  = 0.5*np.sin(2*np.pi*val*t)
    song  = np.concatenate([song, note])
ipd.Audio(song, rate=sr)

