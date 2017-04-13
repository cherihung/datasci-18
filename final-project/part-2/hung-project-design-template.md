# Final Project Design Writeup - Cheri Hung

### Project Problem and Hypothesis

This project aims to find the cause for food cost overage in a given restaurant. Food cost overage is an indication of waste or mismanagement. In any case, it is a major business concern. The goal is to determine factors that can be used to predict whether overage is likely to occur for a particular food item. The factors include: _gross sales_ as a proxy for demand, _type of menu items used for the food item_, _inventory order pattern_. The goal is to create a model for making such prediction which would help project or estimate chance of overage.

### Datasets

The data is based on a single restaurant's management data that my company has access to. The data is stored in SQL database. There are APIs to access aggregated data for quick view but raw datasets used for this project will come from the database.

The key metric to use is *variance*, which is calculated by the system as *Actual Cost - Ideal Cost* for an inventory item. On a single item table, the fields would be like below:

| ProductId | ProductName | BeginningInventory  | OrdersReceived | EndingInventory | ActualUsage | IdealUsage | Variance |
| ------------- |:-------------:| -----:|
| 756 | POULTRY - CHX WING | 2094 | 2730 | 1827.5 | 2996.5 | 2478 | 518.5 |

Each food item can then be paired with a query to inventory order records, like below:

| ProductId | ProductName | Date  | Invoice | Orders | RecipeUnits | InventoryUnits |
| ------------- |:-------------:| -----:|
| 756 | POULTRY - CHX WING | 04/06/2017 | #616583667 | 3 | 630 | 120 |
| 756 | POULTRY - CHX WING | 04/06/2017 | #616601721 | 4 | 840 | 160 |
| 756 | POULTRY - CHX WING | 04/08/2017 | #616617104 | 6 | 1260 | 240 |

To get the menu items using this food item, another query will need to be paired to table, like below:

| Id | MenuItem |
| ------------- |:-------------:| -----:|
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
* What do you expect the output to look like?
* What does your target audience expect the output to look like?
* What gain do you expect from your most important feature on its own?
* How complicated does your model have to be?
* How successful does your project have to be in order to be considered a "success"?
* What will you do if the project is a bust (this happens! but it shouldn't here)?
