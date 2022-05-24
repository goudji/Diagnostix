import sys
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from wtforms import validators, SubmitField
from replit import db
 
app = Flask(__name__)



class SubmitForm(FlaskForm):
    submit = SubmitField('submit')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home/', methods=['post', 'get'])
def home():
    return render_template('home.html')

testarr=[]

@app.route('/symptoms', methods=['GET', 'POST'])
def symptoms():
    testarr = request.form.getlist('s')
    print(testarr)
    if request.method == 'POST':
      #testarr=float(testarr)
      def Machinelearn(testarr):
        if len(testarr)>0:
          l = []
          for  x in range (0, 132):
            l.append(0)

          for i in testarr: 
            l[int(i)] = 1


          TestData=l
          print(TestData)
          logmodel = LogisticRegression()

          diseasesTrain_data = pd.read_csv('Training.csv')
          

          diseasesTrain_data.dropna()
          

          X = diseasesTrain_data.iloc[:, 0:132]
          y = diseasesTrain_data['prognosis']
          Test_X = TestData
          
          model = DecisionTreeClassifier()
          logmodel.fit(X, y)

          predictions = logmodel.predict( [Test_X] )
          
          return predictions

      Pred=Machinelearn(testarr)
      print(testarr)
      print(Pred)
      a=Pred[0]
      
      #a=str(Pred)

      print(a)
      return redirect(url_for('disease', disease = a))
      
    return render_template("symptoms.html")



@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/disease/<disease>')
def disease(disease):
  #return disease
  return render_template("disease.html", value=disease)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)



###########################################################################################################################################################################################################################################################






















if (len(testarr)>0):

  newarr=np.array([132])

  for i in range(len(newarr)):
    if (testarr(i)!=0):
      newarr(i).append(testarr(i))
    else:
      newarr(i)==0

  print(newarr)


















ar = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain','stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue','weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat','irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion','headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)','depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic_patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']
for x in range(0, len(ar)):
    if '_' in ar[x]:
        ar[x] = ar[x].replace('_', ' ')

'''dictionary = {}
for y in range(1, len(are)+1):
    dictionary[y] = are[y-1]

dict2 = {}
for symptom in ar:
  dict2[symptom] = 0

for i in testarr: 
  dict2[dictionary[i]] = 1'''

l = []
for  x in range (0, 132):
  l.append(0)

for i in testarr: 
  l[i] = 1




  '''@app.route('/route_name')
def script_output():
    output = execute('./script')
    return render_template('template_name.html',output=output)



    <p>{{ output }}</p>'''