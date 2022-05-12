from celery import shared_task
from celery_progress.backend import ProgressRecorder
import csv
from .models import Product, Channel
from time import sleep
from copy import deepcopy as dp

@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)
    for i in range(4):
        sleep(duration)
        progress_recorder.set_progress(i + 1, 4, f'On iteration {i}')
    return 'Done'



# @shared_task(bind=True)
# def go_insert_data(self, io_string):
#     progress_recorder = ProgressRecorder(self)
#     data=csv.reader(io_string, delimiter=',',quotechar="|")
#     print(data)
#     print(list(data))
#     print(len(list(data)),"lenlist")
#     print(sum(1 for i in range(data)),"lenlist")
#     print(data,"data")
#     for i, col in enumerate(data):
#         print(col,"colom")
#         progress_recorder.set_progress(i + 1, len(data) , f'On iteration {i}')
#         xx,created=Product.objects.update_or_create(
#             name=col[0],
#             code=col[1],
#             channel=Channel.objects.get(pk=int(col[2])),
#             status= int(col[3])
#         )
#     return 'Finnished Insert Data'

@shared_task(bind=True)
def save_product_from_csv(self,file_path):
    # do try catch accordingly
    # open csv file, read lines
    progress_recorder = ProgressRecorder(self)
    with open(file_path, 'r') as fp:
        productss = csv.reader(fp, delimiter=',')
        
        header=next(productss)
        products=list(productss)
        row_count = len(products)
        
        print(len(products), row_count, header)
        print(products, row_count, header)
        
        for i, col in enumerate(products):
            print(i, col)
            if i==0:
                pass
            else:
                progress_recorder.set_progress(i + 1, row_count , f'On iteration {i}')
                xx,created=Product.objects.update_or_create(
                name=col[0],
                code=col[1],
                channel=Channel.objects.get(pk=int(col[2])),
                status= int(col[3])
               
        )
                print("hehe",created)
        fp.close()
    
    return 'Done'


# def save_product_from_csv2(file_path):
#     # do try catch accordingly
#     # open csv file, read lines
#     print("hehe",file_path)
#     with open(file_path, 'r') as fp:
#         print("it is here")
#         products = csv.reader(fp, delimiter=',')
#         row_count = sum(1 for row in products)
#         line_number=0
#         for col in products:
#             print( col,"nnnnnn")
#             if line_number == 0:
#                 print(f'Column names are {", ".join(col)}')
#                 line_count += 1
#             else:
#                 print(f'Column else names are {", ".join(col)}')
                
#                 xx,created=Product.objects.update_or_create(
#                 name=col[0],
#                 code=col[1],
#                 channel=Channel.objects.get(pk=int(col[2])),
#                 status= int(col[3])
               
#         )
#                 print("hehe",created)
#         fp.close()
#     print("hehsse",products)
#     print("hehse",row_count)
#     # progress_recorder = ProgressRecorder(self)
#     # lo=[1,2,3,4,5,6,7]
#     # for i in range(12):
#     #     sleep(1)
#     #     progress_recorder.set_progress(i + 1, 12, f'On iteration {i}')
#     return 'Done'


# def save_product_from_csv2(file_path):

#     print("hehe",file_path)
#     file = open(file_path)
#     numline = len(file.readlines())
#     for i in file.readlines()[1:]:
#         print(i,"this is i")
#     print (numline,"numline",file)
#     file=open(file_path)
#     # file = open("Salary_Data.csv")
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     row_count = sum(1 for row in csvreader)
#     print(header,"header", row_count)
#     rows = []
#     for row in csvreader:
#         rows.append(row)
#     print(rows,"rows")
#     file.close()
    
#     rows = []
#     with open(file_path, 'r') as file:
#         csvreader = csv.reader(file)
#         header = next(csvreader)
#         for row in csvreader:
#             rows.append(row)
#     print(header,"header2")
#     print(rows,'row2')
#     # with open(file_path, 'r') as fp:
#     #     print("it is here")
#     #     products = csv.reader(fp, delimiter=',')
#     #     row_count = sum(1 for row in products)
#     #     line_number=0
#     #     for col in products:
#     #         print( col,"nnnnnn")
#     #         if line_number == 0:
#     #             print(f'Column names are {", ".join(col)}')
#     #             line_count += 1
#     #         else:
#     #             print(f'Column else names are {", ".join(col)}')
                
#     #             xx,created=Product.objects.update_or_create(
#     #             name=col[0],
#     #             code=col[1],
#     #             channel=Channel.objects.get(pk=int(col[2])),
#     #             status= int(col[3])
               
#     #     )
#     #             print("hehe",created)
#     #     fp.close()
#     # print("hehsse",products)
#     # print("hehse",row_count)
#     # progress_recorder = ProgressRecorder(self)
#     # lo=[1,2,3,4,5,6,7]
#     # for i in range(12):
#     #     sleep(1)
#     #     progress_recorder.set_progress(i + 1, 12, f'On iteration {i}')
#     return 'Done'

# import csv
# def save_new_students_from_csv(file_path):
#     # do try catch accordingly
#     # open csv file, read lines
#     with open(file_path, 'r') as fp:
#         students = csv.reader(fp, delimiter=',')
#         row = 0
#         for student in students:
#             if row==0:
#                 headers = student
#                 row = row + 1
#             else:
#                 # create a dictionary of student details
#                 new_student_details = {}
#                 for i in range(len(headers)):
#                     new_student_details[headers[i]] = student[i]

#                 # for the foreign key field current_class in Student you should get the object first and reassign the value to the key
#                 new_student_details['current_class'] = StudentClass.objects.get() # get the record according to value which is stored in db and csv file

#                 # create an instance of Student model
#                 new_student = Student()
#                 new_student.__dict__.update(new_student_details)
#                 new_student.save()
#                 row = row + 1
#         fp.close()