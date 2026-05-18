import pandas as pd

# تحميل البيانات
df = pd.read_csv('./data/researchers.csv')

# تنظيف التكرار
df = df.drop_duplicates()

# الفلترة
filtered = df[
    (df['is_active'] == True) &
    (df['h_index'] > 15)
]

# الترتيب
filtered = filtered.sort_values(by='joined_year')

# أول حرف من last_name
letters = filtered['last_name'].str[0]

# دمج الأحرف
word = ''.join(letters)

print(word)
#DATAOPENSDOORS 