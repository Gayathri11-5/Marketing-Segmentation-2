import pandas as pd
def marketing(profile_data):
    sugesstions=[]
    for idx, row in profile_data.iterrows():
        if row["Income"]>0.6 and row.get("Kidhome",0)>0:
            sug="Offer family-focused deals and discounts"
        elif row.get("Recency", 0) < 10:
            sug = "⏰ Send time-sensitive limited-time deals"
        elif row.get("Teenhome", 0) > 0:
            sug = "🎮 Promote tech gadgets and teen-focused offers"
        else:
            sug="try discounts and offers for this season"
        sugesstions.append(sug)
    return pd.DataFrame({"Cluster":profile_data.index,"Suggested marketing strategy":sugesstions})