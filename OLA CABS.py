print("Available cars\nFor SUV press 1\nFor SEDAN press 2\nFor OMNI press 3")
car_type=eval(input("Select the type of car you want to ride:"))
Luxury=input("Do you need AC or NON AC:")
if(Luxury=="AC"):
    if(car_type==1):
        print("Charge for 1 person for per KM=Rs.40\nPassenger limit=7")
        no_of_passengers=eval(input("No.of Passengers:"))
        amount=no_of_passengers*40
    elif(car_type==2):
        print("Charge for 1 person for per KM=Rs.20\nPassenger limit=4")
        no_of_passengers=eval(input("No.of Passengers:"))
        amount=no_of_passengers*20
    elif(car_type==3):
        print("Charge for 1 person for per KM=Rs.50\nPassenger limit=9")
        no_of_passengers=eval(input("No.of Passengers:"))
        amount=no_of_passengers*50
elif(Luxury=="NON AC"):
    if(car_type==1):
        print("Charge for 1 person for per KM=Rs.30\nPassenger limit=7")
        no_of_passengers=eval(input("No.of Passengers:"))
        amount=no_of_passengers*30
    elif(car_type==2):
        print("Charge for 1 person for per KM=Rs.10\nPassenger limit=4")
        no_of_passengers=eval(input("No.of Passengers:"))
        amount=no_of_passengers*10
    elif(car_type==3):
        print("Charge for 1 person for per KM=Rs.40\nPassenger limit=9")
        no_of_passengers=eval(input("No.of Passengers:"))
        amount=no_of_passengers*40
     
start=eval(input("Enter the total KM reading at pickup:"))
destination=eval(input("Enter the total KM reading at dropout:"))
km_travelled=destination-start
total_amount=km_travelled*amount
share=total_amount/no_of_passengers
print("\t\tWelcome to OLA cabs\n"
      "Total KM travelled\t:Rs.",km_travelled,"\n"
      "The Amount to be paid\t:Rs.",total_amount,"\n"
      "Per Person Share\t:Rs.",share)
