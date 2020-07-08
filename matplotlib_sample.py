# importing
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set()


#fig = plt.figure()
#ax = fig.add_subplot(2,2,1)

#or

#fig, ax = plt.subplots()


# Preparing the plots
# ax[0] - subplot
ax[0].hist(compare_3d_df_cl.budget_change, 50, density=True, facecolor='g', alpha=0.75)
ax[0].hist(compare_3d_df_cl.budget_change, bins = np.arange(min(d), max(d) + 500, 500))

# Для нескольких графиков:
for combo in zip(['category1', 'category2'], ax):
    combo[1].set_title(combo[0])

# Saving
fig.savefig('temp.png')

# Good article on OOP approach
https://medium.com/@kapil.mathur1987/matplotlib-an-introduction-to-its-object-oriented-interface-a318b1530aed

#Questions
#понятно, что такое multiple subplots, но что насчет multiple axes? это просто список subplots?
