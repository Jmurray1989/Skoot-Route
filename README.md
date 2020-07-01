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

To stop the website from having loads of white as the background and to create a better visual experience for the user i added a subtle gradient effect to the route pages using white to begin with and then the gradient effect working its way into orange.
