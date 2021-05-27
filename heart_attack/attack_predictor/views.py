from django.shortcuts import render
# from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from pathlib import Path
# Create your views here.
import os
BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)

file_path = os.path.join(BASE_DIR, 'cleaned_file.csv')
df = pd.read_csv(file_path)


x = df.iloc[:, :-1]
y = df['output']
model_random = RandomForestClassifier(n_estimators=350)
model_random.fit(x, y)



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
        else:
            print("working")
            greater_than_120 = 0
            less_than_120 = 1
        print('the type is ', type(fasting_blood_sugar))

        rest_ecg = request.POST.get('rest_ecg')

        if int(rest_ecg) == 0:
            normal = 1
            abnormal = 0
            hypernormal = 0
        elif int(rest_ecg) == 1:
            normal = 0
            abnormal = 1
            hypernormal = 0
        else:
            normal = 0
            abnormal = 0
            hypernormal = 1

        agina_ex = request.POST.get('agina_ex')

        if int(agina_ex) == 0:
            agin_no = 1
            agin_yes = 0
        else:
            agin_no=0
            agin_yes=1

        ecg_graph_trend = request.POST.get('graph')

        if int(ecg_graph_trend) == 0:
            upsloping = 1
            flat = 0
            downsloping = 0
        elif int(ecg_graph_trend) == 1:
            upsloping = 0
            flat = 1
            downsloping = 0
        else:
                upsloping = 0
                flat = 0
                downsloping = 1

        fluroscopy = request.POST.get('color')

        if int(fluroscopy) == 0:
            colored_1 = 1
            colored_2 = 0
            colored_3 = 0
        elif int(fluroscopy) == 1:
            colored_1 = 0
            colored_2 = 1
            colored_3 = 0
        else:
            colored_1 = 0
            colored_2 = 0
            colored_3 = 1

        thalassemia = request.POST.get('thall')

        if int(thalassemia) == 0:
            thall_normal = 1
            fixed_deffect = 0
            rev_defect = 0
        elif int(thalassemia) == 1:
            thall_normal = 0
            fixed_deffect = 1
            rev_defect = 0
        else:
            thall_normal = 0
            fixed_deffect = 0
            rev_defect = 1

        agina_level = request.POST.get('agina_level')

        if int(agina_level) == 0:
            typ_agina = 1
            atyp_agina = 0
            non_agn_pain = 0
            asymp = 0
        elif int(agina_level) == 1:
            typ_agina = 0
            atyp_agina = 1
            non_agn_pain = 0
            asymp = 0
        elif int(agina_level) == 2:
            typ_agina = 0
            atyp_agina = 0
            non_agn_pain = 1
            asymp = 0
        else:
            typ_agina = 0
            atyp_agina = 0
            non_agn_pain = 0
            asymp = 1
            print(type(agina_level),'sdsds')


        pass_value = {
            'title': 'results',
            'age': age,
            'gender': gender,
            'restingbloodpressure': restingbloodpressure,
            'cholestrol':cholestrol,
            'maxheartrate': maxheartrate,
            'treadmill_ecg': treadmill_ecg,
            'fasting_blood_sugar': fasting_blood_sugar,
            'rest_ecg': rest_ecg,
            'agina_ex': agina_ex,
            'ecg_graph_trend': ecg_graph_trend,
            'fluroscopy': fluroscopy,
            'thalassemia': thalassemia,
            'agina_level': agina_level
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

        return render(request, 'result.html', {'pass_value': pass_value.values(), 'attack_result': final_result[0]})
    else:
        return render(request, 'index.html')


def results_page(request):
    if request.method == 'POST':
        return render(request, 'index.html')
    else:
        return render(request, 'result.html')
