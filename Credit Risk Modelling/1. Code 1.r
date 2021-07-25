# install.packages("dplyr")
# install.packages("readxl")

getwd()
setwd('C:/Users/redhw/OneDrive/Documents/GitHub/Python-Code-Testing/Credit Risk Modelling')

data = readxl::read_excel('candy-data.xlsx')

# model = LinearRegression().fit(candy['chocolate'].values.reshape(-1,1), candy['winpercent'])
model = lm(winpercent ~ chocolate + fruity -1,data = data)

summary(model)

# a