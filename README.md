# Quantium starter repo
This repo contains everything you need to get started on the program! Good luck!


Task 1:

Task Overview
What you'll learn
Meet your clients Soul Foods who have seen a decline in sales on their top performing candy product
How a software engineer at Quantium supports clients to understand the impact of their decisions on profitability
What you'll do
Meet your supervisor Priscilla, a software engineer at Quantium in the financial services business area
Set up your local development environment


Here is the background information on your task
With little more than a few requirements and a messy data set to reference, it’s time to take a swing at this project. While Quantium has a few core tech stacks they work with on a regular basis, a small interactive visualisation like this one is perfectly suited to the Dash framework. Dash is a Python framework for developing visual tools to interrogate data. It’s easy to use, quick to develop with, and results in a pretty finished product. Before you can get to work on the application itself, set up your local development environment for working with Dash. Your local development environment can be thought of as a workbench with all the tools necessary to progress on a project. Invest an adequate amount of time setting up a good workbench and development on any project will be made far easier.


Here is your task
To begin, get your hands on the starter repo - fork and clone it to your machine using this link. If this step is confusing, read the first two chapters of the Git book linked below.
 
Open the project in your IDE of choice — feel free to use any Python IDE you’re comfortable with. If you don’t have a favourite Python IDE yet, look at Pycharm Community Edition. It’s a well-designed IDE by Jetbrains packed with features and plugins, powerful enough to work on the most complex projects, and entirely free.
 
One of the best ways to manage dependencies in Python is with virtual environments. Each virtual environment contains a Python interpreter and a collection of project dependencies. They are entirely encapsulated in a single folder, and easy to work with once you get the hang of them. For this project, you will set up a Python 3.9 virtual environment. Review the resources linked below for more information.
 
Next, add the dash and pandas packages as dependencies to your virtual environment. Instructions for this step can be found in the Resources section below.
 
With your virtual environment active, run `pip install "dash[testing]"` (without backticks) to install all the necessary dash testing dependencies.
 
Congratulations! You’ve completed the bulk of the work for this task and now have access to a fully-featured workbench. All that’s left is to submit your work. Commit your changes and push them to GitHub!
 
You’re done! Submit a link to your repo below!

Estimated time for task completion: 30-60 minutes depending on your learning style.





Task 2: Data Processing

1

2

3

4

5
Task Overview
What you'll learn
What data processing is and why it is important
What you'll do
Meet your supervisor Liam, a software engineer at Quantium
Perform some data processing to reorganise the data into a format that you can work with





Here is the background information on your task
In this task, you will become familiar with the art of data processing. Data processing is the esoteric practice of squishing data into a useful format. Data points themselves — raw quantities in isolation — are useless but become useful when arranged in thoughtful proximity with other data points. When done skilfully, a carefully organized corpus of data can be interrogated for useful information: answers to difficult questions, surprising insights which were initially hidden, and elusive trends which can quite literally be used to predict the future. There is an immense power buried in the sea of data collected with nonchalant regularity all around the world which can be harnessed if you choose to do so. The first step in the transmutation of data into information is a process affectionately referred to as “data processing”.

By way of illustration, Soul Foods has asked the question, “Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?” Seems like a useful thing to know if you’re the one making those sorts of decisions. But all you have at your disposal are a few CSV files with a handful of seemingly random columns. Attempt to answer the question by simply looking at the available data. The answer isn’t very obvious, is it? Your task is to mould that raw material into something useful.



Here is your task
Soul Foods has provided you with three CSV files, all of which are in the data folder of the starter repo you cloned in the last task. These CSV files contain transaction data for Soul Foods’s entire morsel line. Each row indicates the quantity of a given type of morsel sold in a given region at a given price on a given day. Take a moment to acquaint yourself with the data contained in each one of these files.
 
Next, we’ll go field by field and think about how we can use each one:
The first field, “product”, contains many different types of morsels. Soul Foods is only interested in Pink Morsels, so we can remove any row which contains another type of product.
Next come “quantity” and “price”. Since we’re interested in the total sales for a given day, these can be combined into a single field, “sales,” by multiplying them together.
The date field is useful as is and can remain untouched.
It would be nice to filter by region in the final visualisation, so we’ll also leave the region field untouched.
 
Your task is to use the above instructions to convert the three CSV files into a single formatted output file. Your output file should contain three fields:
Sales
Date
Region
 
When you are finished, commit and push your changes, then submit a link to your repo below!


