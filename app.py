from flask import Flask, render_template, request
from functionality.amount import get_amount
from functionality.payment import make_payment
from db.fake_db import impact_choices

app = Flask(__name__)


@app.route('/overview/<int:user_id>')
def amount(user_id: int):
    user_amount, _name = get_amount(user_id)
    return render_template('overview.html', amount=user_amount, name=_name)


@app.route('/payment', methods=["POST"])
def payment():
    req_data = request.get_json(force=True)
    response, tokens = make_payment(payer_iban=req_data['payer_iban'],
                                    payee_iban=req_data['payee_iban'],
                                    payment_amount=req_data['payment_amount'],
                                    sort_code=req_data['payee_iban'][:2])

    print(response)
    return render_template('cashback.html', name=response["payer"], tokens=tokens)


@app.route('/choices', methods=["GET"])
def choices():
    """
    Export impact choices and token value
    """
    return render_template('impact.html', choices=impact_choices)


if __name__ == '__main__':
    app.run(debug=True)
