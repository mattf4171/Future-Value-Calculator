"""
This flask app will provide free resources to users who are intrested in future value

"""
from flask import Flask, render_template, request

app = Flask(__name__)

def predict_bond_FV(investings):
    """
    Show average annual Total Returns for 1, 3, 5, & 10 years in Bond Market
    """
    avg_annual_tot_returns_bond = []
    one_yr = investings + (investings * (-0.1035))
    three_yr = investings + (investings * (-0.0093))
    five_yr = investings + (investings * (0.0086))
    ten_yr = investings + (investings * (0.0150))
    avg_annual_tot_returns_bond.append([one_yr, three_yr, five_yr, ten_yr])
    return avg_annual_tot_returns_bond

def predict_stock_FV(investings):
    """
    Show average annual Total Returns for 1, 3, 5, & 10 years in Fidelity 500 Index
    """
    avg_annual_tot_returns_stock = []
    one_yr = investings + (investings * (-0.1063))
    three_yr = investings + (investings * (0.1059))
    five_yr = investings + (investings * (0.1129))
    ten_yr = investings + (investings * (0.1295))
    avg_annual_tot_returns_stock.append([one_yr, three_yr, five_yr, ten_yr])
    return avg_annual_tot_returns_stock

@app.route("/")
def index():
    
    # # Load current count
    # f = open("count.txt", "r")
    # count = int(f.read())
    # f.close()

    # # Increment the count
    # count += 1

    # # Overwrite the count
    # f = open("count.txt", "w")
    # f.write(str(count))
    # f.close()

    # Render HTML with count variable
    # return render_template("index.html", count=count)

    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def futureVal():
    # TODO: try catch for int or otherwise
    if request.form.get('indexButton') == 'VALUE1':
        investings = str(request.form.get('invest_amount')).strip(',$')
        print(investings)
    # predict_bond_FV(int(investings))
    # predict_stock_FV(int(investings))

    print('bond_FV: ',predict_bond_FV(int(investings)))
    print('stock_FV: ',predict_stock_FV(int(investings)))
    return render_template("futureVal.html", bond_FV = predict_bond_FV(int(investings)), stock_FV = predict_stock_FV(int(investings)))#, bond_FV = predict_bond_FV(int(investings)), stock_FV = predict_stock_FV(int(investings)))


if __name__ == "__main__":
    app.run()