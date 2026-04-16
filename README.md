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




Task 3:


What you'll learn
How a dataset can be visualised in a variety of different ways generating a variety of narratives
What you'll do
Meet your supervisor Blaise, a data engineer at Quantium in the retail business area
Create a Dash app to visualise data in an informative way that answers your client’s question


Here is the background information on your task
Data visualisation is just as much an art as a science. A particular dataset can be visualised in countless ways, many misleading, but some useful. Think of each visualisation as a different narrative governed by the same facts. By changing the narrative while leaving the facts unchanged, the facts can be made to convey an entirely different point. Here there be dragons. This is the power of data analysis — you have a dangerous amount of control over the point you convey. It’s up to you to derive that point from the data, rather than forcing the data to support a point it doesn’t actually fit.

In this case, we want to figure out what impact the price increase of Pink Morsels had on overall sales. Take a moment to think about different ways we could visualise the data to answer this question. Ideas? In the interest of creating something simple that simply works (usually a good idea, and an excellent opportunity to reinforce the KISS principle), you’ll be implementing a line chart. It may not be the most interesting visualisation in existence, but it will likely answer Soul Foods’s question with minimal embellishment to the dataset. In other words, we get a raw, unadulterated look at the data and let the data speak for itself.






Here is your task
Your task is to create a Dash app to visualise the data you generated in the last task. Lean on the resources linked below to learn more about the basics of working with Dash. Your application must incorporate the following elements:
A header which appropriately titles the visualiser
A line chart which visualises the sales data generated in the last task, sorted by date. Be sure to include appropriate axis labels for the chart.
 
Recall the original purpose of the Dash app you are building — the goal is to answer Soul Foods’s question: “Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?” With the visualiser complete, the answer should be obvious. Congratulations, you just answered a pertinent business question using the awesome power of quantitative data. Soul Foods will be pleased to hear all about it!
 
When you are finished, commit and push your changes, then submit a link to your repo below!




Task 4

Task Overview
What you'll learn
Why it’s important and valuable to design a visually pleasing UI
What you'll do
Add a radio button to make your app interactive
Develop an intuitive UI that makes your Dash app visually impressive by applying some CSS to each element


Unsurprisingly, any good visualiser needs a visual component. The best data visualisers aren’t just useful but aesthetically pleasing as well. If you intend to work with data, do not underestimate the power of an intuitive, visually pleasing UI. Many data analysts overlook this component of their job, but you must remember that your app will be used by humans, not machines. By spending time on the look and feel of your visualiser, you’ll ensure that human users can navigate it intuitively and enjoyably. 

Think of it as showing affection to your visualiser, dressing it up before you put it on display for the world! To illustrate, look at this example from Dash: https://dash.gallery/dash-brain-viewer/. The developers who worked on this visualisation clearly thought about how people would interact with it and considered its visual appeal. The result is a visualiser that sucks you in — their data is fun to play with!

 

Here is your task

Soul Foods would like a way to dig into region-specific sales data for Pink Morsels. To this end, they’d like a radio button in your visualiser which allows them to filter sales data by region. Leaning on the resources linked below, add a radio button with five options to narrow which data appear in the line chart: “north,” “east,” “south,” “west,” and “all.”
 
Now it’s time to dress up your Dash app! Apply some CSS to each element to make your application more visually appealing. There are no requirements for this step other than that you put effort into making your visualiser interesting. The model answer contains an example styling, but the possibilities are infinite — make your visualiser your own!
 
When you are finished, commit and push your changes, then submit a link to your repo below!


Task 5


Task Overview
What you'll learn
Why good testing is important to avoid unintended consequences when making changes to a codebase
What you'll do
Create a test suite to verify your Dash app is working as expected


Here is the background information on your task
Testing is the practice of programmatically ensuring the thing you built behaves as expected. Let’s consider a theoretical situation you could find yourself in someday. Consider a potential future where you work on a massive codebase, something with hundreds of thousands of lines of code — countless interconnected components all communicating with each other, passing data back and forth at high speeds in incomprehensible patterns. 

The system is a decade old, and the engineers who originally designed and built it have moved on to other things. Despite having worked on the system for months, its sheer scale has prevented you from completely understanding how every part of the system works. Now suppose you are asked to make a change to the system — modify some esoteric class deep within the bowels of the thing. How would you know your change hasn’t broken some heavily patched component with an obscure relationship to the class you modified? The answer is good testing.

Any production-grade codebase will have an equally robust test suite associated with it. For every granular piece of behaviour in the system, there will be a corresponding collection of tests which ensure it behaves as expected. These tests can be run nigh-instantaneously, and if any slice of code does something unexpected, it will register as a failed test (if properly written). When modifying code, you can run the test suite to ensure you haven’t broken anything. 

It’s one of the many boons of good testing, more of which are described in the linked resources. In this task, your job is to draft a test suite to ensure the visualiser works as expected. These tests may seem trivial, but they are illustrative of an imperative coding practice. Poorly tested production code inevitably leads to sleepless nights for all involved.




Here is your task
Your task is to create a test suite to verify your Dash app is working as expected. Using the standard Dash testing framework (documentation linked in the resources below) write three tests which ensure the following:
The header is present.
The visualisation is present.
The region picker is present.
Execute your test suite using Pytest and ensure each test passes.
Commit and push your changes, then submit a link to your repo below.


Task 6:

Task Overview
What you'll learn
What continuous integration is and why it is useful for developers
What you'll do
Implement a bash script, which automatically runs the test suite


Bonus task!
This is an optional bonus task! If you do not wish to complete it, please type N/A into the text field below to finish the program. 

Background information

Continuous integration is the practice of frequently merging the feature branch you are working on with the main branch shared by everyone else working on the same codebase. The goal of continuous integration is to replace large, conflicting merges with smaller, gradual changes. Consider a scenario wherein four developers are working on different parts of the same codebase. This codebase has a main branch, as well as a one-feature branch per developer.

Three of the developers are using a continuous integration workflow. They make small incremental changes, commit them, and merge their feature branches into main several times a day. The fourth developer decides against the practice, creates a feature branch when they start work on their ticket, and does not attempt to merge until a week later when it is complete. Unfortunately, the main branch has changed significantly by the time dev four attempts to merge their feature branch. 

They now must spend a significant amount of time combing through merge conflicts just to merge their feature branch. Needless to say, they don’t have a good time. The three developers using a CI workflow kept their feature branches relatively up to date with main, and as such, spent far less time resolving merge conflicts and more time on the company ping-pong tables.

Furthermore, most CI engines have powerful automated testing and deployment capabilities. In addition to avoiding merge conflicts, the CI engine ensures all tests pass with each commit and can even deploy them to staging environments. As such, developers are instantly made aware that their code behaves as expected when combined with everyone else's. In this task, you will focus on the test automation side of CI — your goal is to make the test you created in the last task executable by a CI engine.

Task instructions

In this task, you will implement a bash script, which automatically runs the test suite you created in the last task. You could integrate this script into a CI engine to allow the test suite to run automatically. The bash script should do the following:

Activate the project virtual environment.
Execute the test suite.
Return exit code 0 if all tests passed, or 1 if something went wrong.