import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Africa Climate Dashboard", layout="wide")

st.title("🌍 Africa Climate Dashboard (Week 0 Project)")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    ethiopia = pd.read_csv("data/ethiopia.csv")
    kenya = pd.read_csv("data/kenya.csv")
    sudan = pd.read_csv("data/sudan.csv")
    tanzania = pd.read_csv("data/tanzania.csv")
    nigeria = pd.read_csv("data/nigeria.csv")

    ethiopia["Country"] = "Ethiopia"
    kenya["Country"] = "Kenya"
    sudan["Country"] = "Sudan"
    tanzania["Country"] = "Tanzania"
    nigeria["Country"] = "Nigeria"

    df = pd.concat([ethiopia, kenya, sudan, tanzania, nigeria])
    df["DATE"] = pd.to_datetime(df["YEAR"] * 1000 + df["DOY"], format="%Y%j")
    return df

df = load_data()

# ---------------- FILTER ----------------
countries = st.multiselect(
    "Select Countries",
    list(df["Country"].unique()),
    default=list(df["Country"].unique())
)

df = df[df["Country"].isin(countries)]

# ---------------- TEMPERATURE ----------------
st.subheader("🌡️ Temperature Trend")

temp = df.groupby(["Country", pd.Grouper(key="DATE", freq="ME")])["T2M"].mean().reset_index()

plt.figure(figsize=(10,5))
for c in countries:
    data = temp[temp["Country"] == c]
    plt.plot(data["DATE"], data["T2M"], label=c)

plt.legend()
plt.xlabel("Date")
plt.ylabel("Temperature")
st.pyplot(plt)

# ---------------- PRECIPITATION ----------------
st.subheader("🌧️ Precipitation")

fig, ax = plt.subplots()
df.boxplot(column="PRECTOTCORR", by="Country", ax=ax)
plt.suptitle("")
st.pyplot(fig)

# ---------------- HUMIDITY ----------------
st.subheader("💧 Humidity")

humidity = df.groupby("Country")["RH2M"].mean()

fig, ax = plt.subplots()
humidity.plot(kind="bar", ax=ax)
st.pyplot(fig)

# ---------------- WIND ----------------
st.subheader("🌬️ Wind Speed")

wind = df.groupby("Country")["WS2M"].mean()

fig, ax = plt.subplots()
wind.plot(kind="bar", ax=ax)
st.pyplot(fig)

# ---------------- DATA ----------------
st.subheader("📊 Data Preview")
st.dataframe(df.head())