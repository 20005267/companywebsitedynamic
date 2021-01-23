# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAME:

## BASE.HTML:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Silicon Private Limited</title>
    <link rel="stylesheet" href="{% static 'css/layout.css' %}">
    <link rel = "icon" href ="{% static 'img/titleicon.jpg' %}" type = "image/x-icon"> 
              
</head>

<body>
    <div class="container">
    <div class="banner">
        Silicon Private Limited.
    </div>
    <div class="menu">
        <div class="menuitem"><a href="/home">Home</a></div> 
        <div class="menuitem"><a href="/products">Products</a></div> 
        <div class="menuitem"><a href="/people">People</a></div>
        <div class="menuitem"><a href="/contact">Contact Us</a></div> 
    </div><div class="content">
    {% block content %}    
    {% endblock  %}
    </div>
    <div class="footer">
        Copyright © 2020 Silicon Private Limited, Developed by Kayalvizhi
    </div>
    </div>
</body>

</html>
```
## HOME.HTML:
```
{% extends "companyapp/base.html" %}

{% block content %}
    <div class="homecontent">    
    <h1>About Us</h1>
    <img src="/static/img/building2.jpg" alt="Building">
    <div class="contenttext">
    Silicon Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications that serve the data center, networking, software, broadband, wireless, and storage and industrial markets. Common applications for its products include: data center networking, home connectivity, broadband access, telecommunications equipment, smartphones, base stations, data center servers and storage, factory automation, power generation and alternative energy systems, displays, and mainframe operations and management, and application software development. Some of Silicon's core technologies and products include:
    <ul>
        <li>Memory Chips</li>
        <li>SATA HDD</li>
        <li>SATA SSD </li>
        <li>Broadband Modems</li>
        <li>Wifi Devices</li>
        <li>Switching Devices</li>
        <li>Optical Sensors</li>
    </ul> 
    </div>
    </div>
{% endblock  %}
```
## PEOPLE.HTML:
```
{% extends "companyapp/base.html" %}
{% load static %}
<!DOCTYPE html>
<html>

<head>
    <title>PEOPLE LIST</title>
    <link rel="stylesheet" href="{% static 'css/layout.css' %}">
</head>

<body>
    {% block content %}
    <div class="container">
        <h1>OUR PEOPLES</h1>
        <div class="content">
            <div class="peoplelist">
                {% for people in peoples %}
                <div class="people">
                    <div class="peoplelist">
                        <img src="{{ people.photo.url }}" alt="people image">
                    </div>
                    <div class="peoplephoto">{{ photo }}</div>
                    <div class="peoplename">{{ people.name }}</div>
                    <div class="peopledesignation">{{ people.designation }}</div>
                </div>
                {% endfor %}
            </div>
       </div>
    {% endblock %}
    </div>
</body>

</html>
```
## PRODUCTS.HTML:
```

{% extends "companyapp/base.html" %}
{% load static %}
<!DOCTYPE html>
<html>

<head>
    <title>PRODUCTS LIST</title>
    <link rel="stylesheet" href="{% static 'css/people.css' %}">
</head>

<body>
    {% block content %}
    <div class="container">
        <h1>OUR PREMIUM PRODUCTS</h1>
        <div class="content">
            <div class="peoplelist">
                {% for product in products %}
                <div class="people">
                    <div class="peoplelist">
                        <img src="{{ product.photo.url }}" alt="product image">
                    </div>
                    <div class="peoplephoto">{{ photo }}</div>
                    <div class="peoplename">{{ product.name }}</div>
                    <div class="peopledesignation">{{ product.price }}</div>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
    {% endblock %}
</body>

</html>
```
## CONTACTUS.HTML:
```
{% extends "companyapp/base.html" %}

{% block content %}
<div class="contactuscontent">
    <h1>CONTACT US</h1>
    <div class="contactustext">
        <h2>Aazhiya(General Contact Manager)</h2>
        <h2>Arihant Silicon Products Private Limited</h2>
        <h2>Arihant Silicon Products India Contact Information,Email Address,Main Office Location Including
headquaters address,office phone number,customer support helpline number and email id is available here 
with company bio data,network presence,as well as service locations </h2>
        <h2>Chennai,India - 6000051</h2>
        <h2>contact number - 8362891743</h2>
        <h2>Email address - Siliconcompanyrj@gmail.com</h2>
    </div>
</div>
{% endblock %}
```
## output

![output](./static/img/output1.jpg)

![output](./static/img/output2.jpg)

![output](./static/img/output3.jpg)

![output](./static/img/output4.jpg)

## VALIDATION CODE REPORT:

![output](./static/img/output1.jpg)

![output](./static/img/output2.jpg)

![output](./static/img/output3.jpg)

![output](./static/img/output4.jpg)

## RESULT:

Thus a website is designed for the chip manufacturing company and is hosted in the URL http://kayalvizhi.student.saveetha.in:8000/. HTML code is validated.
