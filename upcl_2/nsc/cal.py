from flask import Flask, request

app = Flask(__name__)

@app.route('/generate_bill', methods=['POST'])
def generate_bill():
    # Read the input data from the request
    data = request.get_json()
    units_consumed = data.get('units_consumed')

    # Calculate the bill amount
    bill_amount = 0
    if units_consumed <= 100:
        bill_amount = units_consumed * 1.2
    elif units_consumed <= 200:
        bill_amount = 100 * 1.2 + (units_consumed - 100) * 1.5
    else:
        bill_amount = 100 * 1.2 + 100 * 1.5 + (units_consumed - 200) * 2.0

    # Return the bill amount
    return {'bill_amount': bill_amount}

if __name__ == '__main__':
    app.run()
