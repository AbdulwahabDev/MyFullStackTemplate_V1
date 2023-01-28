# Tuwaiq_Team_Project

# pre request steps before run docker images ...
- (frontend_angular_app) :
    - cd frontend/frontend_angular_app
    - npm install -g @angular/cli
    - npm install
    - ng build ( YOU MUST DO IT EACH TIME BEFORE RUN frontend_angular_app DOCKER IMAGE ... )

# STEP 1 
- docker compose up --build
OR (preferred)
- docker compose up pgsql  --build  
- docker compose up auth_app  --build  
- docker compose up frontend_angular_app  --build   // do not forget to build angular before !!

# STEP 2 add first user
- http://127.0.0.1:3101/USERS_Entities_seeds?UserName=admin&Paswword=admin

# STEP 3 login from fronend   
- URL http://127.0.0.1:4201
- username : admin
- password : 123456


##  HAVE FUN :) 
