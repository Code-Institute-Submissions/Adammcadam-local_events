# Local Events

## What does it do and what need does it fulfil?
This project uses skills gained to build a Flask website that uses a MongoDB backend. It is for people in my local area to view local upcoming events and bands. 
Add their bands and even their venues to website for others to view.
The project itself can be viewed here [https://local-events-flask-mongo.herokuapp.com/](https://local-events-flask-mongo.herokuapp.com/)

## Project Functionality
The website is fully responsive and uses Mongo DB to hold bands and venue collections. The user is able to create, edit, update and delete their own bands and/or venues.

The home page shows all bands in two categories. Most viewed and all the most recent or upcoming events for ease of use for the user.

The bands page has pagination which runs through the db to avoid long load times on the page.

Each band and venue can be clicked onto and will only that specific band or venue

All users to the site can currently create, edit, update and delete all bands and venues.

## Future Features

To improve the user experience more I would like to add the ability to see venues on a map. Using google maps API 

> Add the ability for files to be used instead of URLs for logo's

> The ability for bands to upload songs.

> The ability for bands to add their merch stores to their cards

The following technologies were used in the design and build of this project.

#### [Python](https://www.python.org/)
- Python was used to create all the logic behind the application

#### [MongoDB](https://www.mongodb.com/)
- MongoDB was used to store all the data in collections

#### [Flask](http://flask.palletsprojects.com/en/1.1.x/)
- Flask was used as the framework behind the application

#### [HTML5](https://www.w3.org/TR/html/) & [CSS3](https://www.w3.org/Style/CSS/)
- HTML5 & CSS3 were used to create the layout and styling of this site
- Code validators were used to check for errors with the [HTML](https://validator.w3.org/) and [CSS](https://jigsaw.w3.org/css-validator/)

#### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- Javascript and the selected external libraries have been used throughout this site.
- Mainly [JQuery](https://jquery.com/) for the datetimepicker

#### [AWS Cloud9](https://aws.amazon.com/cloud9/)
- Cloud9 IDE editor used to write the HTML, CSS and JavaScript.

#### [Adobe Photoshop CC](https://www.photoshop.com/)
- Photoshop was used to create and edit the sites favicon and logo.

#### [Git & GitHub](https://github.com/)
- Git used for version control. GitHub used as a remote repository and the hosting of this site.

#### [Heroku](https://www.heroku.com)
- Heroku used as a remote repository and the hosting of this site.

## Testing

My tests were done to check the pages loaded correctly and the logic ran correctly. You find these tests in test.py

The responsiveness and correct displaying of all elements has been tested on a number of devices, browsers, and resolutions. Chrome, Firefox, Opera, Safari, Edge, and IE all display without issue.

The following physical devices tested with no issues found.
- Windows desktop HD & UHD
- Google Pixel 2
- Apple iPad Pro
- Apple MacBook Air

## Deployment 

The site was developed using the cloud9 IDE and uses git for version control which is then pushed to GitHub and Heroku. The site is hosted on GitHub Pages and deployed there from the master branch on GitHub. There is no difference between the development version of this site, and the final version hosted on GitHub Pages.

To deploy this project, I took the following initial steps:

From my GitHub page I clicked on 'Repositories' and selected the required repository, in this case 'phasergame'

I then clicked on the 'settings' option, located on the top horizontal menu bar

Next, I scrolled down the page to the GitHub Pages section and located the dropdown box under 'Source'

From there I selected the 'master branch'

GitHub takes you back to the top of the page to allow you to rename the repository if desired. I kept it the same.

These steps resulted in the finished site being deployed at https://adammcadam.github.io/local_events/.

Every subsequent push to GitHub on the master branch updates the deployed site to match.

A MongoDB database is used and setup inside Heroku. 

A Procfile has also been used to help Heroku know what commands are run by the apps dyno's.
