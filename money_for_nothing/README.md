# Stock Market Investment Optimizer

## 1 - Problem Analysis

### 1.1 - Summary
The goal is to determine the optimal buying and selling points for a stock investment, aiming for short-term profit.

### 1.2 - Input
The path to a JSON file containing a list of predicted stock price changes over time, from left to right. This file is mandatory. Here's an example of the file content:

'[108, 45, 216, 215, 213, 96, 167, 245]'


### 1.3 - Output
The result (i.e., the optimal investment entries and exits) must be displayed on the terminal's standard output and must be a JSON object.

### 1.4 - Context
The context involves devising a buying and selling strategy to maximize short-term profits.

Analyzing the context, we understand that:
- We need to open and read a data file.
- Analyze the data in this file.
- Apply a strategy based on the action taken, i.e., buying or selling.
- Return the result.

## 2 - Problem Resolution

To determine the algorithmic solution to implement, we need to understand the buying and selling conditions based on the stock price over time. We iterate through the list except for the last price (as there's no successor) and compare successors. If we try to sell and reach the last index, we sell. If the last index still doesn't allow any profit, we don't make a purchase and return an empty list.

### 2.1 - Buying Condition
If the investor's last action was to buy, do nothing.
Otherwise, check if the current price is lower than the successor's price (i+1).
If so, we buy. Now, we need to try selling.

### 2.2 - Selling Condition
If we are in selling mode, check if the current price (i) is higher than the successor's price (i+1). If so, we sell. Now, we need to try buying.

### 2.3 - Intermediate Solution
I came up with this idea directly. It's simple but very effective.

## 3 - Evaluate the Solution

### 3.1 - Accuracy
The results are accurate, and the algorithm works with a variety of different input data.

### 3.2 - Complexity
The overall complexity of this algorithm mainly depends on the size of the JSON file and the list of price predictions. In the worst case, the complexity can be considered linear (O(n)), where n is the size of the input data.
