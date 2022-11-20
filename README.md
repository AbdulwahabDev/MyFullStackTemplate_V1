# MyFullStackTemplate_V1

- ### app_backend container ** Python@10 FastAPI **
- [ docker-compose > services > app_backend   ]

- ### pgsql container ** POSTGRE@15 **
- [ docker-compose > services > pgsql   ]

- ### adminer container ** SIMPLE DB READER TOOL   **
- [ docker-compose > services > adminer   ] 

- ### app_frontend container ** NOT MODERN FRONTEND FRAMEWORK YET !! **
- [ docker-compose > services > app_frontend   ] 
 
  

# STEP 1 
- docker compose up 

# STEP 2 add first user
- http://127.0.0.1:3003/USERS_Entities_seeds?UserName=admin&Paswword=admin



# STEP 3 test login from fronend   
- URL http://localhost:3000
- username : admin
- password : admin


....

## you can accses db useing adminer 
- http://127.0.0.1:8080
- Server   : pgsql
- Username : postgres
- Password : postgres



### ---




##  HAVE FUN :)
