import pickle

with open('backup.pkl','rb') as f:
    dane = pickle.load(f)

print(dane)
