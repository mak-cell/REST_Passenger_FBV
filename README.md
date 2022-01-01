# REST_Passenger_FBV
This is a API App Based on Django Rest Framework -  
Which perform basic crud operation using function based api.  
@api_view   
Below are the API's   
GET http://127.0.0.1:8000/passenger/ - For Getting all Passenger List from DB  
POST http://127.0.0.1:8000/passenger/ - data - {"id":2,"firstname":"Jagan","lastname":"Behera","rewardpoint":"9.000"}  # To create a passenger  
  
GET http://127.0.0.1:8000/passenger_details/1(pk) - to fetch perticular passenger data  
PUT http://127.0.0.1:8000/passenger_details/1     {"id":1,"firstname":"Jagan","lastname":"Behera","rewardpoint":"9.000"} # For Pertial Update  
DELETE http://127.0.0.1:8000/passenger_details/1 # To delete pasenger data from db   
  
Auther - mohankrushnabehera@gmail.com  
mak-cell  
https://mak-cell.github.io/  
  
Thank You
