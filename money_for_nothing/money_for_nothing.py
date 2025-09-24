import json
import sys

def is_validJSON(json_data):
    """
    Checks if a JSON object is valid.
    
    This function checks whether a JSON object exists and is not empty.
    
    Args:
        json_data (dict or list): The JSON data to validate.
    
    Returns:
        bool: True if the JSON object is valid, False otherwise.
    """
    if not json_data:
        print("[]")
        return False
    return True

def maximize_profit(prediction):
    """
    Maximizes profit based on predicted stock prices.

    This function takes a list of predicted prices of a stock over a period of time
    and determines the optimal buying and selling points to maximize profit.
    It follows a strategy where the investor sells first before buying again to ensure short-term profit.

    Args:
    prediction (list of int): A list of integers representing the predicted prices of the stock over time.

    Returns:
    list of int: A list of integers representing the indices where it is optimal to buy and sell the stock.
    The first index corresponds to a buy action, the next to a sell action, and so on.
    If no buying/selling action leads to profit, an empty list is returned.
    """

    buy_sell_indices = []
    buying = False
    for i in range(len(prediction) - 1):
        if not buying:
            if prediction[i] < prediction[i + 1]:
                buy_sell_indices.append(i)
                buying = True
        else:
            if prediction[i] > prediction[i + 1]:
                buy_sell_indices.append(i)
                buying = False

    if buying:
        buy_sell_indices.append(len(prediction) - 1)

    return buy_sell_indices

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <json_list>")
        sys.exit(1)

    json_data_str = sys.argv[1]

    try:
        prediction = json.loads(json_data_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data: {e}")
        sys.exit(1)

    if is_validJSON(prediction):
        result = maximize_profit(prediction)
        print(json.dumps(result))
