
class Question:
    number_of_questions = 0
    def __init__(self , text , choices , answer ):
        self.text = text
        self.choices = choices
        self.answer = answer
        Question.number_of_questions += 1

    number_of_true_answer = 0
    def checkAnswer(a,b,c):
        if b not in c:
            raise ValueError('Hatalı bir cevap girdiniz. Lütfen testi tekrardan başlatın. ')
        if a == b :
            Question.number_of_true_answer += 1
            print('Cevabınız Doğru')
        else:
            print('Cevabınız Yanlış')

q1 = Question('Barış Erbayın Doğum Yılı Nedir ?' , ['1994' , '1995' , '1996' , '1997'] , '1997'  )
q2 = Question('Barış Erbay hangi fakülte mezunudur ?' , ['hukuk' , 'mühendislik' , 'iktisat' , 'işletme'] , 'hukuk'  )
q3 = Question('Barış Erbay hangi şehirde doğmuştur ?' , ['adana' , 'gaziantep' , 'İzmir' , 'istanbul'] , 'gaziantep'  )
q4 = Question('Barış Erbay\' ın boyu kaç cm\'dir ? ' , ['178' , '180' , '183' , '185'] , '180'  )
q5 = Question('Barış Erbay hangi üniversiteden mezun olmuştur ?' , ['doğu akdeniz üniversitesi' , 'uluslararası kıbrıs üniversitesi' , 'yakın doğu üniversitesi' , 'girne amerikan üniversitesi'] , 'uluslararası kıbrıs üniversitesi'  )
q6 = Question('Barış Erbay hangi yılda üniversiteye başlamıştır ?' , ['2013' , '2014' , '2015' , '2016'] , '2015'  )

questions = [q1,q2,q3,q4,q5,q6]

for q in questions:

    print(f' {q.text} - Seçenekler : {q.choices}')
    cevap = input('Lütfen cevabınızı yazınız : ')
    Question.checkAnswer(q.answer, cevap , q.choices) 
    print('----------------------------------------------------------')

print(f' {Question.number_of_questions} soruda {Question.number_of_true_answer} doğru cevabınız bulunmaktadır.  ')

