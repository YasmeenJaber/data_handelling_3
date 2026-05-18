
# --------------------------------
# CP3
# --------------------------------
import pandas as pd
funding = pd.read_excel(
    './data/funding.xlsx'
)

# تنظيف وتحويل
funding['amount_cad'] = pd.to_numeric(
    funding['amount_cad'],
    errors='coerce'
)

# حذف القيم الفارغة
funding = funding.dropna(subset=['amount_cad'])

# إبقاء الموجب فقط
funding = funding[
    funding['amount_cad'] > 0
]

# المجموع
total = funding['amount_cad'].sum()

print(total)
#2024000.0