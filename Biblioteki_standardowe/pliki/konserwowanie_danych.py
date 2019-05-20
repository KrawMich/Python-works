import pickle

a = {'ala':5,'ola':7,'zenek':9}

with open('backup.pkl','wb') as f:
    pickle.dump( a,f)

    