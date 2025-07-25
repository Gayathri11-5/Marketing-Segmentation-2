import pandas as pd
def marketing(profile_data):
    suggestions=[]
    for idx, row in profile_data.iterrows():
        income=row.get("Income", 0)
        wines=row.get("MntWines",0)
        recency=row.get("Recency",0)
        teenhome=row.get("Teenhome",0)
        web=row.get("NumWebPurchases",0)
        if income > 0.8 and wines >500
            sug = f"cluster{idx} 💎 Offer premium memberships and loyalty rewards"
        elif recency < 10:
            sug =  f"cluster{idx}⏰ Send time-sensitive limited-time deals"
        elif teenhome > 0:
            sug =  f"cluster{idx}🎮 Promote tech gadgets and teen-focused offers"
        elif web >7:
            sug=f"cluster{idx}focus their activity in purchasing and offer deals and discounts"
        else:
            sug="try discounts and offers for this season"
        suggestions.append(sug)
    return pd.DataFrame({"Cluster":profile_data.index,"Suggested marketing strategy":suggestions})
