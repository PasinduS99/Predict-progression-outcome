# case 04


def marking_process():

    if pass_marks == 120:
        return 'p'

    elif pass_marks == 100:
        return 't'

    elif fail_marks >= 80:
        return 'e'

    else:
        return 'm'

#histrogram
def histrogram():
    max_value = max(progress, module_trailer, module_retriever, exclude)
    
    print('progress\ttrailing\tretriever\texclude')

    for i in range (max_value):
        if i < progress:
            print('   *\t\t   ',end = '')

        else:
            print('    \t\t   ',end = '') 

        if i < module_trailer:
            print('*\t\t   ',end = '')

        else:
            print(' \t\t   ',end = '')

        if i < module_retriever:
            print('*\t\t   ',end = '')

        else:
            print(' \t\t   ',end = '') 

        if i < exclude:
            print('*')

        else:
            print(' ') 


    print(progress + module_trailer + module_retriever + exclude,'outcomes in total')     
    

progress = 0
module_trailer = 0
module_retriever = 0
exclude = 0

index = 0

marks_list = [120,0,0,100,20,0,100,0,20,80,20,20,60,40,20,40,40,40,20,40,60,20,20,80,20,0,100,0,0,120]
while index < len(marks_list):
    pass_marks = marks_list[index]
    print(pass_marks)
    index += 1
    defer_marks = marks_list[index]
    print(defer_marks)
    index += 1
    fail_marks = marks_list[index]
    print(fail_marks)
    index += 1

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

histrogram()
 

