###########################################################################################################################################################
#-PROGRAM 1 

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626,
           949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
for i in numbers:
    if(i==237):
        break
    elif(i%2==0):
        print(i)


############################################################################################################################################################
#PROGRAM 2

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
final_list  = color_list_1 - color_list_2
print(final_list)


############################################################################################################################################################
#PROGRAM 3

alphabet = "abcdefghijklmnopqrstuvwxyz"
sentence = input("Write your setence : " )
flag = 0 
for char in alphabet:
    if char in sentence.lower():
         flag = 0
    else:
         flag = -1
if(flag==0):
    print("Given sentence is a Pangram ")
elif(flag==-1):
    print("Given sentence is Not a Pangram ")

         


##############################################################################################################################################################
#PROGRAM  4

n = int(input("Enter yor given number :"))
answer = (n + ((n*10)+n) + (n*100)+((n*10)+n))
print(answer)


##############################################################################################################################################################
#PROGRAM 5

input_list = input("Enter your input : " )
result = []
result = input_list.split("#")


list1 = []
list2 = []
for i in list(result[0].split()):
    list1.append(int(i))
print(list1)

for i in list(result[1].split()):
    list2.append(int(i))
print(list2)


#################################################################################################################################################################
#PROGRAM 6  

output = []
s = input("Enter your Sequence : ")
output = s.split(",")
print("," .join(sorted(output)))


##################################################################################################################################################################
###PROGRAM 7

d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
index = 0 
for i in d['Marks']:
    if(i==max(d['Marks'])):
          break 
    elif(i!=max(d['Marks'])):
         index+=1
print(d['Student'][index])

###################################################################################################################################################################
##PROGRAM 8

s = input("Input a string : ")
digit,letter = 0,0
for c in s:
    if c.isdigit():
        digit=digit+1
    elif c.isalpha():
        letter=letter+1
    else:
        pass
print("Letters", letter)
print("Digits", digit)

###################################################################################################################################################################
#PROGRAM 9

d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
n = input("Enter your subject : ")
d1 =[]
newdata= {}

for i in range(len(d['Subject'])):
    if(d['Subject'][i]==n):
        d1.append(i)

newdata['Name'] = []
newdata['Subject'] = []
newdata['Ratings'] = []
for i in d1:
    newdata['Name'].append(d['Name'][i])
    newdata['Subject'].append(d['Subject'][i])
    newdata['Ratings'].append(d['Ratings'][i])
print(newdata)


######################################################################################################################################################################
#PROGRAM  10

n = int(input("Enter the range upto: "))
def divbyseven(n):
    for i in range(1,n+1):
        if i % 7 == 0:
            yield i
        else:
            continue
for num in divbyseven(n):
	print(num)



##########################################################################################################################################################################
#PROGRAM 11

input_list = []
x = None
print('Enter direction and route(in this format DIRECTION<space>STEPS):')
for _ in range(0,4):
    s = input('')
    x = s.split(' ')
    input_list.append(x)
up_steps = 0
down_steps = 0
left_steps = 0
right_steps = 0

for i in input_list:
    if i[0].upper() == 'UP':
        up_steps = int(i[1]) 
    elif i[0].upper() == 'DOWN':
        down_steps = int(i[1])
    elif i[0].upper() == 'LEFT':
        left_steps = int(i[1])
    elif i[0].upper() == 'RIGHT':
        right_steps = int(i[1])

v_distance = up_steps-down_steps
h_distance = left_steps-right_steps

print(v_distance)
print(h_distance)

total_diatance = round(abs(((v_distance**2)+(h_distance**2))**0.5))
print(total_diatance)

#################################################################################
