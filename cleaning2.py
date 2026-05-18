import pandas as pd

# قراءة البيانات
df = pd.read_csv('data_handelling_3/data/researchers.csv')

# عرض أول الصفوف
print(df.head())

# --------------------------------
# فحص القيم المفقودة
# --------------------------------
print(df.isnull().sum())

# حذف الصفوف الفارغة
df = df.dropna()

# --------------------------------
# حذف التكرار
# --------------------------------
df = df.drop_duplicates()

# --------------------------------
# إعادة ترتيب الـ index
# --------------------------------
df = df.reset_index(drop=True)

# --------------------------------
# حفظ البيانات النظيفة
# --------------------------------
df.to_csv('data_handelling_3/data/researchers_clean.csv', index=False)

print("Cleaning Finished")
print(df.shape)
print(df['country'].value_counts())