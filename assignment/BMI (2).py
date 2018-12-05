#BMI CALCULATER
foot=.3048
inch=.0254
#this is your height in foot
myHeightfoot=input("Enter your height in foot>")
#this is your height in inch
myHeightinch=input("Enter your height in inch>")
#this is your height in  meter
myHeightmeter=myHeightfoot*foot+myHeightinch*inch
#this is my weight in kg
myWeight=input("Enter your weight in kg>")
#this is my bmi
myBmi=(myWeight)/(myHeightmeter**2)
print (myBmi)
