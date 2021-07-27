# case 02


def marking_process():

    if pass_marks == 120:
        return 'p'

    elif pass_marks == 100:
        return 't'

    elif fail_marks >= 80:
        return 'e'

    else:
        return 'm'


def validation(mark_p, mark_d, mark_f):
    
    
    if mark_p + mark_d + mark_f == 120:
    
        if mark_p % 20 != 0 or mark_d % 20 != 0 or mark_f % 20 != 0:
            print('Range error')
            return False
        else:
            return True

    else:
        print('Total incorrect')
        return False


def is_q(marks):
    if marks == 'q':
        return True

    return False

#histrogram
def histrogram():
    print(f'Progress {progress}: \t{"*" * progress}')
    print(f'Trailing {module_trailer}: \t{"*" * module_trailer}')
    print(f'Retriever {module_retriever}: \t{"*" * module_retriever}')
    print(f'Excluded {exclude}: \t{"*" * exclude}')       

    print('\n',progress + module_trailer + module_retriever + exclude,'outcomes in total.\n')     
    

progress = 0
module_trailer = 0
module_retriever = 0
exclude = 0

while True:

    try:
        pass_marks = input('Enter your pass credit ')
        if is_q(pass_marks):
            break
        pass_marks = int(pass_marks)

        defer_marks = input('Enter your defer credit ')
        if is_q(defer_marks):
            break
        defer_marks = int(defer_marks)

        fail_marks = input('Enter your fail credit ')
        if is_q(fail_marks):
            break
        fail_marks = int(fail_marks)

    except ValueError:
        print('Integers required')
        continue

    if validation(pass_marks, defer_marks, fail_marks):

        if marking_process() == 'p': 
            progress += 1
            print('Progression Outcome :', 'Progress')

        elif marking_process() == 't':
            module_trailer += 1
            print('Progression Outcome :', 'Progress – module trailer')

        elif marking_process() == 'e':
            module_retriever += 1
            print('Progression Outcome :', 'Exclude')

        elif marking_process() == 'm':
            exclude += 1
            print('Progression Outcome :', 'Do not progress – module retriever')

histrogram() #histrogram function
 

