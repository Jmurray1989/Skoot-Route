# Skoot-Route

<hr>

### Code Institute / Data Centric Development Milestone Project

Tasked to create a website combining knowledge from the Python Fundamentals, Practical Python & the Data Centric Development modules on the Code Institute course.

## Introducing you to
<p align="center">
  <img width="400" height="350" src="static/images/skoot-route-logo.png">
</p>


#### The Idea:

Having previously created a scooter shop website for my MS2 and briefly touching on Skoot Routes within that, I decided for this project that i was going to take that idea and build on it. The site is based around Skoot routes that people can use to find unknown places around major cities while on holidays or just travelling around there own town on their scooters.

I built this website using all the content we learned on the course and more using features like EmailJS, Javascript, & Flask features.
 
#### The goal of this website is to:

Is to give people the freedom to explore unknown or popular places that people like taking their scooters for a ride and by allowing them to share it with others.
They can do this by the way of sharing their route links from google maps and by giving a brief description as to why they love it so much and hopefully encourage people to explore the unknown or hidden gems that they have found.

## User Experience

<hr>

### User Stories:

1. As a user I want to easily navigate the site across all pages.

2. As a user I want to be able to have the ability to view pre-made (public) skoot routes.

3. As a user I want to sign up to a newsletter so i am kept up to date with the latest routes

4. As a user i want to be able to create, edit & delete my own routes.

5. As a user i want to be able to share my routes in a public place for others to enjoy.

6. As a user I want to view the site from any device (mobile, tablet, desktop).

## Design

<img src="https://github.com/Jmurray1989/Skoot-Route/blob/master/static/images/device-mockup.png">

The website contains the key CRUD functionality and uses a document based database MongoDB.
The user functionality is created using Flask, HTML & CSS. The project utilises the Bootstrap framework to ensure Mobile first fully responsive design. When considering the design elements for this project, a modern/vivid color scheme is what came to mind first and it includes all the main points of a website such as the navigation bar and Footer elements.

The project is version controlled via Git & Github and is deployed via Heroku. All environment variables are held in a git ignored file and held secret to ensure the project meets standard security protocols.

### Font:

The project has a main font of 'Maven Pro' which was imported via css from Google Fonts, with the backup font being set to a default of 'Sans-serif'. The clean feel gave the website a modern look but also making each character very easy to read for the user.

### Logo:

