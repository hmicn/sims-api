from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/orders", methods=["POST"])
def trade_day():
    # receive the trading data from the POST request
    data = request.get_json()
    """
    The received data contains:
    - symbol: the stock ticker, for example MSFT
    - date: the trading date
    - open: the price at the start of the trading session
    - close: the price at the end of the trading session
    - high: the highest price reached during the day
    - low: the lowest price reached during the day
    - volume: the total number of shares traded during the day
    """

    # Populate the response with the required keys and values based on the received data
    response = {
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)