from django.shortcuts import render
# from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from pathlib import Path
# Create your views here
from bs4 import BeautifulSoup
import requests
import os
from html.parser import HTMLParser
BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)

file_path = os.path.join(BASE_DIR, 'cleaned_file.csv')
df = pd.read_csv(file_path)


x = df.iloc[:, :-1]
y = df['output']
model_random = RandomForestClassifier(n_estimators=350)
model_random.fit(x, y)

#web srapping part
res = requests.get('https://medlineplus.gov/howtopreventheartdisease.html')
soup = BeautifulSoup(res.text,'html.parser')
ifAtHighRisk=soup.select('#topic-summary > ul:nth-child(6)')
# ifAtHighRisk1 = soup.find('')
print('lenght of scrap is ',len(ifAtHighRisk[0]))
print(ifAtHighRisk[0])
print('type of doup s s   ',type(ifAtHighRisk[0]))
# html_doc = HTMLParser.feed(ifAtHighRisk[0])

def home_page(request):

    if request.method == 'POST':
        age = request.POST.get('age', None)
        # print(int(age))
        gender = request.POST.get('gender', None)
        if gender == 'male':
            male = 1
            female = 0
        else:
            female = 1
            male = 0
        restingbloodpressure = request.POST.get('R_B_P', None)
        cholestrol = request.POST.get('chol', None)
        maxheartrate = request.POST.get('heart_rate', None)
        treadmill_ecg = request.POST.get('treadmill_ECG', None)
        fasting_blood_sugar = request.POST.get('fbs', None)
        if int(fasting_blood_sugar) == 1:
            print("working")
            greater_than_120 = 1
            less_than_120 = 0
            bloodSugarResult = 'Greater than 120mg/dl'
        else:
            print("working")
            greater_than_120 = 0
            less_than_120 = 1
            bloodSugarResult = 'Less than 120mg/dl'
        # print('the type is ', type(fasting_blood_sugar))

        rest_ecg = request.POST.get('rest_ecg')

        if int(rest_ecg) == 0:
            normal = 1
            abnormal = 0
            hypernormal = 0
            restECGResult = 'Normal'
        elif int(rest_ecg) == 1:
            normal = 0
            abnormal = 1
            hypernormal = 0
            restECGResult = 'Abnormal'
        else:
            normal = 0
            abnormal = 0
            hypernormal = 1
            restECGResult = 'HyperNormal'

        agina_ex = request.POST.get('agina_ex')

        if int(agina_ex) == 0:
            agin_no = 1
            agin_yes = 0
            painAfterExercise = 'No doesn\'t have a chest pain' 
        else:
            agin_no=0
            agin_yes=1
            painAfterExercise = 'Yes does have a chest pain'

        ecg_graph_trend = request.POST.get('graph')

        if int(ecg_graph_trend) == 0:
            upsloping = 1
            flat = 0
            downsloping = 0
            ecgGraphTrenResults = 'Upsloping'
        elif int(ecg_graph_trend) == 1:
            upsloping = 0
            flat = 1
            downsloping = 0
            ecgGraphTrenResults = 'Flat'
        else:
                upsloping = 0
                flat = 0
                downsloping = 1
                ecgGraphTrenResults = 'downsloping'

        fluroscopy = request.POST.get('color')

        if int(fluroscopy) == 0:
            colored_1 = 1
            colored_2 = 0
            colored_3 = 0
            fluroscopyResults = 'it is a colored 1 stage'
        elif int(fluroscopy) == 1:
            colored_1 = 0
            colored_2 = 1
            colored_3 = 0
            fluroscopyResults = 'it is a colored 2 stage'
        else:
            colored_1 = 0
            colored_2 = 0
            colored_3 = 1
            fluroscopyResults = 'it is a colored 3 stage'

        thalassemia = request.POST.get('thall')

        if int(thalassemia) == 0:
            thall_normal = 1
            fixed_deffect = 0
            rev_defect = 0
            thallResults = 'Normal'
        elif int(thalassemia) == 1:
            thall_normal = 0
            fixed_deffect = 1
            rev_defect = 0
            thallResults = 'fixed defect'
        else:
            thall_normal = 0
            fixed_deffect = 0
            rev_defect = 1
            thallResults = 'reverse defect'

        agina_level = request.POST.get('agina_level')

        if int(agina_level) == 0:
            typ_agina = 1
            atyp_agina = 0
            non_agn_pain = 0
            asymp = 0
            chestPainResult = 'typical agina'
        elif int(agina_level) == 1:
            typ_agina = 0
            atyp_agina = 1
            non_agn_pain = 0
            asymp = 0
            chestPainResult = 'Atypical agina'
        elif int(agina_level) == 2:
            typ_agina = 0
            atyp_agina = 0
            non_agn_pain = 1
            asymp = 0
            chestPainResult = 'Non Aginal Pain'
        else:
            typ_agina = 0
            atyp_agina = 0
            non_agn_pain = 0
            asymp = 1
            chestPainResult = 'Asymtomatic pain '
            # print(type(agina_level),'sdsds')


        pass_value = {
            
            'Age': age,
            'Gender': gender.upper(),
            'Resting Blood pressure ': restingbloodpressure,
            'Cholestrol level ':cholestrol,
            'Maximum Heart Rate': maxheartrate,
            'Tredmill ECG numbers ': treadmill_ecg,
            'Fasting Blood sugar': bloodSugarResult,
            'ECG result type ': restECGResult,
            'Chest pain after doing an exersice?': painAfterExercise,
            'ECG grapg trend ': ecgGraphTrenResults,
            'Fluroscopy Results ': fluroscopyResults,
            'Thalasemia ': thallResults,
            'Chest pain Level ': chestPainResult
        }
        input_list = [int(age), female, male, int(restingbloodpressure), int(cholestrol),
                      int(maxheartrate), float(treadmill_ecg),  less_than_120,greater_than_120,
                      normal, abnormal, hypernormal, agin_no, agin_yes, upsloping, flat, downsloping,
                      colored_1, colored_2, colored_3, thall_normal, fixed_deffect, rev_defect,
                      typ_agina, atyp_agina, non_agn_pain, asymp]

        final_result = model_random.predict([input_list])
        print(f'{final_result[0]} is the final result')
        # print(model_random.predict([input_list]))
        print(input_list)
        team_info = zip(pass_value.keys(),pass_value.values())

        return render(request, 'result.html', {'pass_value': team_info, 'attack_result': final_result[0],'title':'results',
                                               'ifAtHighRisk': ifAtHighRisk[0]})
    else:
        return render(request, 'index.html')


def results_page(request):
    if request.method == 'POST':
        return render(request, 'index.html')
    else:
        return render(request, 'result.html')
