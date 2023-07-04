import os,time
os.system('cls')
print()
print()
print('       Please wait.. ')
time.sleep(3)
os.system('cls')
print()
print()
print('-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=')
print('-- -- -- -- -- -- -- -- -- -- - IIITD - Online Test - -- -- -- -- -- -- -- -- --')
print('=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-')
print()
print('       Rules of the test:')
print()
print('       (*) Each topic has a maximum of 10 questions.')
print()
print('       (*) Maximum marks : +40')
print()
print('       (*) Minimum marks : -10')
print()
print('                                        Marks:')
print()
print('       (a) For each correct answer    : +4')
print()
print('       (b) For each incorrect answer  : -1')
print()
print('       (c) For all other cases        : zero')
print()
print('==============================================================================')
print()
test=input('   Are you ready to take the test ? : ')
print()
print('==============================================================================')
print()
os.system('cls')
print()
print()
print('       Please wait.. ')
time.sleep(3)
os.system('cls')
if test in ('yes','Yes','Y','y'):
    print()
    print()
    print()
    name=input('   Enter your name : ')
    os.system('cls')
    print()
    print()
    print('       Please wait.. ')
    while True:
        time.sleep(3)
        os.system('cls')
        print()
        print()
        print('==============================================================================')
        print()
        print('       Well, ',name,', please choose your favourite topic :',sep='')
        print()
        print('       (1.) Language')
        print()
        print('       (2.) Science')
        print()
        print('       (3.) General Knowledge')
        print()
        print('       (4.) Mental ability')
        print()
        print('       (5.) Exit')
        print()
        topic=input('       Choose your option : ')
        print()
        print('==============================================================================')
        print()
        os.system('cls')
        print()
        print()
        print('       Please wait.. ')
        time.sleep(3)
        os.system('cls')
        print()
        print()

    #break---------------------------------------------------------------------------------------------------------------

        if topic in ('(1.)','(1)','1.','1'):
            score=0
            print('       Welcome ',name,'. All the best !!',sep='')
            print()
            print('------------------------------')
            print('               |')
            print('       Topic 1 - Language Test')
            print('               |')
            print('------------------------------')
            print()
            print()

        #1st_question_answer_C

            print('       Q1. They have put speed bumps on the road to ______ accidents.')
            print()
            print('           (a) avoid')
            print()
            print('           (b) prohibit')
            print()
            print('           (c) prevent')
            print()
            print('           (d) forbid')
            print()
            a1=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a1 in ('(A)','(a)','A','a'):
                score-=1
                result1="Incorrect"
            elif a1 in ('(B)','(b)','B','b'):
                score-=1
                result1="Incorrect"
            elif a1 in ('(C)','(c)','C','c'):
                score+=4
                result1="Correct"
            elif a1 in ('(D)','(d)','D','d'):
                score-=1
                result1="Incorrect"
            else:
                score+=0
                result1="Incorrect"

        #2nd_question_answer_B

            print('       Q2. She ______ me to go to school.')
            print()
            print('           (a) said')
            print()
            print('           (b) told')
            print()
            print('           (c) made')
            print()
            print('           (d) suggested')
            print()
            a2=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a2 in ('(A)','(a)','A','a'):
                score-=1
                result2="Incorrect"
            elif a2 in ('(B)','(b)','B','b'):
                score+=4
                result2="Correct"
            elif a2 in ('(C)','(c)','C','c'):
                score-=1
                result2="Incorrect"
            elif a2 in ('(D)','(d)','D','d'):
                score-=1
                result2="Incorrect"
            else:
                score+=0
                result2="Incorrect"

        #3rd_question_answer_C

            print('       Q3. You aren\'t allowed to use your mobile so ______.')
            print()
            print('           (a) it\'s no point to leave it on')
            print()
            print('           (b) it\'s no point in leaving it on')
            print()
            print('           (c) there\'s no point in leaving it on')
            print()
            print('           (d) there\'s no point to leave it on')
            print()
            a3=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a3 in ('(A)','(a)','A','a'):
                score-=1
                result3="Incorrect"
            elif a3 in ('(B)','(b)','B','b'):
                score-=1
                result3="Incorrect"
            elif a3 in ('(C)','(c)','C','c'):
                score+=4
                result3="Correct"
            elif a3 in ('(D)','(d)','D','d'):
                score-=1
                result3="Incorrect"
            else:
                score+=0
                result3="Incorrect"

        #4th_question_answer_A

            print('       Q4. Have you visited London?" "______."')
            print()
            print('           (a) Not yet')
            print()
            print('           (b) Ever')
            print()
            print('           (c) Already')
            print()
            print('           (d) Not')
            print()
            a4=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a4 in ('(A)','(a)','A','a'):
                score+=4
                result4="Correct"
            elif a4 in ('(B)','(b)','B','b'):
                score-=1
                result4="Incorrect"
            elif a4 in ('(C)','(c)','C','c'):
                score-=1
                result4="Incorrect"
            elif a4 in ('(D)','(d)','D','d'):
                score-=1
                result4="Incorrect"
            else:
                score+=0
                result4="Incorrect"

        #5th_question_answer_D

            print('       Q5. I ______ a reply to my letter in the next few days.')
            print()
            print('           (a) hope')
            print()
            print('           (b) wait for')
            print()
            print('           (c) get')
            print()
            print('           (d) expect')
            print()
            a5=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a5 in ('(A)','(a)','A','a'):
                score-=1
                result5="Incorrect"
            elif a5 in ('(B)','(b)','B','b'):
                score-=1
                result5="Incorrect"
            elif a5 in ('(C)','(c)','C','c'):
                score-=1
                result5="Incorrect"
            elif a5 in ('(D)','(d)','D','d'):
                score+=4
                result5="Correct"
            else:
                score+=0
                result5="Incorrect"

        #6th_question_answer_C

            print('       Q6. It ______ my brother.')
            print()
            print('           (a) is ages that I didn\'t see')
            print()
            print('           (b) was ages since I saw')
            print()
            print('           (c) is ages since I saw')
            print()
            print('           (d) was ages that I haven\'t seen')
            print()
            a6=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a6 in ('(A)','(a)','A','a'):
                score-=1
                result6="Incorrect"
            elif a6 in ('(B)','(b)','B','b'):
                score-=1
                result6="Incorrect"
            elif a6 in ('(C)','(c)','C','c'):
                score+=4
                result6="Correct"
            elif a6 in ('(D)','(d)','D','d'):
                score-=1
                result6="Incorrect"
            else:
                score+=0
                result6="Incorrect"

        #7th_question_answer_B

            print('       Q7. The doctor gave me a ______ for some medicine yesterday.')
            print()
            print('           (a) note')
            print()
            print('           (b) prescription')
            print()
            print('           (c) receipt')
            print()
            print('           (d) recipe')
            print()
            a7=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a7 in ('(A)','(a)','A','a'):
                score-=1
                result7="Incorrect"
            elif a7 in ('(B)','(b)','B','b'):
                score+=4
                result7="Correct"
            elif a7 in ('(C)','(c)','C','c'):
                score-=1
                result7="Incorrect"
            elif a7 in ('(D)','(d)','D','d'):
                score-=1
                result7="Incorrect"
            else:
                score+=0
                result7="Incorrect"

        #8th_question_answer_A

            print('       Q8. "Did you speak to Juliet?" "No, I\'ve ______ seen her."')
            print()
            print('           (a) hardly')
            print()
            print('           (b) nearly')
            print()
            print('           (c) often')
            print()
            print('           (d) always')
            print()
            a8=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a8 in ('(A)','(a)','A','a'):
                score+=4
                result8="Correct"
            elif a8 in ('(B)','(b)','B','b'):
                score-=1
                result8="Incorrect"
            elif a8 in ('(C)','(c)','C','c'):
                score-=1
                result8="Incorrect"
            elif a8 in ('(D)','(d)','D','d'):
                score-=1
                result8="Incorrect"
            else:
                score+=0
                result8="Incorrect"

        #9th_question_answer_D

            print('       Q9. I\'m fed up ______ this excersice.')
            print()
            print('           (a) for doing')
            print()
            print('           (b) to do')
            print()
            print('           (c) to doing')
            print()
            print('           (d) with doing')
            print()
            a9=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a9 in ('(A)','(a)','A','a'):
                score-=1
                result9="Incorrect"
            elif a9 in ('(B)','(b)','B','b'):
                score-=1
                result9="Incorrect"
            elif a9 in ('(C)','(c)','C','c'):
                score-=1
                result9="Incorrect"
            elif a9 in ('(D)','(d)','D','d'):
                score+=4
                result9="Correct"
            else:
                score+=0
                result9="Incorrect"

        #10th_question_answer_D

            print('      Q10. How long ______ English?')
            print()
            print('           (a) do you learn')
            print()
            print('           (b) are you learning')
            print()
            print('           (c) you learn')
            print()
            print('           (d) have you been learning')
            print()
            a10=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a10 in ('(A)','(a)','A','a'):
                score-=1
                result10="Incorrect"
            elif a10 in ('(B)','(b)','B','b'):
                score-=1
                result10="Incorrect"
            elif a10 in ('(C)','(c)','C','c'):
                score-=1
                result10="Incorrect"
            elif a10 in ('(D)','(d)','D','d'):
                score+=4
                result10="Correct"
            else:
                score+=0
                result10="Incorrect"

            #--------------------------------------------------------------------------------------

            os.system('cls')
            print()
            print()
            print('       Please wait.. ')
            time.sleep(3)
            os.system('cls')
            print()
            print()
            print()

        #end_of_question

            print('           --------------------- Test analysis -----------------------')
            print()
            print('                 Your answer \t Correct answer \t Status')
            print()
            print('           -----------------------------------------------------------')
            print()
            print('           Q1.  ',a1,'\t\t (C) \t\t\t',result1)
            print()
            print('           Q2.  ',a2,'\t\t (B) \t\t\t',result2)
            print()
            print('           Q3.  ',a3,'\t\t (C) \t\t\t',result3)
            print()
            print('           Q4.  ',a4,'\t\t (A) \t\t\t',result4)
            print()
            print('           Q5.  ',a5,'\t\t (D) \t\t\t',result5)
            print()
            print('           Q6.  ',a6,'\t\t (C) \t\t\t',result6)
            print()
            print('           Q7.  ',a7,'\t\t (B) \t\t\t',result7)
            print()
            print('           Q8.  ',a8,'\t\t (A) \t\t\t',result8)
            print()
            print('           Q9.  ',a9,'\t\t (D) \t\t\t',result9)
            print()
            print('          Q10.  ',a10,'\t\t (D) \t\t\t',result10)
            print()
            print('           -----------------------------------------------------------')
            print()
            print('           Total marks obtained :',score,'out of 40')
            print()
            pert=(score*100)/40
            print('           Total percentage :',pert,'%')
            print()
            if pert>90:
                grade='A1'
                msg='Congratulations !!'
                ext=''
            elif pert>80:
                grade='A2'
                msg='Congratulations !!'
                ext=''
            elif pert>70:
                grade='B1'
                msg='Good !!'
                ext=''
            elif pert>60:
                grade='B2'
                msg='Good !!'
                ext=''
            elif pert>40:
                grade='C'
                msg='Sorry !!'
                ext='Better luck next time !!'
            elif pert>20:
                grade='D'
                msg='Sorry !!'
                ext='Better luck next time !!'
            elif pert>0:
                grade='E'
                msg='Sorry !!'
                ext='Better luck next time !!'
            elif pert<0:
                grade='F'
                msg='Sorry !!'
                ext='Better luck next time !!'
            print('          ',msg,grade,'is awarded.',ext)

    #break---------------------------------------------------------------------------------------------------------------

        elif topic in ('(2.)','(2)','2.','2'):
            score=0
            print('       Welcome ',name,'. All the best !!',sep='')
            print()
            print('-----------------------------')
            print('               |')
            print('       Topic 2 - Science Test')
            print('               |')
            print('-----------------------------')
            print()
            print()

        #1st_question_answer_A

            print('       Q1. The chemical name of marble is:')
            print()
            print('           (a) Calcium carbonate')
            print()
            print('           (b) Calcium sulphate')
            print()
            print('           (c) Calcium chloride')
            print()
            print('           (d) Magnesium carbonate')
            print()
            a1=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a1 in ('(A)','(a)','A','a'):
                score+=4
                result1="Correct"
            elif a1 in ('(B)','(b)','B','b'):
                score-=1
                result1="Incorrect"
            elif a1 in ('(C)','(c)','C','c'):
                score-=1
                result1="Incorrect"
            elif a1 in ('(D)','(d)','D','d'):
                score-=1
                result1="Incorrect"
            else:
                score+=0
                result1="Incorrect"

        #2nd_question_answer_C

            print('       Q2. Which of these chemical elements is heavier than iron?')
            print()
            print('           (a) potassium')
            print()
            print('           (b) carbon')
            print()
            print('           (c) gold')
            print()
            print('           (d) manganese')
            print()
            a2=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a2 in ('(A)','(a)','A','a'):
                score-=1
                result2="Incorrect"
            elif a2 in ('(B)','(b)','B','b'):
                score-=1
                result2="Incorrect"
            elif a2 in ('(C)','(c)','C','c'):
                score+=4
                result2="Correct"
            elif a2 in ('(D)','(d)','D','d'):
                score-=1
                result2="Incorrect"
            else:
                score+=0
                result2="Incorrect"

        #3rd_question_answer_D

            print('       Q3. While catching a ball, a player pulls down his hands to lower the:')
            print()
            print('           (a) impulse')
            print()
            print('           (b) force')
            print()
            print('           (c) catching time')
            print()
            print('           (d) momentum')
            print()
            a3=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a3 in ('(A)','(a)','A','a'):
                score-=1
                result3="Incorrect"
            elif a3 in ('(B)','(b)','B','b'):
                score-=1
                result3="Incorrect"
            elif a3 in ('(C)','(c)','C','c'):
                score-=1
                result3="Incorrect"
            elif a3 in ('(D)','(d)','D','d'):
                score+=4
                result3="Correct"
            else:
                score+=0
                result3="Incorrect"

        #4th_question_answer_D

            print('       Q4. Clothes keep us warm in winter because they:')
            print()
            print('           (a) supply heat')
            print()
            print('           (b) do not radiate heat')
            print()
            print('           (c) prevent air from contacting the body')
            print()
            print('           (d) prevent the heat of the body from escaping')
            print()
            a4=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a4 in ('(A)','(a)','A','a'):
                score-=1
                result4="Incorrect"
            elif a4 in ('(B)','(b)','B','b'):
                score-=1
                result4="Incorrect"
            elif a4 in ('(C)','(c)','C','c'):
                score-=1
                result4="Incorrect"
            elif a4 in ('(D)','(d)','D','d'):
                score+=4
                result4="Correct"
            else:
                score+=0
                result4="Incorrect"

        #5th_question_answer_B

            print('       Q5. The sky appears blue because of:')
            print()
            print('           (a) Atmospheric water vapour.')
            print()
            print('           (b) Scattering of light.')
            print()
            print('           (c) Reflection on sea water.')
            print()
            print('           (d) Emission of blue wavelength by the sun.')
            print()
            a5=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a5 in ('(A)','(a)','A','a'):
                score-=1
                result5="Incorrect"
            elif a5 in ('(B)','(b)','B','b'):
                score+=4
                result5="Correct"
            elif a5 in ('(C)','(c)','C','c'):
                score-=1
                result5="Incorrect"
            elif a5 in ('(D)','(d)','D','d'):
                score-=1
                result5="Incorrect"
            else:
                score+=0
                result5="Incorrect"

        #6th_question_answer_A

            print('       Q6. The instrument that measures and records the relative humidity')
            print('           of air is:')
            print()
            print('           (a) Hygrometer')
            print()
            print('           (b) Barometer')
            print()
            print('           (c) Hydrometer')
            print()
            print('           (d) Lactomter')
            print()
            a6=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a6 in ('(A)','(a)','A','a'):
                score+=4
                result6="Correct"
            elif a6 in ('(B)','(b)','B','b'):
                score-=1
                result6="Incorrect"
            elif a6 in ('(C)','(c)','C','c'):
                score-=1
                result6="Incorrect"
            elif a6 in ('(D)','(d)','D','d'):
                score-=1
                result6="Incorrect"
            else:
                score+=0
                result6="Incorrect"

        #7th_question_answer_C
            print('       Q7. If the length of a simple pendulum is halved then its period')
            print('           of oscillation is:')
            print()
            print('           (a) halved')
            print()
            print('           (b) doubled')
            print()
            print('           (c) decreased by a factor')
            print()
            print('           (d) increased by a factor')
            print()
            a7=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a7 in ('(A)','(a)','A','a'):
                score-=1
                result7="Incorrect"
            elif a7 in ('(B)','(b)','B','b'):
                score-=1
                result7="Incorrect"
            elif a7 in ('(C)','(c)','C','c'):
                score+=4
                result7="Correct"
            elif a7 in ('(D)','(d)','D','d'):
                score-=1
                result7="Incorrect"
            else:
                score+=0
                result7="Incorrect"

        #8th_question_answer_A

            print('       Q8. Geostationary satellite revolves at:')
            print()
            print('           (a) fixed height')
            print()
            print('           (b) any height')
            print()
            print('           (c) height which depends upon its mass')
            print()
            print('           (d) height above pole')
            print()
            a8=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a8 in ('(A)','(a)','A','a'):
                score+=4
                result8="Correct"
            elif a8 in ('(B)','(b)','B','b'):
                score-=1
                result8="Incorrect"
            elif a8 in ('(C)','(c)','C','c'):
                score-=1
                result8="Incorrect"
            elif a8 in ('(D)','(d)','D','d'):
                score-=1
                result8="Incorrect"
            else:
                score+=0
                result8="Incorrect"

        #9th_question_answer_C

            print('       Q9. Woolen clothes keep the body warm because:')
            print()
            print('           (a) Wool absorbs radiant heat from outer objects.')
            print()
            print('           (b) Wool increases the temperature of the body.')
            print()
            print('           (c) Wool is a bad conductor.')
            print()
            print('           (d) Wool rejects heat from the outer objects.')
            print()
            a9=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a9 in ('(A)','(a)','A','a'):
                score-=1
                result9="Incorrect"
            elif a9 in ('(B)','(b)','B','b'):
                score-=1
                result9="Incorrect"
            elif a9 in ('(C)','(c)','C','c'):
                score+=4
                result9="Correct"
            elif a9 in ('(D)','(d)','D','d'):
                score-=1
                result9="Incorrect"
            else:
                score+=0
                result9="Incorrect"

        #10th_question_answer_B

            print('      Q10. The speed of light with the rise in the temperature of the medium:')
            print()
            print('           (a) increases')
            print()
            print('           (b) remains unaltered')
            print()
            print('           (c) decreases')
            print()
            print('           (d) drops suddenly')
            print()
            a10=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a10 in ('(A)','(a)','A','a'):
                score-=1
                result10="Incorrect"
            elif a10 in ('(B)','(b)','B','b'):
                score+=4
                result10="Correct"
            elif a10 in ('(C)','(c)','C','c'):
                score-=1
                result10="Incorrect"
            elif a10 in ('(D)','(d)','D','d'):
                score-=1
                result10="Incorrect"
            else:
                score+=0
                result10="Incorrect"

            #--------------------------------------------------------------------------------------

            os.system('cls')
            print()
            print()
            print('       Please wait.. ')
            time.sleep(3)
            os.system('cls')
            print()
            print()
            print()

        #end_of_question

            print('           --------------------- Test analysis -----------------------')
            print()
            print('                 Your answer \t Correct answer \t Status')
            print()
            print('           -----------------------------------------------------------')
            print()
            print('           Q1.  ',a1,'\t\t (A) \t\t\t',result1)
            print()
            print('           Q2.  ',a2,'\t\t (C) \t\t\t',result2)
            print()
            print('           Q3.  ',a3,'\t\t (D) \t\t\t',result3)
            print()
            print('           Q4.  ',a4,'\t\t (D) \t\t\t',result4)
            print()
            print('           Q5.  ',a5,'\t\t (B) \t\t\t',result5)
            print()
            print('           Q6.  ',a6,'\t\t (A) \t\t\t',result6)
            print()
            print('           Q7.  ',a7,'\t\t (C) \t\t\t',result7)
            print()
            print('           Q8.  ',a8,'\t\t (A) \t\t\t',result8)
            print()
            print('           Q9.  ',a9,'\t\t (C) \t\t\t',result9)
            print()
            print('          Q10.  ',a10,'\t\t (B) \t\t\t',result10)
            print()
            print('           -----------------------------------------------------------')
            print()
            print('           Total marks obtained :',score,'out of 40')
            print()
            pert=(score*100)/40
            print('           Total percentage :',pert,'%')
            print()
            if pert>90:
                grade='A1'
                msg='Congratulations !!'
                ext=''
            elif pert>80:
                grade='A2'
                msg='Congratulations !!'
                ext=''
            elif pert>70:
                grade='B1'
                msg='Good !!'
                ext=''
            elif pert>60:
                grade='B2'
                msg='Good !!'
                ext=''
            elif pert>40:
                grade='C'
                msg='Sorry !!'
                ext='Better luck next time !!'
            elif pert>20:
                grade='D'
                msg='Sorry !!'
                ext='Better luck next time !!'
            elif pert>0:
                grade='E'
                msg='Sorry !!'
                ext='Better luck next time !!'
            elif pert<0:
                grade='F'
                msg='Sorry !!'
                ext='Better luck next time !!'
            print('          ',msg,grade,'is awarded.',ext)

    #break---------------------------------------------------------------------------------------------------------------

        elif topic in ('(3.)','(3)','3.','3'):
            score=0
            print('       Welcome ',name,'. All the best !!',sep='')
            print()
            print('---------------------------------------')
            print('               |')
            print('       Topic 3 - General Knowledge Test')
            print('               |')
            print('---------------------------------------')
            print()
            print()

        #1st_question_answer_A

            print('       Q1. Grand Central Terminal, Park Avenue, New York is the world\'s')
            print()
            print('           (a) largest railway station')
            print()
            print('           (b) highest railway station')
            print()
            print('           (c) longest railway station')
            print()
            print('           (d) None of the above')
            print()
            a1=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a1 in ('(A)','(a)','A','a'):
                score+=4
                result1="Correct"
            elif a1 in ('(B)','(b)','B','b'):
                score-=1
                result1="Incorrect"
            elif a1 in ('(C)','(c)','C','c'):
                score-=1
                result1="Incorrect"
            elif a1 in ('(D)','(d)','D','d'):
                score-=1
                result1="Incorrect"
            else:
                score+=0
                result1="Incorrect"

        #2nd_question_answer_D

            print('       Q2. India\'s first metro railway service in Kolkata was started in')
            print('           the year')
            print()
            print('           (a) 1994')
            print()
            print('           (b) 1990')
            print()
            print('           (c) 1980')
            print()
            print('           (d) 1984')
            print()
            a2=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a2 in ('(A)','(a)','A','a'):
                score-=1
                result2="Incorrect"
            elif a2 in ('(B)','(b)','B','b'):
                score-=1
                result2="Incorrect"
            elif a2 in ('(C)','(c)','C','c'):
                score-=1
                result2="Incorrect"
            elif a2 in ('(D)','(d)','D','d'):
                score+=4
                result2="Correct"
            else:
                score+=0
                result2="Incorrect"

        #3rd_question_answer_A

            print('       Q3. Hitler party which came into power in 1933 is known as')
            print()
            print('           (a) Nazi Party')
            print()
            print('           (b) Ku-Klux-Klan')
            print()
            print('           (c) Democratic Party')
            print()
            print('           (d) Labour Party')
            print()
            a3=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a3 in ('(A)','(a)','A','a'):
                score+=4
                result3="Correct"
            elif a3 in ('(B)','(b)','B','b'):
                score-=1
                result3="Incorrect"
            elif a3 in ('(C)','(c)','C','c'):
                score-=1
                result3="Incorrect"
            elif a3 in ('(D)','(d)','D','d'):
                score-=1
                result3="Incorrect"
            else:
                score+=0
                result3="Incorrect"

        #4th_question_answer_A

            print('       Q4. Mother Teresa received Nobel Peace Prize in the year')
            print()
            print('           (a) 1979')
            print()
            print('           (b) 1980')
            print()
            print('           (c) 1982')
            print()
            print('           (d) 1985')
            print()
            a4=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a4 in ('(A)','(a)','A','a'):
                score+=4
                result4="Correct"
            elif a4 in ('(B)','(b)','B','b'):
                score-=1
                result4="Incorrect"
            elif a4 in ('(C)','(c)','C','c'):
                score-=1
                result4="Incorrect"
            elif a4 in ('(D)','(d)','D','d'):
                score-=1
                result4="Incorrect"
            else:
                score+=0
                result4="Incorrect"


        #5th_question_answer_C

            print('       Q5. In which country Mother Teresa was born')
            print()
            print('           (a) Germany')
            print()
            print('           (b) Hungary')
            print()
            print('           (c) Macedonia')
            print()
            print('           (d) Slovakia')
            print()
            a5=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a5 in ('(A)','(a)','A','a'):
                score-=1
                result5="Incorrect"
            elif a5 in ('(B)','(b)','B','b'):
                score-=1
                result5="Incorrect"
            elif a5 in ('(C)','(c)','C','c'):
                score+=4
                result5="Correct"
            elif a5 in ('(D)','(d)','D','d'):
                score-=1
                result5="Incorrect"
            else:
                score+=0
                result5="Incorrect"

        #6th_question_answer_B

            print('       Q6. Garampani sanctuary is located at')
            print()
            print('           (a) Junagarh, Gujarat')
            print()
            print('           (b) Diphu, Assam')
            print()
            print('           (c) Kohima, Nagaland')
            print()
            print('           (d) Gangtok, Sikkim')
            print()
            a6=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a6 in ('(A)','(a)','A','a'):
                score-=1
                result6="Incorrect"
            elif a6 in ('(B)','(b)','B','b'):
                score+=4
                result6="Correct"
            elif a6 in ('(C)','(c)','C','c'):
                score-=1
                result6="Incorrect"
            elif a6 in ('(D)','(d)','D','d'):
                score-=1
                result6="Incorrect"
            else:
                score+=0
                result6="Incorrect"

        #7th_question_answer_D

            print('       Q7. For which of the following disciplines is Nobel Prize awarded?')
            print()
            print('           (a) Physics and Chemistry')
            print()
            print('           (b) Physiology or Medicine')
            print()
            print('           (c) Literature, Piece and Economics')
            print()
            print('           (d) All of the above')
            print()
            a7=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a7 in ('(A)','(a)','A','a'):
                score-=1
                result7="Incorrect"
            elif a7 in ('(B)','(b)','B','b'):
                score-=1
                result7="Incorrect"
            elif a7 in ('(C)','(c)','C','c'):
                score-=1
                result7="Incorrect"
            elif a7 in ('(D)','(d)','D','d'):
                score+=4
                result7="Correct"
            else:
                score+=0
                result7="Incorrect"

        #8th_question_answer_C

            print('       Q8. India\'s first all women Post Office is located at')
            print()
            print('           (a) Patna')
            print()
            print('           (b) Mumbai')
            print()
            print('           (c) Delhi')
            print()
            print('           (d) Chennai')
            print()
            a8=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a8 in ('(A)','(a)','A','a'):
                score-=1
                result8="Incorrect"
            elif a8 in ('(B)','(b)','B','b'):
                score-=1
                result8="Incorrect"
            elif a8 in ('(C)','(c)','C','c'):
                score+=4
                result8="Correct"
            elif a8 in ('(D)','(d)','D','d'):
                score-=1
                result8="Incorrect"
            else:
                score+=0
                result8="Incorrect"

        #9th_question_answer_A

            print('       Q9. Entomology is the science that studies')
            print()
            print('           (a) Insects')
            print()
            print('           (b) Behavior of human beings')
            print()
            print('           (c) The origin and history of technical and scientific terms')
            print()
            print('           (d) The formation of rocks')
            print()
            a9=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a9 in ('(A)','(a)','A','a'):
                score+=4
                result9="Correct"
            elif a9 in ('(B)','(b)','B','b'):
                score-=1
                result9="Incorrect"
            elif a9 in ('(C)','(c)','C','c'):
                score-=1
                result9="Incorrect"
            elif a9 in ('(D)','(d)','D','d'):
                score-=1
                result8="Incorrect"
            else:
                score+=0
                result8="Incorrect"

        #10th_question_answer_B

            print('      Q10. Eritrea, which became the 182nd member of the UN in 1993,')
            print('           is in the continent of')
            print()
            print('           (a) Asia')
            print()
            print('           (b) Africa')
            print()
            print('           (c) Europe')
            print()
            print('           (d) Australia')
            print()
            a10=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a10 in ('(A)','(a)','A','a'):
                score-=1
                result10="Incorrect"
            elif a10 in ('(B)','(b)','B','b'):
                score+=4
                result10="Correct"
            elif a10 in ('(C)','(c)','C','c'):
                score-=1
                result10="Incorrect"
            elif a10 in ('(D)','(d)','D','d'):
                score-=1
                result10="Incorrect"
            else:
                score+=0
                result10="Incorrect"

            #--------------------------------------------------------------------------------------

            os.system('cls')
            print()
            print()
            print('       Please wait.. ')
            time.sleep(3)
            os.system('cls')
            print()
            print()
            print()

        #end_of_question

            print('           --------------------- Test analysis -----------------------')
            print()
            print('                 Your answer \t Correct answer \t Status')
            print()
            print('           -----------------------------------------------------------')
            print()
            print('           Q1.  ',a1,'\t\t (A) \t\t\t',result1)
            print()
            print('           Q2.  ',a2,'\t\t (D) \t\t\t',result2)
            print()
            print('           Q3.  ',a3,'\t\t (A) \t\t\t',result3)
            print()
            print('           Q4.  ',a4,'\t\t (A) \t\t\t',result4)
            print()
            print('           Q5.  ',a5,'\t\t (C) \t\t\t',result5)
            print()
            print('           Q6.  ',a6,'\t\t (B) \t\t\t',result6)
            print()
            print('           Q7.  ',a7,'\t\t (D) \t\t\t',result7)
            print()
            print('           Q8.  ',a8,'\t\t (C) \t\t\t',result8)
            print()
            print('           Q9.  ',a9,'\t\t (A) \t\t\t',result9)
            print()
            print('          Q10.  ',a10,'\t\t (B) \t\t\t',result10)
            print()
            print('           -----------------------------------------------------------')
            print()
            print('           Total marks obtained :',score,'out of 40')
            print()
            pert=(score*100)/40
            print('           Total percentage :',pert,'%')
            print()
            if pert>90:
                grade='A1'
                msg='Congratulations !!'
                ext=''
            elif pert>80:
                grade='A2'
                msg='Congratulations !!'
                ext=''
            elif pert>70:
                grade='B1'
                msg='Good !!'
                ext=''
            elif pert>60:
                grade='B2'
                msg='Good !!'
                ext=''
            elif pert>40:
                grade='C'
                msg='Sorry !!'
                ext='Better luck next time !!'
            elif pert>20:
                grade='D'
                msg='Sorry !!'
                ext='Better luck next time !!'
            elif pert>0:
                grade='E'
                msg='Sorry !!'
                ext='Better luck next time !!'
            elif pert<0:
                grade='F'
                msg='Sorry !!'
                ext='Better luck next time !!'
            print('          ',msg,grade,'is awarded.',ext)

    #break---------------------------------------------------------------------------------------------------------------

        elif topic in ('(4.)','(4)','4.','4'):
            score=0
            print('       Welcome ',name,'. All the best !!',sep='')
            print()
            print('------------------------------------')
            print('               |')
            print('       Topic 4 - Mental ability Test')
            print('               |')
            print('------------------------------------')
            print()
            print()

        #1st_question_answer_B

            print('       Q1. ‘Pen’ is related to ‘plastic’ similarly ‘pencil’ is related to:')
            print()
            print('           (a) Plastic')
            print()
            print('           (b) Wood')
            print()
            print('           (c) Granite')
            print()
            print('           (d) None')
            print()
            a1=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a1 in ('(A)','(a)','A','a'):
                score-=1
                result1="Incorrect"
            elif a1 in ('(B)','(b)','B','b'):
                score+=4
                result1="Correct"
            elif a1 in ('(C)','(c)','C','c'):
                score-=1
                result1="Incorrect"
            elif a1 in ('(D)','(d)','D','d'):
                score-=1
                result1="Incorrect"
            else:
                score+=0
                result1="Incorrect"

        #2nd_question_answer_B

            print('       Q2. Ten years ago Sam\’s mother is 5 times older than her son.')
            print('           After 10 years mother is thrice the son\’s age .The present')
            print('           age of Sam is:')
            print()
            print('           (a) 20')
            print()
            print('           (b) 30')
            print()
            print('           (c) 40')
            print()
            print('           (d) 50')
            print()
            a2=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a2 in ('(A)','(a)','A','a'):
                score-=1
                result2="Incorrect"
            elif a2 in ('(B)','(b)','B','b'):
                score+=4
                result2="Correct"
            elif a2 in ('(C)','(c)','C','c'):
                score-=1
                result2="Incorrect"
            elif a2 in ('(D)','(d)','D','d'):
                score-=1
                result2="Incorrect"
            else:
                score+=0
                result2="Incorrect"

        #3rd_question_answer_C

            print('       Q3. Find the next term in series 4D7, 9G9, 16J11, ...?')
            print()
            print('           (a) 20N12')
            print()
            print('           (b) 20M13')
            print()
            print('           (c) 25M13')
            print()
            print('           (d) 25N13')
            print()
            a3=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a3 in ('(A)','(a)','A','a'):
                score-=1
                result3="Incorrect"
            elif a3 in ('(B)','(b)','B','b'):
                score-=1
                result3="Incorrect"
            elif a3 in ('(C)','(c)','C','c'):
                score+=4
                result3="Correct"
            elif a3 in ('(D)','(d)','D','d'):
                score-=1
                result3="Incorrect"
            else:
                score+=0
                result3="Incorrect"

        #4th_question_answer_D

            print('       Q4. Study the following arrangement carefully and answer the question')
            print('           given below:')
            print()
            print('           G Q W 3 & A 9 8 @ * V S ^ 4 H X P L M K 1 4 5 D')
            print()
            print('           Complete the series. G3, &8, @S, ___')
            print()
            print('           (a) 58')
            print()
            print('           (b) 14')
            print()
            print('           (c) @*')
            print()
            print('           (d) ^X')
            print()
            a4=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a4 in ('(A)','(a)','A','a'):
                score-=1
                result4="Incorrect"
            elif a4 in ('(B)','(b)','B','b'):
                score-=1
                result4="Incorrect"
            elif a4 in ('(C)','(c)','C','c'):
                score-=1
                result4="Incorrect"
            elif a4 in ('(D)','(d)','D','d'):
                score+=4
                result4="Correct"
            else:
                score+=0
                result4="Incorrect"

        #5th_question_answer_A

            print('       Q5. In these series, you will be looking at both the letter pattern')
            print('           and the number pattern. Fill the blank in the middle of the series')
            print('           or end of the series.')
            print()
            print('           K77M, N67O, Q57Q, ? , W37U')
            print()
            print('           (a) T47S')
            print()
            print('           (b) G47S')
            print()
            print('           (c) G76R')
            print()
            print('           (d) I76T')
            print()
            a5=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a5 in ('(A)','(a)','A','a'):
                score+=4
                result5="Correct"
            elif a5 in ('(B)','(b)','B','b'):
                score-=1
                result5="Incorrect"
            elif a5 in ('(C)','(c)','C','c'):
                score-=1
                result5="Incorrect"
            elif a5 in ('(D)','(d)','D','d'):
                score-=1
                result5="Incorrect"
            else:
                score+=0
                result5="Incorrect"

        #6th_question_answer_C

            print('       Q6. Out of 46 students, rank of Shiva is ranked as 12th. What will')
            print('           be his rank from below?')
            print()
            print('           (a) 37')
            print()
            print('           (b) 36')
            print()
            print('           (c) 35')
            print()
            print('           (d) 34')
            print()
            a6=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a6 in ('(A)','(a)','A','a'):
                score-=1
                result6="Incorrect"
            elif a6 in ('(B)','(b)','B','b'):
                score-=1
                result6="Incorrect"
            elif a6 in ('(C)','(c)','C','c'):
                score+=4
                result6="Correct"
            elif a6 in ('(D)','(d)','D','d'):
                score-=1
                result6="Incorrect"
            else:
                score+=0
                result6="Incorrect"

        #7th_question_answer_B
            print('       Q7. Three of the following four are same in a certain way and hence')
            print('           form a group. Find out the one which does not belong to that group.')
            print()
            print('           (a) Printer')
            print()
            print('           (b) Reader')
            print()
            print('           (c) Writer')
            print()
            print('           (d) Publisher')
            print()
            a7=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a7 in ('(A)','(a)','A','a'):
                score-=1
                result7="Incorrect"
            elif a7 in ('(B)','(b)','B','b'):
                score+=4
                result7="Correct"
            elif a7 in ('(C)','(c)','C','c'):
                score-=1
                result7="Incorrect"
            elif a7 in ('(D)','(d)','D','d'):
                score-=1
                result7="Incorrect"
            else:
                score+=0
                result7="Incorrect"

        #8th_question_answer_D

            print('       Q8. Khan family in Lucknow is well-known for their bakery business.')
            print('           Rahim Khan is the owner of the house and he has two girl child')
            print('           named Shabnam and Shahida. Shabnam is married to Tariq and Sheikh')
            print('           is her son. Sattar is husband of Shahida and Suliemann is their')
            print('           only child. Suliemann is grandson of Salma.')
            print()
            print('           How is Tariq related to Shahida?')
            print()
            print('           (a) Son')
            print()
            print('           (b) Brother')
            print()
            print('           (c) Nephew')
            print()
            print('           (d) Brother-in-law')
            print()
            a8=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a8 in ('(A)','(a)','A','a'):
                score-=1
                result8="Incorrect"
            elif a8 in ('(B)','(b)','B','b'):
                score-=1
                result8="Incorrect"
            elif a8 in ('(C)','(c)','C','c'):
                score-=1
                result8="Incorrect"
            elif a8 in ('(D)','(d)','D','d'):
                score+=4
                result8="Correct"
            else:
                score+=0
                result8="Incorrect"

        #9th_question_answer_D

            print('       Q9. If Dev says that his mother is the only girl child of Cindy\’s')
            print('           mother, how is Cindy related to Dev?')
            print()
            print('           (a) Son')
            print()
            print('           (b) Father')
            print()
            print('           (c) Brother')
            print()
            print('           (d) Uncle')
            print()
            a9=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a9 in ('(A)','(a)','A','a'):
                score-=1
                result9="Incorrect"
            elif a9 in ('(B)','(b)','B','b'):
                score-=1
                result9="Incorrect"
            elif a9 in ('(C)','(c)','C','c'):
                score-=1
                result9="Incorrect"
            elif a9 in ('(D)','(d)','D','d'):
                score+=4
                result9="Correct"
            else:
                score+=0
                result9="Incorrect"

        #10th_question_answer_A

            print('      Q10. 570, 566, 576, 572, 582, 578, _')
            print()
            print('           (a) 588')
            print()
            print('           (b) 580')
            print()
            print('           (c) 590')
            print()
            print('           (d) 586')
            print()
            a10=input('       Answer : ')
            print()
            print('==============================================================================')
            print()
            if a10 in ('(A)','(a)','A','a'):
                score+=4
                result10="Correct"
            elif a10 in ('(B)','(b)','B','b'):
                score-=1
                result10="Incorrect"
            elif a10 in ('(C)','(c)','C','c'):
                score-=1
                result10="Incorrect"
            elif a10 in ('(D)','(d)','D','d'):
                score-=1
                result10="Incorrect"
            else:
                score+=0
                result10="Incorrect"

            #--------------------------------------------------------------------------------------

            os.system('cls')
            print()
            print()
            print('       Please wait.. ')
            time.sleep(3)
            os.system('cls')
            print()
            print()
            print()

        #end_of_question

            print('           --------------------- Test analysis -----------------------')
            print()
            print('                 Your answer \t Correct answer \t Status')
            print()
            print('           -----------------------------------------------------------')
            print()
            print('           Q1.  ',a1,'\t\t (B) \t\t\t',result1)
            print()
            print('           Q2.  ',a2,'\t\t (B) \t\t\t',result2)
            print()
            print('           Q3.  ',a3,'\t\t (C) \t\t\t',result3)
            print()
            print('           Q4.  ',a4,'\t\t (D) \t\t\t',result4)
            print()
            print('           Q5.  ',a5,'\t\t (A) \t\t\t',result5)
            print()
            print('           Q6.  ',a6,'\t\t (C) \t\t\t',result6)
            print()
            print('           Q7.  ',a7,'\t\t (B) \t\t\t',result7)
            print()
            print('           Q8.  ',a8,'\t\t (D) \t\t\t',result8)
            print()
            print('           Q9.  ',a9,'\t\t (D) \t\t\t',result9)
            print()
            print('          Q10.  ',a10,'\t\t (A) \t\t\t',result10)
            print()
            print('           -----------------------------------------------------------')
            print()
            print('           Total marks obtained :',score,'out of 40')
            print()
            pert=(score*100)/40
            print('           Total percentage :',pert,'%')
            print()
            if pert>90:
                grade='A1'
                msg='Congratulations !!'
                ext=''
            elif pert>80:
                grade='A2'
                msg='Congratulations !!'
                ext=''
            elif pert>70:
                grade='B1'
                msg='Good !!'
                ext=''
            elif pert>60:
                grade='B2'
                msg='Good !!'
                ext=''
            elif pert>40:
                grade='C'
                msg='Sorry !!'
                ext='Better luck next time !!'
            elif pert>20:
                grade='D'
                msg='Sorry !!'
                ext='Better luck next time !!'
            elif pert>0:
                grade='E'
                msg='Sorry !!'
                ext='Better luck next time !!'
            elif pert<0:
                grade='F'
                msg='Sorry !!'
                ext='Better luck next time !!'
            print('          ',msg,grade,'is awarded.',ext)
            print()
            print('           -----------------------------------------------------------')
            print()

#break---------------------------------------------------------------------------------------------------------------

        elif topic in ('(5.)','(5)','5.','5'):
            time.sleep(2)
            os.system('cls')
            print()
            print()
            print()
            print('   Well, thank you and visit again with cool mind :> !!')
            break

#break---------------------------------------------------------------------------------------------------------------

        else:
            print('   Sorry, didn\'t catch that :< !!')
            break
        print()
        print()
        again=input("           Want to give test again? ")
        if again in ('yes','Yes','Y','y'):
            time.sleep(2)
            os.system('cls')
            print()
            print(f'           Please wait ...')
            print()
            continue
        elif again in ('no','No','N','n'):
            time.sleep(2)
            os.system('cls')
            print()
            print(f'           Thank you {name}, Visit again !!')
            print()
            print('           Exiting the program .....')
            time.sleep(3)
            exit()
        else:
            break
        	
#break---------------------------------------------------------------------------------------------------------------

elif test in ('no','No','N','n'):
	print()
	print()
	print()
	print('   Well, thank you and visit again with cool mind :> !!')
else:
	print()
	print()
	print()
	print('   Sorry, didn\'t catch that :< !!')
print()
print()
print('-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-')
print('================================ Thank you !! ===================================')
print('-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-=+=-')
print()