import pandas as pd

# =========================
# 1) قراءة الملفات
# =========================

researchers = pd.read_csv("data/researchers.csv")

publications = pd.read_json("data/publications.json")

funding = pd.read_excel("data/funding.xlsx")


# =========================
# 2) تنظيف بيانات التمويل
# =========================

def clean_funding(df):

    # حذف القيم الفارغة
    df = df.dropna()

    # حذف القيم السالبة من amount_cad
    df = df[df["amount_cad"] >= 0]

    # حذف التكرار
    df = df.drop_duplicates()

    return df


funding_clean = clean_funding(funding)


# =========================
# 3) دمج البيانات
# =========================

# دمج الباحثين مع الأبحاث
merged1 = pd.merge(
    researchers,
    publications,
    on="researcher_id",
    how="inner"
)

# دمج الناتج مع التمويل
merged_data = pd.merge(
    merged1,
    funding_clean,
    on="researcher_id",
    how="inner"
)


# =========================
# عدد الصفوف بعد الدمج
# =========================

print("Rows after merge:", len(merged_data))


# =========================
# ما الذي خسرناه في inner join؟
# =========================

lost_researchers = len(researchers) - len(
    merged_data["researcher_id"].unique()
)

print("Researchers lost بسبب inner join:", lost_researchers)


# =========================
# 4) السؤال الأول
# أعلى citations
# =========================

top_citations = merged_data.groupby("first_name")["citations"].sum()

top_researcher = top_citations.idxmax()
top_citation_value = top_citations.max()

print("\nResearcher with highest citations:")
print(top_researcher, "-", top_citation_value)


# =========================
# 5) السؤال الثاني
# أكثر مجال حصل funding
# =========================

top_field = merged_data.groupby("field")["amount_cad"].sum()

top_field_name = top_field.idxmax()
top_field_value = top_field.max()

print("\nField with highest funding:")
print(top_field_name, "-", top_field_value)


# =========================
# 6) السؤال الثالث
# أقدم باحث وما زال active
# =========================

active_researchers = merged_data[merged_data["is_active"] == True]

oldest_active = active_researchers.sort_values("joined_year").iloc[0]

print("\nOldest active researcher:")
print(oldest_active["first_name"], "-", oldest_active["joined_year"])


# =========================
# 7) حفظ الملف النهائي
# =========================

merged_data.to_csv(
    "output_clean_research_data.csv",
    index=False
)

print("\nClean merged file saved successfully!")