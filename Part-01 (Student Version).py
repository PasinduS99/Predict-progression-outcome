# case01


def marking_process():

    if pass_marks == 120:
        print('Progression Outcome :', 'Progress')
        

    elif pass_marks == 100:
        print('Progression Outcome :', 'Progress – module trailer')
        

    elif fail_marks >= 80:
        print('Progression Outcome :', 'Exclude')

    else:
        print('Progression Outcome :', 'Do not progress – module retriever')


def validation(mark_p, mark_d, mark_f):
    if mark_p + mark_d + mark_f == 120:

        if mark_p % 20 != 0 or mark_d % 20 != 0 or mark_f % 20 != 0:
            print('Range error')
          
        else:
            marking_process() # marking_process function

    else:
        print('Total incorrect')

       
progress = 0
module_trailer = 0
module_retriever = 0
exclude = 0

try:
    pass_marks = int(input('Enter your pass credit '))
    defer_marks = int(input('Enter your defer credit '))
    fail_marks = int(input('Enter your fail credit '))

    validation(pass_marks, defer_marks, fail_marks) #validation function

except ValueError:
    print('Integers required')
