question_test={
    "Q1_":{
        "Question":"Capital of Pakistan?",
         
        "options":"a)Islamabad b) Karachi c) Peshawar", 
        "answer":"a"
    }, 
    "Q2_":{
        "Question":"what is your age?", 
        "options":"a) 19 b) 20 c) 30",
        "answer":"a"
    }, 
    "Q3_":{
        "Question":"biggest city of Pakistan?", 
        "options":"a)Islamabad b) Karachi c) Peshawar",
        "answer":"b"
    },
    "Q4_":{
        "Question":"2+2=?", 
        "options":"a) 3 b) 0.4c) 4",
        "answer":"c"
    }, 
    "Q5_":{
        "Question":"what is your dream country name?", 
        "options":"a)china b) Norway c) Japan",
        "answer":"c"   
    }
}
score=0
n=[]
for q in question_test:
    print(question_test[q]["Question"])
  
    print(question_test[q]["options"])
    choice=input("\nchoice any option. "). lower()
    if choice==question_test[q]["answer"]:
       score+=1
       n. append(1)
    else:
        print(f"you wrong❌,\"{question_test[q].get("answer")}\"is correct")
        pass
print("you correctly answered:",len(n))        
print(f"\nyou secure:{score}")