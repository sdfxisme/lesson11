from Class_Steel import Steel
import pickle

sheet1 = Steel(600,100,3)
f = open('sheet.pkl', 'wb')
pickle.dump(sheet1,f)
f.close()

f= open('sheet.pkl', 'rb')
sheet_loaded = pickle.load(f)
print(sheet_loaded)
f.close()