The main idea of this logo was taken from this [site](https://skoot.ie/) and by using photoshop i was able to add in a few of my own elements to help me create my desired logo.  Its a very clean and simple logo but by incorporating the two O's to the body of the scooter made it really stand out and grab attention.

My Logo can be seen in the navbar of my site and is used as 'Home' button across all pages.

##### As seen here:

<img src="https://github.com/Jmurray1989/Skoot-Route/blob/master/static/images/navbar.png">

### Color Scheme:

To help me choose my color scheme i used [Adobe Color Wheel](https://color.adobe.com/create).

This process took a long time during the wireframe stage. In the end i decided on this color scheme as it is quite vivid bold and dark all at the same time. The bright orange gives it a very vivid feel and helps to highlight important points against the black backdrop and at the same time it gives the website a dark and bold feel. I also used white with a mix of an orange gradient to just break the page up from being a standard white background.

Three primary colors were chosen when creating this project:

- ![#000000](https://placehold.it/15/000000/000000?text=+) `#000000` 
- ![#fd9a05](https://placehold.it/15/fd9a05/000000?text=+) `#fd9a05` 
- ![#ffffff](https://placehold.it/15/ffffff/000000?text=+) `#ffffff`

The three colours are featured heavily across the site. 

The navbar is colored in ![#000000](https://placehold.it/15/000000/000000?text=+) `#000000`, which offered a dark background to the logo and the nav-link elements
of ![#ffffff](https://placehold.it/15/ffffff/000000?text=+) `#ffffff` and ![#fd9a05](https://placehold.it/15/fd9a05/000000?text=+) `#fd9a05`.

The call to action buttons utilised the same navbar coloring of, ![#000000](https://placehold.it/15/000000/000000?text=+) `#000000`, as their borders.
When not active, focused or hovered the main background color was set to, ![#fd9a05](https://placehold.it/15/fd9a05/000000?text=+) `#fd9a05` with the font inside being set to black. When an action or hover was captured on the button, it would turn the font to white, to show the user that this element is interact-able and something will happen when pressed.

To give the website a more colorful feel & to create a better visual experience for the user i added a subtle gradient effect to the route pages using white to begin with and then adding the gradient effect working its way into orange.

### Wireframes:

To build my wireframes i used [Balsamiq](https://balsamiq.com/).

All wireframes created for this project can be found [Here]("/").

Each element was structurally planned out at this stage and even during the physical build of the application there was not much deviation from the original planning. Each page was rendered as a wireframe in all viewport sizes to show the difference between them and to show how the elements would react to differing viewport sizes.

#### Base Template:

The base.html parent template contains all the default components for each page.
A head element containing the meta data and all relevant links to Title, Logo, Favicon, Frameworks, custom CSS & JS files for the application.
A navbar containing the logo and navigation links. The navbar also contains a sign up modal which can be accessed across all pages. 
Our footer which contains our social icons, all this can be achieved by using jinja templating language.

{% block content %}
{& endblock %}

* Base Template Wireframe

<img height="300" width="300" src="">

#### All other wireframe examples for different viewports can be found below:-

* Desktop

<img height="300" width="300" src="">

* Mobile

<img height="300" width="300" src="">

## Features

<hr>

* This is a summary of the features i have put in place on my project but also the features i hope to add in the future.

* All pages on the website follow the same principle with a fixed navbar, main image, a header, a footer with links to all of our social media platforms.

<strong>The project has several key features:</strong>

One of the main features is the CRUD functionality which is vital to this projects setup.

Create: The user being able to create a new skoot route via the create route form.

Read: Is implemented on the site showing the user the public routes that themselves & others have created.

Update: Present for a user to update a route and push it back to the database.

Delete: Present for a user in that they can delete a route from the site and the database.

In order to test the CRUD functionality operated correctly i created, edited & updated over 50 routes to make sure everything operated correctly on the site and also that the database updated accordingly. I also had family and friends and even my mentor Gerard Mc Bride set up their own routes and make sure they found no issues while doing so.

### Navbar

The navbar is featured on all pages and is used to navigate the site.

 The navbar links are on the right side of the navbar. I have 6 links in total:-
- Home
- About
- Skoot Routes 
- Public Routes
- Mobile
- Sign Up (which is linked to a modal)

Intuitive navigation fixed to the top of the the page that resizes for mobile devices with the hamburger icon. When pressed it expands to show the other navigable pages. On desktop i have used a hover function that will show the user which navpage they are highlighting over and to show the user that this is interact-able and something will happen when clicked.

### Buttons

###### Sign Up

* On the homescreen and across all pages i use a sign up button which is linked to a modal which allows the user to sign up to The Green-Machine newsletter.

<p align="center">
  <img width="175" height="55" src="https://github.com/Jmurray1989/Skoot-Route/blob/master/static/images/sign-up.png">
</p>

###### Lets Skoot!

* When the user clicks on this button of their desired route it will bring them to google maps which will show them the route they can take on their scooter around dublin landmarks and sites.

<p align="center">
  <img width="175" height="55" src="https://github.com/Jmurray1989/Skoot-Route/blob/master/static/images/lets-skoot.png">
</p>

###### Add Your Route +

* When the user clicks on this button it will allow them to add their own route to the public routes page on the website and also adds it into the database.

<p align="center">
  <img width="175" height="55" src="https://github.com/Jmurray1989/Skoot-Route/blob/master/static/images/add-route.png">
</p>

###### Edit & Delete

* Allows a user to edit or delete a route from the site and also the database.

<p align="center">
  <img width="175" height="55" src="https://github.com/Jmurray1989/Skoot-Route/blob/master/static/images/edit-delete.png">
</p>

### Footer Divider

* The footer divider is featured on the mobile page of the website and it contains two clickable logos which will take you to external sites to download our mobile app.

<p align="center">
  <img width="175" height="55" src="https://github.com/Jmurray1989/Skoot-Route/blob/master/static/images/apps.png">
</p>

1. [Google Play Store](https://play.google.com/store)
2. [Appstore](https://www.apple.com/ios/app-store/)

### Footer

* The footer is featured on all pages and contains clickable icons that will take you to each of our social media platforms.

1. [Facebook](https://www.facebook.com/)
2. [Twitter](https://twitter.com/)
3. [Instagram](https://www.instagram.com/)
4. [Youtube](https://www.youtube.com/)

### Future Plans

In an ideal world, there are a couple items that I would've loved to have completed as well, but just didn't have the time or knowledge just yet as to how to implement these features.

- To allow the user to create an account so that the routes they create are only editable by themself and nobody else.

- Introduce a live version of google maps so that the map displays the route in each card instead of just an outside link.

- To add user reviews to each of the routes added.

- To add a view counter to each individual route so the user can see how many people have viewed their route.

- Search functionality to search by multiple features such as length, Location, route type etc.

- In the sign up newsletter modal, I would like to have the social icons fully functioning so that the user could sign up to the newsletter by signing up through their social media platforms.

## Technologies Used:

<hr>

The Technologies I used to build this project are as follows,

[HTML5](https://en.wikipedia.org/wiki/HTML5)

* Buiding the foundation of my project.

[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

* For custom styling of my project.

[Javascript](https://www.javascript.com/)

* To implement features and user input for the website.

[Python](https://www.python.org/)

* Used as back end programming language.

[Flask](https://flask.palletsprojects.com/en/1.1.x/)

* Used as a microframework.

[Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

* Used for templating with Flask.

[JQuery](https://jquery.com/)

* The project uses JQuery to simplify DOM manipulation.

[Bootstrap](https://getbootstrap.com/)

* The framework i used to achieve the album card layout, my navbar, gallery section & contact form.

[Font Awesome](https://fontawesome.com/)

* Used for all icons within the footer and buttons.

[Google Fonts](https://fonts.google.com/)

* Used for the typography of the project.

[EmailJS](https://www.emailjs.com/)

* Used to send an auto-reply mail on user sign up to newsletter

[GitHub](https://github.com/)

* Used to store & manage my code.

[GitPod](https://www.gitpod.io/)

* My IDE of choice to develop my project.

[Heroku](https://id.heroku.com/login)

* A cloud platform enabling deployment for this CRUD application.
    
### Tools Used:

[Tinypng](https://tinypng.com/) 

* Used to compress images without affecting image quality and to achieve faster image load times.

[Balsamiq](https://balsamiq.com/)

* Used for the creation of my pre-build wireframes showing the main elements and differences in size of same through small to large screen sizes.

[Favicon Generator](https://www.favicon-generator.org/)

* Used to create favicon from custom Logo I created for the project.

[Adobe Color Wheel](https://color.adobe.com/create)

* Helped achieve color scheme.

[W3C Mark-up Validation](https://validator.w3.org/) and [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) 

* where used to check the validity of the project's code. 

[JSHint](https://jshint.com/)

* Using JSHint to validate the project's Javascript

[PEP 8 Online Validator](http://pep8online.com/) 

* To check my python code to be consistent with PEP8 requirements.

[Autoprefixer CSS](https://autoprefixer.github.io/)

* Used to check for possible webkits required in the applications stylesheet ensuring Cross-browser support.

[MongoDB](https://www.mongodb.com/)

* Non-relational database used.

[Google Chrome DevTools](https://bit.ly/3giMhjy)

* Used to test the application's functionality and the CSS visualisation, as well as the correct style properties to override Bootstraps default settings.

[Adobe Photoshop](https://www.adobe.com/ie/products/photoshop.html)

* Used to crop, re-size, editing and creation of images.

## Testing

<hr>

The website has been tested across multiple browsers and on mobile devices to ensure compatibility and responsiveness of the site. Continuous testing for this application was carried out throughout the entire lifetime of the build. This was achieved through Chrome Devtools and it was used constantly to test on as many devices as possible from Android to Apple phones & tablet dimensions, and also larger device sizes. The website was tested constantly throughout the build at home using devices i had on hand such as a Samsung Galaxy S10 & S8, a Xiaomi Redmi Pro 8 and for the tablet size i used an Amazon Fire HD 8.

If a bug arose during testing it was dealt with during the build of the project. The build and the fix where then pushed to the repository for the latest changes to take affect on the deployed application via automatic build & deploy function set up in Heroku.

### Desktop

- Chrome
- Mozilla Firefox
- Microsoft Edge
- IE
- Opera

### Mobile Devices

- Xiaomi Redmi Pro 8
- Galaxy S10, S8
- iPad + iPad Pro (using Chrome devtools)
- Amazon Fire Hd 8

I used [W3C Mark-up Validation](https://validator.w3.org/) and [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) to validate my html and css code. Unfortunately the W3C Validator for HTML does not understand the Jinja templating syntax, so it therefore shows a lot of errors with regards to {{ variables }}, {% for %} {% endfor %}, etc. Aside from the Jinja warnings and errors, all of the remaining code is perfectly validating 


I used JSHint to validate the project's Javascript file which i configured to accept jQuery & ES6 New JS features, It returned 0 warnings. 

I used PEP8 online to make sure my Python files are compliant to current standards.

### Known Issues



As Safari is no longer developed for Windows I used a site known as [LambdaTest](https://www.lambdatest.com/) to run my code in a live view for mac and safari software. It returned a few errors however as this is not official software i cannot be sure the results given are accurate. When I tested my project through chrome and other browsers on this site it showed me errors which i do not have on these browsers when ran locally.

### User Story Testing

1. As a user I want to easily navigate the site across all pages.

- This was made possible by the navbar which features links to different pages and also the buttons placed around as shortcuts to different parts of the site. 

2. As a user I want to be able to have the ability to view pre-made (public) skoot routes.

- To view these you can either go to the skoot routes page which are pre made routes by us for you or go to the public pages section where other users have created routes for use and viewing.

3. As a user I want to sign up to a newsletter so i am kept up to date with the latest routes.

- Located in the navbar is a 'Sign-Up' button which will allow the user to subscribe to our newsletter and they will receive a notification email on receipt of their request.

4. As a user i want to be able to create, edit & delete my own routes.

- This feature was added to the public routes page where the user can add, edit or delete the routes they created.

5. As a user i want to be able to share my routes in a public place for others to enjoy.

- These can be seen in the public routes section of the website.

6. As a user I want to view the site from any device (mobile, tablet, desktop).

- The website was developed with mobile first responsive design which will scale up for larger devices.

## Deployment

### Remote Deployment

This site is currently deployed on Heroku using the master branch on GitHub. To implement this project on Heroku, the following steps were taken:

1. Create a requirements.txt file so Heroku can install the required dependencies to run the app.
sudo pip3 freeze --local > requirements.txt

2. Create a Procfile to tell Heroku what type of application is being deployed, and how to run it.
echo web: python run.py > Procfile

3. Sign up for a free Heroku account, create your project app, and click the Deploy tab, at which point you can Connect GitHub as the Deployment Method, and select Enable Automatic Deployment.

4. In the Heroku Settings tab, click on the Reveal Config Vars button to configure environmental variables as follows:

IP : 0.0.0.0
PORT : 5000
MONGO_URI : <link to your Mongo DB>
MONGO_DBNAME : <Mongo DB name>

5. Once the above was done, the app was deployed via this link: "https://skoot-route.herokuapp.com/". 

My repository can be found here:

* https://github.com/Jmurray1989/Skoot-Route

### Clone Repo

To clone the repository:

1. Select the Repository from the Github Dashboard.

2. Click on the "Clone or download" dropdown button which is located beside the Gitpod button to the right.

3. Click on the "clipboard icon" to the right to copy the web URL.

4. Open your preferred Integrated Development Environment (IDE) and navigate to the terminal window.

5. Change the directory to where you want to clone the repository too.

6. Paste the Git URL copied from above and click "Ok". .

## Credits

<hr>

### Content

- The modal & the footer divider used was sourced from this [Site](https://mdbootstrap.com/).

- The Skoot Route Idea was based on the design from this site [Here](https://skoot.ie/pages/dublin-skoot-routes). 

- The use of the CRUD functionality was assisted by the course content from the Code Institute Course.

- How to set up enviroment variables and store mongo db username and passwords in env.py file and put into .gitignore was assisted by a blogpost from CI in Slack.

- Creating custom 404 & 500 pages from Flask Documentation.

### Code

For assistance i have used the following sites:-

* [Stack Overflow](https://stackoverflow.com/)
* [CSS Tricks](https://css-tricks.com/)
* [W3Schools](https://www.w3schools.com/)

### Media

- The photos used in this site were obtained from google images searches. As it is for educational purpose and not for profit i was made aware that it may not be neccessary to ask for permission.

### Acknowledgements

- I would like to thank those in Slack, the Tutor Support and my Mentor Gerard McBride for assisting with me with any queries i had during this project. You and all the advice have really helped me during the course of this build.

Disclaimer: This project and its content were created for educational purposes only as part of the Code Institute Course for Milestone 3 Grading.

