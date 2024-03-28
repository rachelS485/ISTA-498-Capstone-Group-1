import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

def send_email(receiver_email, subject, message):
    # Email configuration
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach message to email
    msg.attach(MIMEText(message, 'plain'))

    # Establish a secure connection with the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the SMTP server
    server.quit()

# Initialize Selenium WebDriver
driver = webdriver.Chrome()

# List of courses to scrape
research_methods = ["ESOC302"]

for course_code in research_methods:
    # URL for the course page
    course_url = "https://catalog.arizona.edu/courses?page=1&cq=" + course_code
    driver.get(course_url)

    # Clicking on the course button
    course_btn_path = '//*[@id="courses-list"]/div/div[2]/div/button'
    course_btn = driver.find_element(By.XPATH, course_btn_path)
    course_btn.click()

    # Getting the course information
    course_name = driver.find_element(By.XPATH, '//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/h1').text
    course_desc = driver.find_element(By.XPATH, '//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[1]/div/div/div').text
    course_unit = driver.find_element(By.XPATH, '//*[@id="main-content"]/main/aside[2]/div/div/div/div[3]/div[3]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div').text

    # Prepare the message for email
    message = f"Hi student,\n\nHere is the information for course {course_code}:\n\nName: {course_name}\nDescription: {course_desc}\nUnit: {course_unit}"

    # Send email reminder to students
    send_email("student@example.com", f"Reminder: Course Information for {course_code}", message)

# Quit the WebDriver
driver.quit()
