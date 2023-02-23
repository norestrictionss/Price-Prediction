from flask import Flask, render_template, url_for, redirect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from model.main import linear_regression
from model.main import x_train, y_train
import pandas as pd

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = 'secret key'
result = []


class HouseForm(FlaskForm):
    area = StringField(label='Area', validators=[DataRequired()])
    number_of_bath = StringField(label='Number of Bath', validators=[DataRequired()])
    number_of_bedroom = StringField(label='Number of Bedrooms', validators=[DataRequired()])
    submit_button = SubmitField(label='Submit')


@app.route('/index', methods=['POST', 'GET'])
def index():
    form = HouseForm()
    if form.validate_on_submit():
        dataset = {'area': form.area.data,
                   'bedrooms': form.number_of_bedroom.data,
                   'bathrooms': form.number_of_bath.data}
        data = [[form.area.data, form.number_of_bedroom.data, form.number_of_bath.data]]

        dataframe = pd.DataFrame(data, columns=['area', 'bedrooms', 'bathrooms'])
        result = linear_regression(x_train, y_train, dataframe)
        result = result.iloc[0,0]
        print("Estimated price for input values is: ", result)
        return redirect(url_for('index'))
    return render_template('app.html', form=form)


if __name__ == '__main__':
    from waitress import serve

    serve(app, port=8080)
