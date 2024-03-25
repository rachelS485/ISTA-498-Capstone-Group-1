from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

courses = "https://catalog.arizona.edu/courses?page=1&cq="
driver.get(courses)

core_courses= ["ISTA116", "ISTA130","ISTA131","ISTA161"]
emphasis_datascience= ["ESOC 414","ISTA311","ISTA320","ISTA321","ISTA322","ISTA331","ISTA350","ISTA355","ISTA410","ISTA421","ISTA429","ISTA431","ISTA439","ISTA450","ISTA455","ISTA456","ISTA457","LIS470"]
emphasis_interactive_immersive_technologies = ["GAME425", "GAME451","ISTA303","ISTA320", "ISTA330", "ISTA350", "ISTA403", "ISTA416", "ISTA424", "ISTA495"]
computational_arts_media = ["ESOC300","ESOC340", "ISTA301","ISTA302","ISTA303", "ISTA329", "ISTA352","ISTA401","ISTA403"]
society = ["ESOC313","ESOC314","ESOC315","ESOC316","ESOC317", "ESOC318","ESOC319", "ESOC330", "ESOC477", "ESOC478", "ESOC488", "ESOC495"]
research_method = ["ESOC302"]
engangement=["ESOC480","ISTA498"]

core = []
data_science = []
immersive_tech = []
comp_arts = []
soc = []
research = []
engange = []


##### CORE COURSES #########
##ISTA 100
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA100"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')

#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

core.append([name.text,desc.text,unit.text])


##ISTA 116
courses = "https://catalog.arizona.edu/courses?page=1&cq=" + "ISTA116"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)
    
#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

core.append([name.text,desc.text,unit.text])

##ISTA 130
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA130"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

core.append([name.text,desc.text,unit.text])

##ISTA 131
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA131"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

core.append([name.text,desc.text,unit.text])

##ISTA 161
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA161"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)
    
core.append([name.text,desc.text,unit.text])


###### DATA SCIENCE EMPHASIS COURSES

##ESOC 414
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC414"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

data_science.append([name.text,desc.text,unit.text])

##ISTA 311
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA311"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

data_science.append([name.text,desc.text,unit.text])

##ISTA 320
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA320"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)
    
data_science.append([name.text,desc.text,unit.text])

##ISTA 321
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA321"
driver.implicitly_wait(5)
driver.get(courses)
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

data_science.append([name.text,desc.text,unit.text])

##ISTA 322
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA322"
driver.implicitly_wait(5)
driver.get(courses)

#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)
    
data_science.append([name.text,desc.text,unit.text])

##ISTA 331
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA331"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

data_science.append([name.text,desc.text,unit.text])

##ISTA 350
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA350"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

data_science.append([name.text,desc.text,unit.text])

##ISTA 355
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA355"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)
    
#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

data_science.append([name.text,desc.text,unit.text])

##ISTA 410
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA410"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

data_science.append([name.text,desc.text,unit.text])

##ISTA 421
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA421"
driver.implicitly_wait
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

data_science.append([name.text,desc.text,unit.text])

##ISTA 429
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA429"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)
    
#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)
    
data_science.append([name.text,desc.text,unit.text])

##ISTA 431
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA431"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)
    
#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)
    
data_science.append([name.text,desc.text,unit.text])


##ISTA 439
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA439"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)
    
#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)
    
data_science.append([name.text,desc.text,unit.text])

##ISTA 450
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA450"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)
    
#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)
    
data_science.append([name.text,desc.text,unit.text])

##ISTA 455
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA455"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)
    
#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)
    
data_science.append([name.text,desc.text,unit.text])

##ISTA 456
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA456"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)
    
#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)
    
data_science.append([name.text,desc.text,unit.text])

##ISTA 457
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA457"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)
    
#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)
    
data_science.append([name.text,desc.text,unit.text])

##LIS 470
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "LIS470"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)
    
#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)
    
data_science.append([name.text,desc.text,unit.text])


#### INTERACTIVE AND IMMERSIVE TECHNOLOGIES EMPHASIS

##GAME 425
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"GAME425"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)
immersive_tech.append([name.text,desc.text,unit.text]) 

##GAME 451
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"GAME451"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

immersive_tech.append([name.text,desc.text,unit.text])

##ISTA 303
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA303"
driver.implicitly_wait(5)
driver.get(courses)
      
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

immersive_tech.append([name.text,desc.text,unit.text])

##ISTA 320
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA320"
driver.implicitly_wait(5)
driver.get(courses)

#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

