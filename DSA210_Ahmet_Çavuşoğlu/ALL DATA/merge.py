# 1. Date formatting
daily_passenger_weather["tarih"] = pd.to_datetime(daily_passenger_weather["tarih"])
istanbul_weather_data["tarih"] = pd.to_datetime(istanbul_weather_data["tarih"])

# 2. Merge by date
merged_df = pd.merge(
    daily_passenger_weather,
    istanbul_weather_data,
    on="tarih",
    how="left"
)

# 3. Final clean structure
final_df = merged_df[[
    "tarih",
    "istasyon_adi",
    "gunluk_yolcu",
    "nem",
    "maksimum_sicaklik",
    "minimum_sicaklik",
    "ruzgar_hizi",
]].copy()

# 4. Add derived columns
final_df["ay"] = final_df["tarih"].dt.month
final_df["gun"] = (final_df["tarih"] - pd.Timestamp("2024-01-01")).dt.days + 1

# Preview
print(final_df.head())
