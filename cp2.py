
import pandas as pd

# تحميل البيانات
df = pd.read_csv('./data/researchers.csv')
papers = pd.read_json(
    'data_handelling_3/data/publications.json'
)

# أعلى citations
top_paper = papers.loc[
    papers['citations'].idxmax()
]

print(top_paper['title'])

#Data Opens Doors: A Manifesto for Open Research