immersive_tech.append([name.text,desc.text,unit.text])

##ISTA 330

courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA330"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

immersive_tech.append([name.text,desc.text,unit.text])

##ISTA 350
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA350"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

immersive_tech.append([name.text,desc.text,unit.text])

##ISTA 403
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA403"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

immersive_tech.append([name.text,desc.text,unit.text])

##ISTA 416
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA416"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

immersive_tech.append([name.text,desc.text,unit.text])

##ISTA 424
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA424"
driver.implicitly_wait(5)
driver.get(courses)
    
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

immersive_tech.append([name.text,desc.text,unit.text])

##ISTA 495
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA495"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

immersive_tech.append([name.text,desc.text,unit.text])

######COMPUTATIONAL ARTS AND MEDIA#####

##ESOC 300
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ESOC300"
driver.implicitly_wait(5)
driver.get(courses)
    
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

comp_arts.append([name.text,desc.text,unit.text])

##ESOC 340
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ESOC340"
driver.implicitly_wait(5)
driver.get(courses)    
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

comp_arts.append([name.text,desc.text,unit.text])

##ISTA 301
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA301" 
driver.implicitly_wait(5)
driver.get(courses)
    
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

comp_arts.append([name.text,desc.text,unit.text])

##ISTA 302
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA302" 
driver.implicitly_wait(5)
driver.get(courses)
    
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

comp_arts.append([name.text,desc.text,unit.text])

##ISTA 303
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA303"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

comp_arts.append([name.text,desc.text,unit.text])

##ISTA 329
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA329"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

comp_arts.append([name.text,desc.text,unit.text])

##ISTA 352
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA352"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

comp_arts.append([name.text,desc.text,unit.text])

##ISTA 401
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ISTA401"
driver.implicitly_wait(5)
driver.get(courses)
      
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

comp_arts.append([name.text,desc.text,unit.text])

##ISTA 403
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA403" 
driver.implicitly_wait(5)
driver.get(courses)
    
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

comp_arts.append([name.text,desc.text,unit.text])    


##### SOCIETY #######

##ESOC 313
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+ "ESOC313"
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

soc.append([name.text,desc.text,unit.text]) 

##ESOC 314
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC314" 
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

soc.append([name.text,desc.text,unit.text])  


##ESOC 315
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC315"
driver.implicitly_wait(5) 
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

soc.append([name.text,desc.text,unit.text]) 

##ESOC 316
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC316"
driver.implicitly_wait(5) 
driver.get(courses)
    
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

soc.append([name.text,desc.text,unit.text])   


##ESOC 317
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC317" 
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

soc.append([name.text,desc.text,unit.text])   


##ESOC 318
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC318" 
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

soc.append([name.text,desc.text,unit.text])

##ESOC 319
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC319" 
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

soc.append([name.text,desc.text,unit.text])

##ESOC 330
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC330"
driver.implicitly_wait(5) 
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

soc.append([name.text,desc.text,unit.text])

##ESOC 477

courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC477" 
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = ' //*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

soc.append([name.text,desc.text,unit.text]) 

#ESOC 478
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC478" 
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

soc.append([name.text,desc.text,unit.text])

##ESOC 495
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC495" 
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

soc.append([name.text,desc.text,unit.text])


##### RESEARCH METHODS

##ESOC 302
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC302" 
driver.implicitly_wait(5)
driver.get(courses)
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

research.append([name.text,desc.text,unit.text])


##### ENGAGMENT ####

##ESOC 480
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ESOC480" 
driver.implicitly_wait(5)
driver.get(courses)
    
    
#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

engange.append([name.text,desc.text,unit.text])

##ISTA 498
courses =  "https://catalog.arizona.edu/courses?page=1&cq="+"ISTA498"
driver.implicitly_wait(5) 
driver.get(courses)

#Pressing the course button
course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
course_btn = driver.find_element(By.XPATH, course_btn_path)
course_btn.click()

#Getting the course name, printing it (to make sure it works), appending to the respective list  
course_name= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1')
#The for loop will print the name of the course name.
for name in course_name:
    print(name.text)
    
#Getting the course description, printing it (to make sure it works), appending to the respective list  
course_desc= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div')
#The for loop will print the name of the course name.
for desc in course_desc:
    print(desc.text)

#Getting the course unit, printing it (to make sure it works), appending to the respective list  
course_unit= driver.find_elements(By.XPATH,'//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div')
#The for loop will print the name of the course name.
for unit in course_unit:
    print(unit.text)

engange.append([name.text,desc.text,unit.text])