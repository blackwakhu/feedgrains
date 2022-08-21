from flask import Flask, request, render_template
import numpy as np
from items import GroupCommod, GroupGeography, Commodity, Attribute, SortOrder, TimePeriod, Unit
import pickle

app = Flask(__name__)
model = pickle.load(open('decisiontree.pkl','rb'))

groupcommod, groupcommod_id = GroupCommod()
groupgeography, groupgeography_id = GroupGeography()
commod, commod_id = Commodity()
attribute, attribute_id = Attribute()
unit, unit_id = Unit()
timep, timep_id = TimePeriod()
sort_order = SortOrder()

@app.route('/')
def home():
    return render_template('index.html', groupcommod=groupcommod, groupcommod_id=groupcommod_id,groupgeography=groupgeography, groupgeography_id=groupgeography_id, commod=commod, commod_id=commod_id,
    attribute=attribute, attribute_id=attribute_id, unit=unit, unit_id=unit_id, timep=timep, timep_id=timep_id, sort_order=sort_order)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    initial = [float(x) for x in request.form.values()]
    final = np.array(initial).reshape(1,-1)
    predictiction = model.predict(final)
    return render_template('index.html', prediction=f'the amount is {predictiction[0]}', groupcommod=groupcommod, groupcommod_id=groupcommod_id,groupgeography=groupgeography, groupgeography_id=groupgeography_id, commod=commod, commod_id=commod_id,
    attribute=attribute, attribute_id=attribute_id, unit=unit, unit_id=unit_id, timep=timep, timep_id=timep_id, sort_order=sort_order)

if __name__ == "__main__":
    app.run()