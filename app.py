"""
This flask app will provide free resources to users who are intrested in future value

"""
from flask import Flask, render_template, request, abort

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
    avg_annual_tot_returns_bond.append([1,one_yr])
    avg_annual_tot_returns_bond.append([3, three_yr])
    avg_annual_tot_returns_bond.append([5,five_yr])
    avg_annual_tot_returns_bond.append([10,ten_yr])
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
    avg_annual_tot_returns_stock.append([1,one_yr])
    avg_annual_tot_returns_stock.append([3, three_yr])
    avg_annual_tot_returns_stock.append([5,five_yr])
    avg_annual_tot_returns_stock.append([10,ten_yr])
    return avg_annual_tot_returns_stock

@app.route("/")
def index():
    return render_template("index.html", err_msg="")

@app.route('/predict', methods=["POST", "GET"])
def futureVal():
    # TODO: try catch for int or otherwise
    while True:
        try:
            if request.form.get('indexButton') == 'Calculate':
                investings = str(request.form.get('invest_amount')).strip(',$')
                print(investings)
            if request.form.get('indexButton') == 'Recalculate':
                print("Recalculate Now...")
                return render_template("index.html", err_msg="")
            break
        except ValueError:
            print('Please enter a number:')
            abort(ValueError)


    print(predict_bond_FV(int(investings)))
    return render_template("futureVal.html", investings = investings, bond_FV = predict_bond_FV(int(investings)), stock_FV = predict_stock_FV(int(investings)) )#, bond_FV = predict_bond_FV(int(investings)), stock_FV = predict_stock_FV(int(investings)))

# @app.route('/home', methods="POST")
# def recalculate():
#     if request.form.get('indexButton') == '':
#         return render_template("index.html", err_msg="")

if __name__ == "__main__":
    app.run()