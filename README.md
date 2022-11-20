# MyFullStackTemplate_V1

 <hr />
 
- ### app_backend container ** Python@10 FastAPI **
- [ docker-compose > services > app_backend   ]
- POSTMAN APIs COLLECTION : [myfullstacktemplate-v1-POSTMAN-LINK](https://www.postman.com/universal-resonance-102655/workspace/myfullstacktemplate-v1)

 <hr />
 
- ### pgsql container ** POSTGRE@15 **
- [ docker-compose > services > pgsql   ]


- ### adminer container ** SIMPLE DB READER TOOL   **
- [ docker-compose > services > adminer   ] 


 <hr />
 
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
