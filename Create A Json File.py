#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


DataSet={
    "intents": [
        {
            "tag": [
                "greetings"
            ],
            "code": [
                "Hi",
                "How are you",
                "Is anyone Present",
                "Good Day",
                "Whats up",
                "How do You Do",
                "Hey",
                "Hello",
                "Greetings"
            ],
            "response": [
                "Hello Human",
                "Good To See You Again",
                "Hey, How Can I Help You",
                "Welcome HomoSapien"
            ],
            "context": ""
        },
        {
            "tag": [
                "bye"
            ],
            "code": [
                "Goodbye",
                "See you Again",
                "Ciao",
                "Hasta La Vista",
                "Au Revior",
                "I am Leaving",
                "Thanks For The Help",
                "Have A Good Day",
                "Take Care",
                "Thanks"
            ],
            "response": [
                "Thanks For The Talk",
                "Hopefully Wont see you soon",
                "Talk to You Later",
                "GoodBye",
                "BayMin - The MediBot At Your Service, Anytime Anyplace Anywhere"
            ],
            "context": ""
        },
        {
            "tag": [
                "creator"
            ],
            "code": [
                "Who made you?",
                "Who is Your Father?",
                "Who is your Creator?",
                "Creator",
                "Father"
            ],
            "response": [
                "I was Created My Mathew Jose(MJ)"
            ],
            "context": ""
        },
        {
            "tag": [
                "age"
            ],
            "code": [
                "whats Your Age?",
                "How Old Are You?",
                "How Old?",
                "Age?"
            ],
            "response": [
                "That's A Little Personal Don't You Think :D"
            ],
            "context": ""
        },
        {
            "tag": [
                "functions"
            ],
            "code": [
                "What can You do?",
                "What is Your Functionalities?",
                "functions",
                "abilities",
                "Uses",
                "Tell Me What you do"
            ],
            "response": [
                "I am A Medical Bot Which Listens To Your Symptoms  Tells You WIth Disease With You Show Higest Probablity Of Being Affected By."
            ],
            "context": ""
        },
        {
            "tag": [
                "disease1"
            ],
            "code": [
                "nasal congestion itchy  watery eyes sneezing runny nose sore throat ",
                "nasal congestion, itchy  watery eyes, sneezing,  nose, scratchy throat, throat clearing cough from postnasal drip"
            ],
            "response": [
                "You Are Showing Symptoms Of The Allergies"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease2"
            ],
            "code": [
                "Feel tired fainting Weakness Fatigue easily Have decreased energy Appear pale Develop palpitations rapid heart rate Experience shortness of breath"
            ],
            "response": [
                "You Are Showing Symptoms Of The Anemia"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease3"
            ],
            "code": [
                "Headaches, body aches, fever symptoms Nasal congestion, runny nosesneezing Cough Sore throat"
            ],
            "response": [
                "You Are Showing Symptoms Of The Cold/Flu"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease4"
            ],
            "code": [
                "shortness of breath, chest pain, cough"
            ],
            "response": [
                "You Are Showing Symptoms Of The Asthma"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease5"
            ],
            "code": [
                "loss of orientation agitation, irritability, quarrelsomeness"
            ],
            "response": [
                "You Are Showing Symptoms Of alzheimers"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease6"
            ],
            "code": [
                "absence of menstrual periods breast swelling  tenderness. Food cravings"
            ],
            "response": [
                "You Are Showing Symptoms Of pregnancy"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease7"
            ],
            "code": [
                "a rapid heart rate, excessive sweating, intolerance to heat, tremor, nervousness,  agitation fatigue, weight loss, hair loss"
            ],
            "response": [
                "You Are Showing Symptoms Of hyperthyroid"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease8"
            ],
            "code": [
                "fatigue, depression, mild weight gain, cold intolerance, sleepiness, dry skin,  muscle cramps"
            ],
            "response": [
                "You Are Showing Symptoms Of hypothyroid"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease9"
            ],
            "code": [
                "dehydration, hunger, increased urination,  increased thirst"
            ],
            "response": [
                "You Are Showing Symptoms Of diabetes"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease10"
            ],
            "code": [
                "fever, swollen lymph nodes, joint  muscle aches,  sore throat. chills, night sweats mouth ulcers"
            ],
            "response": [
                "You Are Showing Symptoms Of HIV AIDS"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease11"
            ],
            "code": [
                "dizziness, shortness of breath, headache,  blurred vision nosebleeds, blood in the urine, fatigue, chest pain,"
            ],
            "response": [
                "You Are Showing Symptoms Of high blood pressure"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease12"
            ],
            "code": [
                "aches stiffness, muscle ache fever, fatigue, lack of appetite, loss of energy"
            ],
            "response": [
                "You Are Showing Symptoms Of Rheumatoid Arthritis"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease13"
            ],
            "code": [
                "fatigue, loss of appetite, nausea, jaundice pain in the upper right abdomen inflamed liver"
            ],
            "response": [
                "You Are Showing Symptoms Of hepatitis B"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease14"
            ],
            "code": [
                "headache, fever, exhaustion severe muscle joint pain rash, fever,headache"
            ],
            "response": [
                "You Are Showing Symptoms Of Dengue"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease15"
            ],
            "code": [
                "fever  chills, headaches, nausea  vomiting general weakness  body aches"
            ],
            "response": [
                "You Are Showing Symptoms Of Malaria"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease16"
            ],
            "code": [
                "general weakness, fever red spots on the body fever"
            ],
            "response": [
                "You Are Showing Symptoms Of Chicken Pox"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease17"
            ],
            "code": [
                "Yellow discoloration of the skin, mucous membranes sleepiness Changes in muscle tone High-pitched crying Seizures"
            ],
            "response": [
                "You Are Showing Symptoms Of jaundice"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease18"
            ],
            "code": [
                "bowel movements are frequent watery. no signs of inflammation. cramping abdominal pain"
            ],
            "response": [
                "You Are Showing Symptoms Of Diarrhea"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease19"
            ],
            "code": [
                "decrease in clarity of vision, not fully correctable with glasses"
            ],
            "response": [
                "You Are Showing Symptoms Of cataract"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease20"
            ],
            "code": [
                "fever, chills, cough, shortness of breath,  fatigue."
            ],
            "response": [
                "You Are Showing Symptoms Of pneumonia"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease21"
            ],
            "code": [
                "inability to urinate painful discomfort in the lower abdomen bloating of the lower abdomen"
            ],
            "response": [
                "You Are Showing Symptoms Of Urinary Retention"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease22"
            ],
            "code": [
                "lack of sleep Daytime sleepiness  fatigue Mood changes Po concentration  attention Anxiety Headaches Lack of energy"
            ],
            "response": [
                "You Are Showing Symptoms Of Insomnia"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease23"
            ],
            "code": [
                "sinus headache, facial tenderness, pressure  pain in the sinuses, in the ears  teeth, fever, cloudy discolored nasal sore throat, cough"
            ],
            "response": [
                "You Are Showing Symptoms Of Sinus Infection"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease24"
            ],
            "code": [
                "fatigue, loss of appetite, muscle aches fever"
            ],
            "response": [
                "You Are Showing Symptoms Of hepatitis c"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease25"
            ],
            "code": [
                "swollen, painful salivary glands, fever, headache, fatigue  appetite loss"
            ],
            "response": [
                "You Are Showing Symptoms Of mumps"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease26"
            ],
            "code": [
                "dry cough, conjunctivitis, runny nose high fever."
            ],
            "response": [
                "You Are Showing Symptoms Of measles"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease27"
            ],
            "code": [
                "double vision, blurred vision, drooping eyelids difficulty swallowing, dry mouth, muscle weakness"
            ],
            "response": [
                "You Are Showing Symptoms Of botulism"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease28"
            ],
            "code": [
                "rapid mental deterioration"
            ],
            "response": [
                "You Are Showing Symptoms Of mad cow disease"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease29"
            ],
            "code": [
                "sudden fever, headache, vomiting stiff neck  back, confusion, drowsiness, irritability, loss of consciousness, po responsiveness, seizures, muscle weakness,memory loss."
            ],
            "response": [
                "You Are Showing Symptoms Of meningetis"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease30"
            ],
            "code": [
                "upper abdominal pain nausea, vomiting, abdominal distention"
            ],
            "response": [
                "You Are Showing Symptoms Of indigestion"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease31"
            ],
            "code": [
                "Less bowel movements Lower abdominal discomfort Anal bleeding fissures diarrhea rectal prolapse"
            ],
            "response": [
                "You Are Showing Symptoms Of constipation"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease32"
            ],
            "code": [
                "abdominal pain, loss of appetite, nausea vomiting, fever, abdominal tenderness."
            ],
            "response": [
                "You Are Showing Symptoms Of appendicitis"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease33"
            ],
            "code": [
                "restlessness fatigue; trouble concentrating, that may also appear as memory  attention problems irritabilityheadaches; sleep problems"
            ],
            "response": [
                "You Are Showing Symptoms Of Anxiety Disorder"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease34"
            ],
            "code": [
                "Abdominal pain Diarrhea Vomiting Fever Bloody diarrhea Weight loss"
            ],
            "response": [
                "You Are Showing Symptoms Of crohn's disease"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease35"
            ],
            "code": [
                "Excessive daytime sleepiness hallucinations Sleep paralysis double vision,  droopy eyelids"
            ],
            "response": [
                "You Are Showing Symptoms Of narcolepsy"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease36"
            ],
            "code": [
                "blood in the urine pain kidney painstones in the urinary tractU rinary tract infections"
            ],
            "response": [
                "You Are Showing Symptoms Of cystinuria"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease37"
            ],
            "code": [
                "urinating Blood Groin pain rectal pain abdominal pain low back pain Fever"
            ],
            "response": [
                "You Are Showing Symptoms Of prostatitis"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease38"
            ],
            "code": [
                "chest pressure that goes to the arm shortness of breath sweating pain heaviness tightness ache fullness"
            ],
            "response": [
                "You Are Showing Symptoms Of Angina"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease39"
            ],
            "code": [
                "fever, headache, body aches, skin rash stiff neck, sleepiness, disorientation, coma, tremors, convulsions,  paralysis"
            ],
            "response": [
                "You Are Showing Symptoms Of west nile virus"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease40"
            ],
            "code": [
                "red swollen pus high fevers, chills,  low blood pressure."
            ],
            "response": [
                "You Are Showing Symptoms Of Staph Infection"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease41"
            ],
            "code": [
                "blurred vision"
            ],
            "response": [
                "You Are Showing Symptoms Of Macular Degeneration(Age-Related Type)"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease42"
            ],
            "code": [
                "Flashing lights  floaters"
            ],
            "response": [
                "You Are Showing Symptoms Of Retinal detachment"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease43"
            ],
            "code": [
                "blurriness haziness of vision"
            ],
            "response": [
                "You Are Showing Symptoms Of Glaucoma"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease44"
            ],
            "code": [
                "heavy periods pelvic pain prolapse of the uterus. cancer of the womb, ovaries  cervix"
            ],
            "response": [
                "You Are Showing Symptoms Of hysterectomy"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease45"
            ],
            "code": [
                "a vaginal discharge that is typically thick, odorless"
            ],
            "response": [
                "You Are Showing Symptoms Of yeast infection"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease46"
            ],
            "code": [
                "underweight, worsen depression social withdrawal. irritable  easily upset Sleep disrupted"
            ],
            "response": [
                "You Are Showing Symptoms Of anorexia"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease47"
            ],
            "code": [
                "cough, chest discomfort, shortness of breath,  wheezing."
            ],
            "response": [
                "You Are Showing Symptoms Of chronic obstructive pulmonary disease"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease48"
            ],
            "code": [
                "shortness of breath  wheezing"
            ],
            "response": [
                "You Are Showing Symptoms Of emphysema"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease49"
            ],
            "code": [
                "tiny areas of infection area of skin from which hair grows"
            ],
            "response": [
                "You Are Showing Symptoms Of boils"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease50"
            ],
            "code": [
                "raised  look shiny  dome-shaped, ranging in col from pink to red"
            ],
            "response": [
                "You Are Showing Symptoms Of keloid scar"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease51"
            ],
            "code": [
                "acial flushing, blushing, skin redness small cysts,  thickening of the facial tissue"
            ],
            "response": [
                "You Are Showing Symptoms Of rosacea"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease52"
            ],
            "code": [
                "one-sided stabbing pain, tingling, itching, burning,  stinging sensation rash headache, fever  chills, nausea, body aches,  fluid-filled blistering red rash"
            ],
            "response": [
                "You Are Showing Symptoms Of shingles(herpes zoster)"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease53"
            ],
            "code": [
                "Reddish, scaly plaques head forehead"
            ],
            "response": [
                "You Are Showing Symptoms Of dandruff"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease54"
            ],
            "code": [
                "uninflamed blackheads t, pus-filled pimples "
            ],
            "response": [
                "You Are Showing Symptoms Of acne"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease55"
            ],
            "code": [
                "fleshy, painless growth on the skin"
            ],
            "response": [
                "You Are Showing Symptoms Of common wart"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease56"
            ],
            "code": [
                "redness, swelling, tenderness, itching pain skin tightness  hardening"
            ],
            "response": [
                "You Are Showing Symptoms Of Scleroderma"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease57"
            ],
            "code": [
                "itching sever mild bumps big angular borders  a violet colour"
            ],
            "response": [
                "You Are Showing Symptoms Of Lichen planus"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease58"
            ],
            "code": [
                "simple forgetfulness old age"
            ],
            "response": [
                "You Are Showing Symptoms Of Dementia"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease59"
            ],
            "code": [
                "welts flare itch, swell"
            ],
            "response": [
                "You Are Showing Symptoms Of hives"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease60"
            ],
            "code": [
                "sore throat, discolored, deteriorating teeth, abdominal pain vomiting swollen salivary glands constipation, dehydration, dry skin"
            ],
            "response": [
                "You Are Showing Symptoms Of bulimia nervosa"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease61"
            ],
            "code": [
                "Penile erection occurs penis hard enough f completion of sex"
            ],
            "response": [
                "You Are Showing Symptoms Of erectile dysfunction"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease62"
            ],
            "code": [
                "slow flow of urine need to urinate urgently urinary tract infections, blockage of the urethra"
            ],
            "response": [
                "You Are Showing Symptoms Of Enlarged Prostate Gland"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease63"
            ],
            "code": [
                "Loss of appetite  excessive hunger Insomnia Fatigue  other physical symptomsinadequacy Lack of concentration  making decisions Hopelessness"
            ],
            "response": [
                "You Are Showing Symptoms Of Dysthymia (Persistent Depressive Disorder)"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease64"
            ],
            "code": [
                "racing  pounding heartbeat chest pains; stomach upset; dizziness, lightheadedness, nausea; hyperventilation; difficulty breathing"
            ],
            "response": [
                "You Are Showing Symptoms Of panic attack"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease65"
            ],
            "code": [
                "elevated, expansive irritable mood; racing thoughts; pressured speech decreased need f sleep"
            ],
            "response": [
                "You Are Showing Symptoms Of bipolar disorder"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease66"
            ],
            "code": [
                "upper abdominal pain  discomfort belching, abdominal distention swelling lower chest pain."
            ],
            "response": [
                "You Are Showing Symptoms Of Indigestion(Dyspepsia)"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease67"
            ],
            "code": [
                "dizziness pale skin increased saliva production along with headache fatigue,Nausea ,vomiting"
            ],
            "response": [
                "You Are Showing Symptoms Of motion sickness"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease68"
            ],
            "code": [
                "fatigue  drowsiness becoming tired easily confusion shortness of breath sleepiness headache"
            ],
            "response": [
                "You Are Showing Symptoms Of respiratory acidosis"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease69"
            ],
            "code": [
                "rapid  shallow breathing confusion fatigue headache sleepiness lack of appetite jaundice"
            ],
            "response": [
                "You Are Showing Symptoms Of metabolic acidosis"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease70"
            ],
            "code": [
                "labored  rapid breathing muscle fatigue  general weakness low blood pressure discolored skin fever headaches"
            ],
            "response": [
                "You Are Showing Symptoms Of acute respiratory distress syndrome"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease71"
            ],
            "code": [
                "weakness in the muscles fatigue tiredness darkening in skin col weight loss decreased appetite low blood sugar levels nausea vomiting irritability  depression"
            ],
            "response": [
                "You Are Showing Symptoms Of Addison's disease"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease72"
            ],
            "code": [
                "confusion, fear restlessness high fever sudden pain in the lower back, belly,  legs"
            ],
            "response": [
                "You Are Showing Symptoms Of Addisonian crisis"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease73"
            ],
            "code": [
                "shortness of breath during physical activity waking up short of breath rapid heart rate swollen lower legs"
            ],
            "response": [
                "You Are Showing Symptoms Of beriberi"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease74"
            ],
            "code": [
                "decreased muscle function, particularly in the lower legs loss of feeling in the feet  hands pain"
            ],
            "response": [
                "You Are Showing Symptoms Of dry beriberi"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease75"
            ],
            "code": [
                "confusion memory loss rapid eye movement  double vision"
            ],
            "response": [
                "You Are Showing Symptoms Of thalamus  hypothalamus"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease76"
            ],
            "code": [
                "cough diarrhea respiratory difficulties fever headache muscle aches malaise runny nose sore throat"
            ],
            "response": [
                "You Are Showing Symptoms Of Bird Flu"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease77"
            ],
            "code": [
                "pain  swelling in the affected bones fatigued easily broken bones weight loss"
            ],
            "response": [
                "You Are Showing Symptoms Of bone cancer"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease78"
            ],
            "code": [
                "dull ache in the affected bone weakened bone, leading to severe pain"
            ],
            "response": [
                "You Are Showing Symptoms Of bone tumour"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease79"
            ],
            "code": [
                "shortness of breath wheezing bluish appearance of the skinfatigue ribs fast breathing cough"
            ],
            "response": [
                "You Are Showing Symptoms Of bronchiolitis"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease80"
            ],
            "code": [
                "Ringing in Ears"
            ],
            "response": [
                "You Are Showing Symptoms Of tinnitus"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease81"
            ],
            "code": [
                "a very sore throat difficulty swallowing stomachaches headaches a stiff neck jaw tonsils that have white  yellow spots"
            ],
            "response": [
                "You Are Showing Symptoms Of tonsillitis"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease82"
            ],
            "code": [
                "a skin ulcer swollen lymph nodes near the skin ulcer headaches a fever chills fatigue"
            ],
            "response": [
                "You Are Showing Symptoms Of Tularemia"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease83"
            ],
            "code": [
                "unexplained fatigue fever night sweats appetite loss weight loss"
            ],
            "response": [
                "You Are Showing Symptoms Of tuberculosis"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease84"
            ],
            "code": [
                "severe headache high fever rash back  chest low blood pressure eye sensitivity severe muscle pain"
            ],
            "response": [
                "You Are Showing Symptoms Of typhus"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease85"
            ],
            "code": [
                "loss of appetite weight loss abdominal stomach lower back pain blood clots depression"
            ],
            "response": [
                "You Are Showing Symptoms Of Pancreatic Cancer"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease86"
            ],
            "code": [
                "bone fractures kidney stones depression, lethargy,  confusion nausea vomiting pain in your muscles"
            ],
            "response": [
                "You Are Showing Symptoms Of hyperparathyroidism"
            ],
            "context": ""
        },
        {
            "tag": [
                "disease87"
            ],
            "code": [
                "redness of the skin pus-filled blisters changes in nail shape, color,  texture detachment of your nail"
            ],
            "response": [
                "You Are Showing Symptoms Of paronychia"
            ],
            "context": ""
        }
    ]
}


# In[5]:


with open(r'C:\Users\mjose\Desktop\PROJECTS\MEDBOT\Medbot_DataSet.json', 'w',encoding='UTF-8') as json_file:
    json.dump(DataSet, json_file, ensure_ascii=False, indent=4)


# In[ ]:




