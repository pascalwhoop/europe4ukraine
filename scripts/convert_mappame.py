# %%
import pandas as pd

df = pd.read_json("mappame.json", orient="records")
# %%

df_dropped = df.drop(["icon", "isCustomCategory", "CustomCategoryName", "VideoUrl"], axis=1)
df_renamed = df_dropped.rename(
    columns={
        "id": "_external_id",
        "SocialNetworks": "_ext_link",
        "Lng": "_map_longitude",
        "Lat": "_map_latitude",
        "Name": "Name",
        "Published": "Share publicly",
        "Category": "Support Kind",
        "Country": "Country",
        "Services": "Notes",
        "Address": "_address_free_text",
        #'icon': 'icon',
        "Image": "_attachment_list",
        "WorkTime": "_availability",
        "Email": "Email",
        "Website": "_ext_website",
        "Phone": "Phone",
        #'isCustomCategory': 'isCustomCategory',
        #'CustomCategoryName': 'CustomCategoryName',
        #'VideoUrl': 'VideoUrl'
    }
)

category_map = {
    "Їжа": "Food",
    "Інша допомога": "Other (in comments)",
    "Житло": "Shelter / Housing",
    "Укриття": "Refuge / Shelter",
    "Психологічна допомога": "Psychological",
    "Здоров'я": "Health",
    "Переїзд/трансфер": "Transport",
    "Гроші": "Money",
    "Перетримка тварин": "Pets",
    "Гуманітарна допомога": "Humanitarian",
}
country_map = {'Грузiя': 'Georgia',
 'Польща': 'Poland',
 'Україна': 'Ukraine',
 'Білорусь': 'Belarus',
 'Німеччина': 'Germany',
 'Литва': 'Lithuania',
 'Чехія': 'Czech Republic',
 'Нідерланди': 'Netherlands',
 'Латвія': 'Latvia',
 'Словаччина ': 'Slovakia',
 'Туреччина': 'Turkey',
 'Молдова ': 'Moldova',
 'Угорщина': 'Hungary',
 'Португалія': 'Portugal',
 'Великобританія': 'United Kingdom',
 'Кіпр': 'Cyprus',
 'Швеція': 'Sweden',
 'Іспанія': 'Spain',
 'Франція': 'France',
 'Бельгія': 'Belgium',
 'Північна Ірландія': 'Northern Ireland',
 'Румунія': 'Romania',
 'Австрія': 'Austria',
 'Південна Корея': 'South Korea',
 'Швейцарія ': 'Switzerland',
 'Сербія': 'Serbia',
 'США': 'USA',
 'Ізраїль': 'Israel',
 'Люксембург ': 'Luxembourg',
 'Фінляндія': 'Finland',
 'Росія': 'Russia',
 'Хорватія': 'Croatia',
 'Греція': 'Greece',
 'Італія': 'Italy',
 'Естонія': 'Estonia',
 'Північна Македонія': 'Northern Macedonia',
 'Ірландія': 'Ireland',
 'Норвегія': 'Norway',
 'Чорногорія': 'Montenegro',
 'Киргизстан': 'Kyrgyzstan',
 'Ісландія': 'Iceland',
 'Німеччина ': 'Germany',
 'Словаччина': 'Slovakia',
 'Болгарія': 'Bulgaria',
 'Чилі': 'Chile',
 'Belgium': 'Belgium'}

df_renamed['Support Kind'] = df_renamed["Support Kind"].map(category_map)
df_renamed['Country'] = df_renamed["Country"].map(country_map)

airtable_fields = [
    "Name", 
    "Status",
    "Primary contact owner",
    "Spaces available",
    "Tags",
    "Email",
    "Phone",
    "Languages",
    "Chat applications",
    "Country",
    "City",
    "Street",
    "Address",
    "[Gen] Geocache",
    "Whatsapp Link",
    "cleaned phone number",
    "Notes",
    "Proposed to help",
    "Agreed to help",
    "Support Kind",
    "Financial support amount",
    "Created",
    "Last Modified",
    "QR Code (Whatsapp)",
    "Share publicly",
    "_address_free_text"
]
# add missing columns with empty values
for col in airtable_fields:
    if col not in df_renamed.columns:
        df_renamed[col] = ""

common_fields = [x for x in airtable_fields if x in df_renamed.columns]
new_fields = [x for x in df_renamed.columns if x not in airtable_fields]
df_sorted = df_renamed[common_fields + new_fields]

# some hard coded stuff
df_sorted['Share publicly'] = "yes"
df_sorted['Status'] = "imported"

df_sorted.to_csv("mapame.csv", index=False)
df_sorted.to_excel("mapame.xlsx", index=False)
# %%

df_sorted
# %%
# %%
df
df_copy = df_sorted
df_copy['Share publicly'] = "yes"
df_copy


# %%
