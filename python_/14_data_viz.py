#import libraries
import seaborn as sns
import matplotlib.pyplot as plt

#set a theme
sns.set_theme(style="ticks", color_codes = True)

#import dataset
kashti = sns.load_dataset("titanic")
#print(kashti)


# #plot basic graph
# p = sns.countplot(x= "sex", data = kashti)
# plt.show()


# #plot with two variables graph using hue
# p = sns.countplot(x= "sex", data = kashti ,hue= "class" )
# plt.show()


#plot two variables with titles
p = sns.countplot(x= "sex", data = kashti ,hue= "class" )
p.set_title("COUNT PLOT")
plt.show()

