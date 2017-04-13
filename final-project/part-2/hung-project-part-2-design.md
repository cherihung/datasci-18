# Final Project Design Writeup - Cheri Hung

### Project Problem and Hypothesis

This project aims to find the cause for food cost overage in a given restaurant. Food cost overage is an indication of waste or mismanagement. In any case, it is a major business concern. The goal is to determine factors that can be used to predict whether overage is likely to occur for a particular food item. The factors include: _gross sales_ as a proxy for demand, _type of menu items used for the food item_, _inventory order pattern_. The goal is to create a model for making such prediction which would help project or estimate chance of overage.

### Datasets

The data is based on a single restaurant's management data that my company has access to. The data is stored in SQL database. There are APIs to access aggregated data for quick view but raw datasets used for this project will come from the database. This project will require combining SQL queries to produce a dataset that include all the variables needed. Or, alternatively, I'll do the combination of multiple tables into one dataframe in ipython notebook.

Te relevant data tables from the SQL database are as follow:

The key metric to use is *variance*, which is calculated by the system as *Actual Cost - Ideal Cost* for an inventory item.

*On a single item table, the fields are as below:*

| ProductId | ProductName | BeginningInventory  | OrdersReceived | EndingInventory | ActualUsage | IdealUsage | Variance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 756 | POULTRY - CHX WING | 2094 | 2730 | 1827.5 | 2996.5 | 2478 | 518.5 |

*Each food item can then be paired with a query to inventory order records of the same time period, like below:*
This table will be aggregated into a sum of total number of orders. The hypothesis is that more orders means less efficiency in inventory management and leads to higher overage. Because, typically, there is a minimum number of units in an order.

| ProductId | ProductName | Date  | Invoice | Orders | RecipeUnits | InventoryUnits |
| --- | --- | --- | --- | --- | --- | --- |
| 756 | POULTRY - CHX WING | 04/06/2017 | #616583667 | 3 | 630 | 120 |
| 756 | POULTRY - CHX WING | 04/06/2017 | #616601721 | 4 | 840 | 160 |
| 756 | POULTRY - CHX WING | 04/08/2017 | #616617104 | 6 | 1260 | 240 |

*To get the menu items using this food item, another query will need to be paired to table, like below:*
This table will be aggregated into a sum of total number of menuItems and then associated with each food item in the final dataset.

| Id | MenuItem |
| --- |---|
| 1210 | Naked Wings - 6 |
| 1211 | Naked Wings - 12 |
....

### Domain knowledge

Personally, I have been working on this management system for a few months and have a good understanding of a typical restaurant operation as well as how the data is collected into the system.

This current management system provides many types of reports on food cost overage (i.e. variance) in the system. These reports are centric on aggregating that metric and pairing it with sales-related metrics (i.e. Gross Sales). It is also useful for tracking and trending. For this project, these analysis can help in providing some intuition about the data overall.

There are other management system in the market that advertises this predictive feature. But they aren't useful for this project since the models and algorithm used are proprietary.

### Project Concerns

I am most concerned that none of the proposed factors can provide enough correlative value to make a good prediction. They all appear to have relevance on the variance value. But there are a variety of factors and even confounding variables that contribute food cost overage. For example, unanticipated higher or lower sales/demand due to holidays, weather or other environmental factors. So I have to really think about the timeframe used.

Also, the metric "variance" is calculated based on _Ideal Cost_ entered by the user. This means we are assuming that the user has calculated that cost correctly and that it does not change often, which I don't believe it does. This is a major risk and assumption for this project. Yet, I don't think there is any way around this data entry issue. So the predictive model might not translate well across different restaurants. But, my hope is that the model will be valid up to a regional chain in which recipes, cost estimates and sale estimates can be somewhat consistent.

Another concern I have is being able to standardize units of items. For example, somehow being able to normalize between 1 lbs of shrimp and 1 can of tomatoes for example.

### Outcomes

I would expect the outcome to be a logistic regression model that I can input one or more X variables. And the model would output a true/false prediction on whether overage is likely to occur.  

The target audience for this project at this point is the internal stakeholders (i.e. my company and development team). The output would be a piece of code that the development team can use to plugin in various data and produce a prediction. A ipython notebook should be sufficient for this purpose for the internal audience to evaluate the methodology and model. Ultimately, I would hope this could transition to external target audience (i.e. restaurants) for testing.

Also would expect to utilize any relevant visualizations to explain the regression model.

As the project help identify the most important feature, I expect to be able to recommend further actions on that factor. It is hard to define at this point. But an example would be to better control the scheduling of when to order more inventory. Or, simply be able to allow the managers to plan for overage at a certain period.

As stated earlier, this is a problem with many seemingly correlating variables. Being able to produce a model with statistically accuracy for making prediction would be considered a success. And from that, I would hope further work can be done on trying to predict a range of overage. However, a bust, meaning ending with no viable model that can point to a X variable as a predictor, I'd hope the project could at least signal a reason for why this modeling failed. If it's a matter of features used, perhaps explore other data points that may or may not reside in our database already. If it's a matter of the machine learning model used, perhaps explore another model.
