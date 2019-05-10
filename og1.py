import pandas as pd

mf =pd.read_csv("schedule.csv")

classes = mf.columns
#print(classes)
Highestscore_teachers = mf.loc[(mf["evaluation"].astype(str).str.contains("5"))]
secondbestscore_teachers = mf.loc[(mf["evaluation"].astype(str).str.contains("4"))]

# print(Highestscore_teachers)
# print(secondbestscore_teachers)


Highestscore_teachers["Assigned Classes"] = 1
Highestscore_teachers["Total_number_classes_given"] = Highestscore_teachers.iloc[:,2:28].sum(axis=1)
print(Highestscore_teachers)

Highestscore_teachers.loc[Highestscore_teachers["Total_number_classes_given"] > 2,["Assigned Classes"]] = "Number of Classes Assigned"
print(Highestscore_teachers)
Highestscore_teachers.to_csv("highestS.csv",index=False)
"""
26 classes - so far 17 
that's why we have chosen to give teachers with the highest the 2 highest evaluation scores(5,4) so we can cover all 26 classes.
assuming they have unique positions(classes), we will see. 
 .
"""

secondbestscore_teachers["Assigned Classes"] = 1
secondbestscore_teachers["Total_number_classes_given"] = secondbestscore_teachers.iloc[:,2:28].sum(axis=1)

secondbestscore_teachers["Assigned Classes"] = 1
secondbestscore_teachers["Total_number_classes_given"] = secondbestscore_teachers.iloc[:,2:28].sum(axis=1)

secondbestscore_teachers.loc[secondbestscore_teachers["Total_number_classes_given"] > 4,["Assigned Classes"]] = "Number of Classes Assigned"
print(secondbestscore_teachers)
secondbestscore_teachers.to_csv("secondS.csv",index=False)


"""
Joining the 2 Data frames , and checks for duplicate keys 
"""
# frames = [Highestscore_teachers,secondbestscore_teachers]
# result1 = pd.concat(frames)
# print (result1)
result = pd.merge(Highestscore_teachers,secondbestscore_teachers,how="outer",validate="many_to_many")
result.to_csv("merge.csv",index=False)
print(result)
df = pd.read_csv("merge.csv")

"""
extra credit - reassign courses 
because of the method that we are applying.
every csv file that we previously created serves as a "Checkpoint"
So It's very simple to re-arrange classes again, by loading the previous " Checkpoint"
and then, changing it as needed. 
"""

# def rearange_Classes():
#     rg=pd.read_csv("highestS.csv",index=False)
#                                                 # we still having higher priority on teachers with the highest eva.Scores
#     rg1=pd.read_csv("secondS.csv",index=False)

#result = pd.merge(rg,rg1,on= )  # merging them once again on whatever different key we wanted is as simple as this
                                # or repeat the same concept that we did before

# rearange_Classes()