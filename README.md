# Cityfur - Dog Day Care Guest Management System

## Introduction

Code Institute - Portfilio Project 3 - Django Full-Stack Application<br>
<br>
This application is developed for the real world use case in a dog day care center in Cologne, Germany.<br>
<br>
On a weekday bases, the day care center hosts up to 60 dogs simultaneously and makes sure that all needs of the guests are met.<br>
The application helps with the daily tracking of dogs coming in the morning and leaving in the afternoon. It also helps with keeping all relevant information on display. Like times for applying medication or feeding schedules, and pickup by different individuals that are not the owner. It also includes a system for daily reports where dogs can be tagged to reports, if the report is about them. 
<br>

[The deployed version can be found here!](https://ci-pp4-cityfur-4506435722fe.herokuapp.com/)
<br>

![Website Mockups](/documentation/images/mockups/website-mockups.png)
<br>


## Table of Contents

* [Introduction](#introduction)

* [Use Case](#use-case)
* [User Experience](#user-experience)
  * [Design](#design)
    * [Color Scheme](#color-scheme)
    * [Imagery](#imagery)
    * [Typography](#typography)
    * [Mockups](#mockups)
  * [Features](#features)
    * [UX/UI](#ux/ui)
    * [CRUD](#crud)
    * [Future Features](#future-features)
* [Agile Project Management](#agile-project-management)
  * [Milestones](#milestones)
  * [User Stories](#user-stories)
* [Development](#development)
  * [Database](#database)
  * [Technologies Used](#technologies-used)
    * [Frameworks](#frameworks)
    * [Languages](#languages)
    * [Modules & Libraries](#mudules--libraries)
    * [Programs & Tools](#programs--tools)
  * [Deployment](#deployment)
    * [Version Control](#version-control)
    * [Cloudinary](#cloudinary)
    * [Heroku Deployment](#heroku-deployment)
  * [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Manual Testing](#manual-testing)
    * [Possible Improvements](#possible-improvments)
    * [Fixed Bugs](#fixed-bugs)
    * [Known Unfixes Bugs](#known-unfixed-bugs)
* [Credits](#credits)
  * [Acknowledgements](#acknowledgements)


## Use Case

This application is developed for the real world use case in a dog day care center in Cologne, Germany.<br>
<br>
On a weekday bases, the day care center hosts up to 60 dogs simultaneously and makes sure that all needs of the guests are met.<br>
The application helps with the daily tracking of dogs coming in the morning and leaving in the afternoon. It also helps with keeping all relevant information on display. Like times for applying medication or feeding schedules, and pickup by different individuals that are not the owner. It also includes a system for daily reports where dogs can be tagged to reports, if the report is about them.<br>

<br>
Attached below is a picture of the currently used tracking system, based on a calendar book.<br>
<br>
In this system, every day has a separate page that is divided into several fields:
- Guest count of the day
- Male guests of the day
- Female guests of the day
- Guests coming as couples
- Reports of the day
<br>
When a Guest checks in, the name of the guests is written down in the according field. Once the guest checks out in the evening, the name is crossed out.<br>
Annotations do better distinguish guest are written down behind the name. Used are for example GR for Golden Retriever behind Luke or D for Dalmatiner behind Juna.<br>
<br>
Information like a different person to pick up a guest or other important information are also written down on the bottom in the report area.<br>
<br>

![Original Tracking System](/documentation/images/tracking-system-s.webp)


When finally rolled out, with the help of this newly developed system, the employees at the facility are helped with:

- Keeping track of guests present that day
- Knowing which guests have checked-out and how many are still left at the facility
- Remembering times for applying individual medication
- Remembering Times for individual feeding schedule
- Saving information about pickup from different individuals
- Recognizing guests that are new by having images of every guest in its profile
- Getting an overview over important information about every guest in its individual profile
- Better track situations that happened and were noted as a report with related guests tagged
- Creating a better shift change with all relevant information handed over in a structured way


## User Experience

### Design

#### Color Scheme

The color scheme for this project is very simple and primarily consists of four colores. Two darker blue tones as the main colors for navigation elements. Light blue for confirmation buttons and red as a cancle/delete button.<br>
<br>

![Color Scheme](/documentation/images/color-scheme.png)

#### Imagery

Images used as content for test purposes were created with ChatGPT and DALL-E 3.<br>
The favicon was created by using a FontAwesome icon and a blue background, edited with Affinity Designer 2.<br>

#### Typography

For this project, no special typography was used.<br>
The font is the standard font of the used browser.<br>
Only different font-size and boldness were used.<br>

#### Mockups

For this project, I used mockups created with Figma instead of wireframes to better go into details when laying out the designs.
During the development process, the mockups were constantly updated according to new findings.

<details>
<summary>Mobile Nav</summary>
<br>
This is the navigation for the mobile version of the application.<br>
<br>

![Mobile Nav Mockup](/documentation/images/mockups/0-mobile-nav.png)
</details>


<details>
<summary>Guests List</summary>
<br>
In this overview, all checked-in and already checked-out guests of the day are listed.<br>
The day can be selected in the top menu bar and all profiles on the page can be searched.<br>
On smaller screens, the search bar disappears and is exchanged by a search icon. When clicking the icon, the search bar shows up.<br>
<br>
To check-in a new guest, users can click on the blue "Check-In" button on the bottom.<br>
The last element of the page is the gender selector that gives the option to select all guests checked-in and already checked-out that day, only female and only male guests.<br>
<br>

![Guests List Mockup](/documentation/images/mockups/1-guests-list.png)

Each small profile listed can be clicked on, and the following information are shown:

- Possible medication times
- Possible feeding times
- Different person, then the owner, to pick up the guest
- An icon to indicate that the guest was tagged in a report that day


When clicked on the small profile, a dropdown menu opens with the following options:

- Undo check-in/check-out
- Open guest file
- Read report if guest was mentiones in one on selected day
- Check-out guest if the guest is checked-in
<br>

![Guest Profile Widget Mockup](/documentation/images/mockups/1-1-guest-profile-widget.png)
</details>


<details>
<summary>Guest Check-In</summary>
<br>
When clicking on the "Check-In" button on the guest list (previous chapter), a list of all not checked-in guest of the selected date show up.<br>
Each profile can be clicked, and the check-in button can be clicked. After the confirmation modal, the guest will be checked-in for the selected date.<br>
<br>
When clicking on the "Close Check-In" button, the view will switch to the guest list for the selected date.<br>
<br>
The date picker and search field are working as described in the chapter above.<br>
The gender selector on the bottom is also working as already described.<br>
<br>

![Guest Check-In Mockup](/documentation/images/mockups/2-guest-check-in.png)
</details>


<details>
<summary>All Guests</summary>
<br>

This page shows an overview of all guests with a profile in the database.<br>
Every profile shows the basic information like name, name-addon, gender, medication and food times.<br>
The details page for each profile can be opened by using the dropdown menu.<br>
<br>
On this page, the user is able to use the search and filter all profiles by gender.<br>
When using the date picker, the application will load the guest list for the selected date.<br>
<br>

![All Guests Mockup](/documentation/images/mockups/3-all-guests.png)
</details>


<details>
<summary>Add/Edit Guest</summary>
<br>

Here the user has the chance to add new guests to the system. The same layout is used to change a profile of a guest.<br>
<br>
Information for each guest are:
- First name
- Last name (Family name of the owner)
- Name-addon (If a guest with the same first name already exists, to better distinguish the guests)
- Gender
- Image
- Date of birth
- Information (Anything worth noting that is important and not covered by a dedicated field)
- Food time
- Medication time
- Owner (Choose from list of owners. These are at this version of the app created in the admin backend and only for demo purposes only)
<br>

![Add/Edit Guest Mockup](/documentation/images/mockups/4-add-edit-guest.png)
</details>


<details>
<summary>Guest Details</summary>
<br>

This is the profile overview for each guest. Here all information are listed.<br>
On the bottom of the page, all reports are listed, that the guest has been tagged on.<br>
The user has the chance to edit or delete the profile or go to a specific report the guest was tagged on.<br>
<br>

![Guest Details Mockup](/documentation/images/mockups/5-guest-details.png)
</details>


<details>
<summary>Reports List</summary>
<br>

This page shows a list of all reports written on the selected date.<br>
All reports include a text, a link to go to the report's details page, and a list of all guests tagged on the report, if any were tagged.<br>
<br>

![Reports List Mockup](/documentation/images/mockups/6-reports-list.png)
</details>


<details>
<summary>All Reports</summary>
<br>

On this page, a list of all reports written and present in the database is shown.<br>
The reports are sorted by date, with the newest report on the top.<br>
When selecting a date in the top, the page with the reports for the selected date loads.<br>
<br>

![All Reports Mockup](/documentation/images/mockups/7-all-reports.png)
</details>


<details>
<summary>Report Details</summary>
<br>

A page dedicated to the details of a selected report.<br>
All report details are listed and the user has the options to edit or delete the report.<br>
When deleting the report, a modal opens where the user has to confirm the deletion.<br>
<br>

![Report Details Mockup](/documentation/images/mockups/8-report-details.png)
</details>


<details>
<summary>Add/Edit Report</summary>
<br>

On this page a report can be added, or a selected report can be edited.<br>
Input fields are for the report date, report text and a selection list where the user can select the guests to tag to the report.<br>
<br>

![Add/Edit Report Mockup](/documentation/images/mockups/9-add-edit-report.png)
</details>


### Features

#### UX/UI

In this section, I point out some of the more advanced or useful features of this application.<br>
<br>

<details>
<summary>Search</summary>
<br>

![Search](/documentation/images/features/search.png)
<br>
<br>
The search enables users to search for a specific guest from one of the overview lists. The results immediately reload with every key pressed.
<br>
The search is a special topic in this application. It is created by marking all not matching results as hidden using Bootstrap. All matching results are shown.<br>
<br>
To avoid unnecessary loading times and giving instant feedback, the search was created this way and not by doing a separated get request with every search.<br>
This method is only useful with a limited amount of profiles in the database. In the case of this application and its real world use, this is doable, since only a maximum of around 100 guests will be in the database simultaneously.<br>
</details>

<details>
<summary>Gender Filter</summary>
<br>

![Gender Filter](/documentation/images/features/gender-filter.png)
<br>
<br>
The gender filter enables the user to filter guest lists and only show male, female or all guests.<br>
Similar to the search, the gender selector uses bootstrap classes to show only guests matching the selected filter.<br>
</details>

<details>
<summary>Profile Resize & Dropout</summary>
<br>

![Profile Resize & Dropout](/documentation/images/features/profile-resize-dropout.png)
<br>
<br>
When clicking on a small profile, the profile extends and shows a dropout menu for more options.<br>
If a different profile was already opened, this first one gets small again and the new one opens.<br>
</details>

<details>
<summary>Profile Alerts</summary>
<br>

![Alerts Small Profile](/documentation/images/features/alerts-small.png)
<br>
<br>
Profiles can show icons as alerts for important information. This information can be about needed medication, feeding, different person picking up the guest, or indicating that the guest was tagged on a report of the selected day.<br>
Depending on the status of the profile, the icons and information is displayed differently. Like seen on a small profile above and an opened profile down below.<br>
<br>

![Alerts Large Profile](/documentation/images/features/alerts-large.png)
</details>

<details>
<summary>Confirmation Modals</summary>
<br>

![Confirmation Modal](/documentation/images/features/confirmation-modal.png)
<br>
<br>
Every important action has to be confirmed by clicking a button on an opening modal.<br>
Actions that have to be confirmed with a modal:
- Check-In
- Check-Out
- Undo Check-In
- Undo Check-Out
- Delete Guest Profile
- Delete Report
</details>

<details>
<summary>Report Tagging System</summary>
<br>

![Report Tagging System](/documentation/images/features/report-tagging-system.png)
<br>
<br>
On every report, multiple guest can be tagged. The reports then show up on the profile of the tagged guest.<br>
When a guest profile is deleted from the database, the tag in the report gets automatically deleted too.<br>
</details>




#### CRUD

Full CRUD functionality is implemented with the following features:

**Guests**
- Create Guest Profile
- Read Guest Profile
- Update Guest Profile
- Delete Guest Profile
<br>

**Reports**
- Create Report
- Read Report
- Update Report
- Delete Report
<br>

**Presences**
- Create - Check-In Guest
- Read - See list of checked-in guests
- Update - Guest Check-out, undo check-in or undo check-out
- Delete - Undo guest check-in
<br>


#### Future Features

Since the application is planned to be used in a real facility in Cologne, Germany, the following features are already planned to be developed.

**Customer Management System**<br>
The already existing model for customers is planned to be extended to a full-fledged customer management system.<br>
Users will be able to add new customers to the database, change their information and assign guests to them.<br>
<br>

**Accounting System**<br>
Based on the customer management system is the planned accounting system. This will help with managing subscriptions and different subscription plans. With different subscription plans, guest are allowed to come in one, two, three, four or five days a week. Beside choosing a subscription tier, customers can book additional days for bringing their dogs. For example, if a customer has a subscription to bring its dog two days a week, but as an exception needs to bring in the dog for one additional day in a week.<br>
<br>

**Allergies Alert**<br>
Similar to the alerts for medication or feeding, an alert for allergies is planned. This alert will indicate, that a guest has allergies and more information about the exact allergy is to be found on the profile details page.<br>
<br>

**To-Do Lists**<br>
This will be a list of to does for the employees. Possible to does are mowing the lawn, fixing a fence or buying needed materials.<br>
<br>

**Shopping Lists**<br>
This will be a list that can be filled with needed material, that needs to get bought.<br>
<br>


## Agile Project Management

This project was developed using an agile approach for planning and tracking the development process. The project was separated into several milestones, each containing one or up to eight separate user stories, tasks, features or bugs, each labeled with the MoSCoW methodology. Due to the low complexity of the project, no epics were used to improve workflow.<br>

<br>
During the process of development, the kanban board and backlog, its user stories, tasks, bugs and milestones were constantly adapting to new findings and changing requirements. Feature request have been modified, added or the priority were changed.<br>


### Milestones

This project was structured in seven milestones with one or multiple user stories, tasks, features or bugs.

- [Basic Project Setup](https://github.com/DennisSchenkel/PP4-Cityfur/milestone/1)

- [Guest List And Profiles](https://github.com/DennisSchenkel/PP4-Cityfur/milestone/3)

- [Guests Profiles Management (Add/Change/Delete)](https://github.com/DennisSchenkel/PP4-Cityfur/milestone/8)

- [Report System](https://github.com/DennisSchenkel/PP4-Cityfur/milestone/6)

- [User Management & Authentication](https://github.com/DennisSchenkel/PP4-Cityfur/milestone/2)

- [Final Touch](https://github.com/DennisSchenkel/PP4-Cityfur/milestone/9)

- [The Extra Mile](https://github.com/DennisSchenkel/PP4-Cityfur/milestone/10)


### User Stories

**Basic Project Setup**<br>

- TASK: [Basic project setup](https://github.com/DennisSchenkel/PP4-Cityfur/issues/1)
- TASK: [Create Django admin backend](https://github.com/DennisSchenkel/PP4-Cityfur/issues/2)
- USER STORY: [Navigation with sidebar](https://github.com/DennisSchenkel/PP4-Cityfur/issues/11)
<br>

**Guest List And Profiles**<br>

- USER STORY: [Guests list](https://github.com/DennisSchenkel/PP4-Cityfur/issues/3)
- USER STORY: [Guest profiles](https://github.com/DennisSchenkel/PP4-Cityfur/issues/4)
- USER STORY: [Guest check-in](https://github.com/DennisSchenkel/PP4-Cityfur/issues/5)
- USER STORY: [Filter guests list by gender](https://github.com/DennisSchenkel/PP4-Cityfur/issues/7)
- USER STORY: [Search for guest name](https://github.com/DennisSchenkel/PP4-Cityfur/issues/13)
- USER STORY: [Guest check-out](https://github.com/DennisSchenkel/PP4-Cityfur/issues/14)
- USER STORY: [Guest allergies](https://github.com/DennisSchenkel/PP4-Cityfur/issues/15)
- USER STORY: [Dynamic alerts for food, medication and pickup](https://github.com/DennisSchenkel/PP4-Cityfur/issues/16)
- USER STORY: [Reports mentioned in guest profile](https://github.com/DennisSchenkel/PP4-Cityfur/issues/21)
<br>

**Guests Profiles Management (Add/Change/Delete)**<br>

- USER STORY: [Create new guest profile](https://github.com/DennisSchenkel/PP4-Cityfur/issues/12)
- FEATURE: [Add image upload to guest profile editor](https://github.com/DennisSchenkel/PP4-Cityfur/issues/9)
- FEATURE: [Use placeholder image if no guest image is available](https://github.com/DennisSchenkel/PP4-Cityfur/issues/10)
<br>

**Report System**<br>

- USER STORY: [Write reports](https://github.com/DennisSchenkel/PP4-Cityfur/issues/17)
- USER STORY: [Connect reports and guest for mentions and alerts](https://github.com/DennisSchenkel/PP4-Cityfur/issues/18)
<br>

**User Management & Authentication**<br>

- USER STORY: [User authentication](https://github.com/DennisSchenkel/PP4-Cityfur/issues/6)
<br>

**Final Touch**<br>

- TASK: [Beautidy pages](https://github.com/DennisSchenkel/PP4-Cityfur/issues/19)
- TASK: [403, 404, 405, 500 pages](https://github.com/DennisSchenkel/PP4-Cityfur/issues/20)
- TASK: [Add FavIcon](https://github.com/DennisSchenkel/PP4-Cityfur/issues/24)
- BUG: [Search usable in mobile view](https://github.com/DennisSchenkel/PP4-Cityfur/issues/23)
<br>

**The Extra Mile**<br>

- USER STORY: [Lost of all guests](https://github.com/DennisSchenkel/PP4-Cityfur/issues/22)
- USER STORY: [Intro on landing page](https://github.com/DennisSchenkel/PP4-Cityfur/issues/25)
<br>


## Development

### Database

The following image illustrated the database structure and was made using [dbdiagram](https://dbdiagram.io/home):<br>
<br>

![Database Structure](/documentation/images/database-structure.png)
<br>

**Guest**

This table contains all guest (dogs) that are registered to the dog day care center.<br>
The following fields are worth explaining in more detail:
- First name: The first name can not be empty, and it has to be unique in combination with the name addon.
- Name addon: If a guest with the same first name already exists, a name addon has to be given. This helps to distinguish the guests. In practice the color, breed or size (small, big) of the guest is used.
- Information: This field is for all relevant information about the guest. This could be information about risks, special treatment, or how to handle the guest.
- Food: Check if the guest gets fed during the day.
- Food time 1-3: On which times does the guest get fed.
- Medication: Check if the guest gets medicated during the day.
- Medication time 1-3: On which times does the guest get medicated.
- Customer ID: The owner of the guest is selected from a list of pre-defined customers. More on that later down the line.
- Slug: This field is created automatically and is used to create the domain for the individual's profile.
<br>


**Presence**

When a guest checks in for a day, it is saved in this table with the check-in time.<br>
When checking out in the evening, the check-out time is then saved to the same row.<br>
If the check-out is made undone, only the check-out time is deleted from the row.<br>
If the check-in of the guest for the day is undone, the whole row gets deleted.<br>
<br>
In case the guest is going to be picked up by somebody else than the owner, this can be saved in the field "pickup_name", so the guest is not given to an unauthorized person.<br>
<br>


**Customer**

This table contains the customers, which are the owners of the dogs. When adding a new guest, a customer has to be selected.<br>
Although customers are a required field for creating new guests, at this point they can't be added or edited by users.<br>
The sole purpose is to demonstrate 1:1 and 1:Many relationships in the database.<br>
<br>
Customers can only be added or edited by the admin. For testing purposes, a handful of customers were created.<br>
<br>


**Report**

This table contains reports written for every day. It handles the fields for date and report text. Tagged guests are handled by the GuestReport table.<br>
<br>


**GuestReport** 

This many-to-many table handles all guests tagged to a specific report on a specific date.<br>
This table is automatically generated by Django.<br>
<br>




### Technologies Used

#### Languages

- HTML
- CSS
- JavaScrips
- Python
- Django Template Language

#### Frameworks

The following frameworks have been used.

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [FontAwesome](https://fontawesome.com/)

#### Modules & Libraries

- AllAuth (For user uthentication)
- Black (Code formatter fpr Python)
- Cloudinary (Cloud storage for images)
- Django-Bootstrap-Datapicker-Plus (For datapicker in forms)
- DJ-Database-URL (To configure database URLs)
- Gunicorn (Python WSGI HTTP server for UNIX)
- OS (For operating system interaction)
- Pep8 (Check Python code for PEP8 conventions)
- Pillow (For image processing)
- Psycopg 2 (PostgreSQL adapter for the database)
- Python Dateutility (For better date and time handling)
- Python Slugify (For generating url-slugs)
- Summernote (As a WYSIWYG editor)
- Whitenoise (Middleware for serving static files)

#### Programs & Tools

During the development of this application, the following programs and tools have been used.

- [Visual Studio Code](https://code.visualstudio.com/) (IDE - Integrated Development Environment)
- [Figma](https://www.figma.com/) (Creating Mockups)
- [dbdiagram.io](https://dbdiagram.io/) (Creating database visualization)
- [Heroku](https://www.heroku.com/home) (Deployment of final application)
- [Git](https://git-scm.com/) (Version control)
- [GitHub](https://github.com/) (Used as cloud repository)
- [CI Postgres Database](https://dbs.ci-dbs.net/) (Used for database hosting)
- [CI Python Linter](https://pep8ci.herokuapp.com/) (Python testing)
- [JSHint](https://jshint.com/) (JavaScript testing)
- [W3C HTML Validator](https://validator.w3.org/) (HTML testing)
- [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) (CSS testing)
- [Lighthouse](https://lighthouse-metrics.com/) (Testing of Performance, Accessibility, Best Practices and SEO)
- [Google Chrome Dev Tools](https://developer.chrome.com/) (Working with console and HTML output)
- [Flake8](https://flake8.pycqa.org/en/latest/) (Formatting support for Python)
- [Affinity Design 2](https://affinity.serif.com/de/designer/ ) (Image editing)
- [DALL-E 3](https://openai.com/index/dall-e-3/) (For generating profile images)
- [Cloudinary](https://cloudinary.com/) (As external hosting services for images)
- [Website Mockup Generator
](https://websitemockupgenerator.com/) (For creating a mockup of deployed application)

### Deployment

#### Version Control

This application was developed using Visual Studio Code as the IDE and GitHub for hosting the repository.<br>
<br>
Git was used for version control by using the following comments:

- git add filename - Select the files that should be uploaded and updated to the GitHub repository.
- git commit -m "commit message" - Commenting the commit to better understand the changes in this specific commit.
- git push - Upload the commit to GitHub.


#### Cloudinary

For using Cloudinary as a hosting provider for images, the following steps have to be conducted:
- Create a Cloudinary account.
- Login and visit the Cloudinary user account.
- On the bottom left side, click on the gear symbol.
- On the top left, click on "API Keys".
- Click "Generate New API Key" on the top right.
- Update the Django settings.py with API key.
- Use the API in the Heroku deployment settings like described in the next step.


#### Heroku Deployment

**Step 0: Create requirements.txt**
- Create the requirements.txt (pip freeze > requirements.txt)
- Make sure it contains all needed modules and libraries.
- Modify settings.py
    - Add Heroku to ALLOWED_HOSTS
    - Set DEBUG to "False"
- Create Procfile in root directory with the following content: web: gunicorn PP4_Cityfur.wsgi --log-file -
- Use python manage.py collectstatic in the local IDE terminal to collect all static files

**Step 1: Use Account**
- Create a Heroku account
- Log into the Heroku account

**Step 2: Create New App**
- On the dashboard, click "New" in the upper right corner.
- Select "Create new app"
- Select a name for the application - the name should only contain lowercase letters, numbers, and dashes.
- Choose a region. (Europe as we are in Europe)

**Step 3: Define Deployment Method**
- Select GitHub as deployment method
- Connect GitHub account to Heroku
- Select account and search for repository
- Connect to found repository

**Step 4: Settings**
- Switch to the settings page (Menu in the top)
- Click on "Reveal Config Vars"
- The following Key/Value pairs have been added:
    - CLOUDINARY_URL (Created in chapter before)
    - DB_ENGINE
    - DB_HOST
    - DB_OPTIONS 
    - DB_PASSWORD
    - DB_PORT
    - DB_SSLMODE
    - DB_USER
    - SECRET_KEY
- In the next section, click on "Add buildpack"
- If not already selected, add Python.

**Step 5: Deploy Application**
- Switch to the deploy page (Menu in the top)
- Look under manual deployment
- Select a branch to deploy (Main in my case)
- Click "Deploy Branch"

**Step 6: Use App**
- Heroku will then set up the virtual environment with all packages, modules and libraries needed. (This can take some time)
- When Heroku is done with the deployment, click "View" and start to use the
- Use app
<br>

[The deployed version can be found here!](https://ci-pp4-cityfur-4506435722fe.herokuapp.com/)
<br>


### Testing

#### Validator Testing

<details>
<summary>W3C HTML Validation</summary>
<br>

All tests were conducted by copying the HTML code from the Google Chrome developer's tool and pasting into the [W3C HTML Validator](https://validator.w3.org/).
No errors were found when using the W3C HTML Validator.<br>
On three pages, information were shown about closing tags that have been automatically created by Django and don't have any influence on the pages' behavior.<br>
<br>
To avoid an endless wall of screenshots with passed test, all conducted test and results are listed in the table below:
<br>

![HTML Validation Results](/documentation/images/tests/html-results.png)<br>
<br>
All detailed screenshots are linked below:
<br>

[Reports List](/documentation/images/tests/html-reports-list.png)<br>
[All Reports](/documentation/images/tests/html-reports-all.png)<br>
[Report Details](/documentation/images/tests/html-report-details.png)<br>
[Add Reports](/documentation/images/tests/html-add-report.png)<br>
[Update Report](/documentation/images/tests/html-update-report.png)<br>

[Guests List](/documentation/images/tests/html-guests-list.png)<br>
[All Guests](/documentation/images/tests/html-guests-all.png)<br>
[Guest Details](/documentation/images/tests/html-guest-details.png)<br>
[Add Guest](/documentation/images/tests/html-add-guest.png)<br>
[Update Guest](/documentation/images/tests/html-update-guest.png)<br>

[Landing Page](/documentation/images/tests/html-landingpage.png)<br>
[404 Page](/documentation/images/tests/html-404.png)<br>
</details>


<details>
<summary>Jigsaw CSS Validation</summary>
<br>

No errors were found when using the [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/validator).<br>
<br>
![CSS Validation](/documentation/images/tests/css-validation.png)<br>
</details>


<details>
<summary>JSHint Validator</summary>
<br>

No errors were found when using [JSHint](https://jshint.com).<br>
<br>
To avoid an endless wall of screenshots with passed test, all conducted test and results are listed in the table below:
<br>

![JSHint Results](/documentation/images/tests/jshint-results.png)<br>
<br>
All detailed screenshots are linked below:
<br>

[date_picker_guests.js](/documentation/images/tests/jshint-date-picker-guests.png)<br>
[date_picker_reports.js](/documentation/images/tests/jshint-date-picker-reports.png)<br>
[get_date.js](/documentation/images/tests/jshint-get-date.png)<br>
[guest_list.js](/documentation/images/tests/jshint-guest-list.png)<br>
[guest_search.js](/documentation/images/tests/jshint-guest-search.png)<br>
[redirect.js](/documentation/images/tests/jshint-redirect.png)<br>
[scripts.js](/documentation/images/tests/jshint-scripts.png)<br>
[sidebar_toggle.js](/documentation/images/tests/jshint-sidebar-toggle.png)<br>
</details>


<details>
<summary>CI Python Linter</summary>
<br>

No errors were found when using the [CI Python Linter](https://pep8ci.herokuapp.com/).<br>
<br>

![CI Python Linter](/documentation/images/tests/ci-python-linter.png)<br>
<br>
To avoid an endless wall of screenshots with passed test, all conducted test and results are listed in the table below:
<br>

![CI Python Linter Results](/documentation/images/tests/ci-python-linter-results.png)<br>
</details>


<details>
<summary>Lighthouse</summary>
<br>

This section covers the test done with [Lighthouse](https://lighthouse-metrics.com/).<br>
<br>
**Using the Lighthouse test, multiple issues showed up, leading to low rating for "Best Practices"**<br>
This happens because of two separate factors:<br>
- When showing images hosted on Cloudinary, Cloudinary deploys multiple cookies (15 when testing). Google Chrome will stop supporting 3rd party cookies in the future, what leads to a low scoring when it comes to "Best Practices".
- When loading a page with a form using the Django-Bootstrap-Datapicker-Plus widget (latest version 5.0.5). This widget uses "deprecated APIs" which will be removed from the browser: "DOM Mutation Events, including `DOMSubtreeModified`, `DOMNodeInserted`, `DOMNodeRemoved`, `DOMNodeRemovedFromDocument`, `DOMNodeInsertedIntoDocument`, and `DOMCharacterDataModified`".<br>
<br>
Both issues are, at this point in time, outside my control and finding alternative solutions would take too much time and would lead me to missing the deadline.<br>
<br>

To avoid an endless wall of screenshots with passed test, all conducted test and results are listed in the table below:
<br>

![Lighthouse Results](/documentation/images/tests/lh-results.png)<br>
<br>
All detailed screenshots for desktop results are linked below:
<br>

[Guests List Desktop](/documentation/images/tests/lh-d-guests-list.png)<br>
[All Guests Desktop](/documentation/images/tests/lh-d-all-guests.png)<br>
[Guest Details Desktop](/documentation/images/tests/lh-d-guest-details.png)<br>
[Add Guest Desktop](/documentation/images/tests/lh-d-add-guest.png)<br>
[Update Guest Desktop](/documentation/images/tests/lh-d-update-guest.png)<br>

[Reports List Desktop](/documentation/images/tests/lh-d-reports-list.png)<br>
[All Reports Desktop](/documentation/images/tests/lh-d-all-reports.png)<br>
[Report Details Desktop](/documentation/images/tests/lh-d-report-details.png)<br>
[Add Report Desktop](/documentation/images/tests/lh-d-add-report.png)<br>
[Update Report Desktop](/documentation/images/tests/lh-d-update-report.png)<br>

[Landinpage Desktop](/documentation/images/tests/lh-d-landingpage.png)<br>

<br>
All detailed screenshots for mobile results are linked below:
<br>

[Guests List Mobile](/documentation/images/tests/lh-m-guests-list.png)<br>
[All Guests Mobile](/documentation/images/tests/lh-m-all-guests.png)<br>
[Guest Details Mobile](/documentation/images/tests/lh-m-guest-details.png)<br>
[Add Guest Mobile](/documentation/images/tests/lh-m-add-guest.png)<br>
[Update Guest Mobile](/documentation/images/tests/lh-m-update-guest.png)<br>

[Reports List Mobile](/documentation/images/tests/lh-m-reports-list.png)<br>
[All Reports Mobile](/documentation/images/tests/lh-m-all-reports.png)<br>
[Report Details Mobile](/documentation/images/tests/lh-m-report-details.png)<br>
[Add Report Mobile](/documentation/images/tests/lh-m-add-report.png)<br>
[Update Report Mobile](/documentation/images/tests/lh-m-update-report.png)<br>

[Landinpage Mobile](/documentation/images/tests/lh-m-landingpage.png)<br>
</details>


#### Manual Testing



<details>
<summary>Landing Page</summary>
<br>

| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **Landing Page** |  |  |  |
| --- | --- | --- | --- |
| Open introduction | Opening the introduction modal on the landing page. | When clicking on the "Introduction" button, the modal with the introduction opens. | Pass |
| Closing introduction modal with button | Closing the introduction modal by clicking the "Got it!" button. | When the "Got it!" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing introduction modal clicking outside the modal. | Closing the introduction modal by clicking outside the modal. | When clicked outside, the modal closes and the page is yet again shown like before | Pass |
| Opening login page | Navigate to the login page. | Clicking on the "Login" button, the login page loads. | Pass |
| Open register page | Navigate to the register page. | Clicking in the "Register" button, the register page loads. | Pass |
| Open home page | Navigate to the home page. | Clicking on the dog logo, the home page loads. | Pass |
<br>

| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **Login Page** |  |  |  |
| --- | --- | --- | --- |
| Wrong login credentials | Using wrong login credentials for existing and non-existing accounts | When entering a wrong username or wrong password, the login does not work, and an error is shown  | Pass |
| Login | Correctly working login | When using the correct login credentials for an existing account, the login works and the user is directed to the main page of the application | Pass |
| "Sign up" link | On the login page, a link to the registration page is shown. | When clicking the "sign up" link, the registration page loads. | Pass |
<br>

| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **Register Page** |  |  |  |
| --- | --- | --- | --- |
| Use existing username | A username can only be used once | If the username was already used by a different account, the registration does not work and an error message is shown | Pass |
| Use existing email address | A email address can only be used once | If the email address was already used by a different account, the registration does not work and an error message is shown | Pass |
| Use two different passwords | The password has to be entered two times in the exact same format. | If the two entered passwords are not exactly the same, the registration does not work and an error message is shown. | Pass |
| Use not save password | A password is not allowed to be too common. | If a too common password is used, the registration does not work and an error message is shown. | Pass |
| Registration | Registration working, if everything is entered correctly | When everything is entered correctly, a new account is created and the user is automatically logged in and directed to main page | Pass |
| "Sign in" link | On the registration page, a link to the login page is shown. | When clicking the "sign in" link, the login page loads. | Pass |
</details>

<details>
<summary>Navigation</summary>
<br>

Testing, if the navigation and their items are showing up and are working correctly on each site.<br>

![Nav-Testing](/documentation/images/tests/nav-test.png)
<br>

Testing, if the main navigation is working correctly.<br>

| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **Main Navigation** |  |  |  |
| --- | --- | --- | --- |
| Navigation link to most resent day's guests list | Clicking on "Guests" in the main navigation | When clicking on "Guests" in the main navigation, the page with the list of all guests of the day loads | Pass |
| Navigation link to "All Guests" list | Clicking on "All Guests" in the main navigation | When clicking on "All Guests" in the main navigation, the page with the list of all guests registered to the system loads | Pass |
| Navigation link to "Add Guest" | Clicking on "Add Guest" in the main navigation | Clicking on "Add Guest" in the main navigation | When clicking on "Add Guest" in the main navigation, the page with the form to add a new guest to the system loads | Pass |
| Navigation link to most resent day's reports list | Clicking on "Reports" in the main navigation | When clicking on "Reports" in the main navigation, the page with the list of all reports of the day loads | Pass |
| Navigation link to "All Reports" | Clicking on "All Reports" in the main navigation | When clicking on "All Reports" in the main navigation, the page with the list of all reports in the system loads | Pass |
| Navigation link to "Add Reports" | Clicking on "Add Report" in the main navigation | When clicking on "Add Report" in the main navigation, the page with the form to add a new report loads | Pass |
| Logout | Clicking on "Logout" in the main navigation | When clicking in "Logout" the user gets logged out and redirected to the landing page | Pass |
<br>

Testing, if the navigation using the date picker works correctly.<br>

| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **Date Picker** |  |  |  |
| --- | --- | --- | --- |
| Select date at the days guests list | Selecting a date in the date picker in the top navigation | When selecting a date with the date picker in the top, the page with the results of the selected date loads | Pass |
| Select date at list of all guests | Selecting a date in the date picker in the top navigation | When selecting a date with the date picker in the top, the page with the results of the selected date loads | Pass |
| Select date at the days reports list | Selecting a date in the date picker in the top navigation | When selecting a date with the date picker in the top, the page with the results of the selected date loads | Pass |
| Select date at list of all reports | Selecting a date in the date picker in the top navigation | When selecting a date with the date picker in the top, the page with the results of the selected date loads | Pass |
</details>


<details>
<summary>Days Guests List</summary>
<br>

Testing functionality of the guests list of a selected date, including check-in, check-out, undo check-in, undo check-out, search, gender selector, date picker, profile behavior and links.<br>

| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **Days Guests List** |  |  |  |
| --- | --- | --- | --- |
| Date picker | Used to select the date to list the guests of the day. | When clicking on the date picker and selecting a date, the page with the selected date loads and all guests of the day are showing up correctly. | Pass |
| Check-in mode switch | A button on the bottom of the page to switch to the check-in mode with a list of not yet checked-in guest on the selected day. | When clicking on the bottom, the button changes from "Check-In Mode" to a read "Close Check-In Mode" button and the list of all not yet checked-in guest is shown. | Pass |
| Close Check-in mode switch | A button on the bottom of the page to switch back to the list of checked-in and checked-out guest of the day. | When clicking on the red "Close Check-In Mode" button at the bottom of the screen is turning the button back to the blue "Check-In Mode" button and the list of already checked-in and checked-out guest of the selected day is shown. | Pass |
| Gender selector female | When selected, only the female guests are shown in the list. | When clicking the female icon at the bottom of the page, the list of guests is filtered to show only female guests. | Pass |
| Gender selector male | When selected, only the female guests are shown in the list. | When clicking the male icon at the bottom of the page, the list of guests is filtered to show only male guests. | Pass |
| Gender selector all | When selected, all guests are shown in the list. | When clicking on "All" at the bottom of the page, the list of guests is not filtered and all guests are shown. | Pass |
| Search | Only matching guests should show up in the list when using the search. | When entering something in the search field, the list automatically filters to only show the matching guests. | Pass |
| Check-in | Checking in a guest for the selected day. | When clicking on the button "Check-In" of a selected profile, the check-in confirmation modal opens. | Pass |
| Check-in confirmation modal | Confirming the check-in of the guest for the selected day. | When clicking the confirmation, the guest gets checked in and the list of the selected day reloads. | Pass |
| Check-in confirmation modal with pickup | Entering information about a different pickup person in the confirmation modal. | When entering the name and clicking the confirmation, the guest gets checked in and the list of the selected day reloads. The pickup information is stored correctly. | Pass |
| Closing check-in confirmation modal with button | Closing the check-in confirmation modal by clicking the "Stop Check-In" button. | When the "Stop Check-In" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing check-in confirmation modal with x-button | Closing the check-in confirmation modal by clicking the "X" button. | When the "X" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing check-in confirmation modal by clicking outside the modal. | Closing the check-in confirmation modal by clicking outside the modal. | When clicked outside, the modal closes and the page is yet again shown like before | Pass |
| Undo check-in | Undo check-in for a guest for the selected day. | When clicking on the button "Undo Check-In" of a selected profile, the undo check-in confirmation modal opens. | Pass |
| Undo check-in confirmation modal | Confirming to undo the check-in of the guest for the selected day. | When clicking "Undo Check-In" in the modal, the check-in is made undone, the information is deleted from the database and the list of the selected day reloads. | Pass |
| Closing undo check-in confirmation modal with button | Closing the undo check-in confirmation modal by clicking the "Stop Undo Check-In" button. | When the "Stop Undo Check-In" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing undo check-in confirmation modal with x-button | Closing  undo check-in confirmation modal by clicking the "X" button. | When the "X" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing undo check-in confirmation modal by clicking outside the modal. | Closing the undo check-in confirmation modal by clicking outside the modal. | When clicked outside, the modal closes and the page is yet again shown like before | Pass |
| Check-out | Checking out a guest for the selected day. | When clicking on the button "Check-Out" of a selected profile, the check-out confirmation modal opens. | Pass |
| Check-out confirmation modal | Confirming the check-out of the guest for the selected day. | When clicking the confirmation, the guest gets checked-out and the list of the selected day reloads. | Pass |
| Closing check-out confirmation modal with button | Closing the check-out confirmation modal by clicking the "Stop Check-Out" button. | When the "Stop Check-Out" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing check-out confirmation modal with x-button | Closing the check-out confirmation modal by clicking the "X" button. | When the "X" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing check-out confirmation modal by clicking outside the modal. | Closing the check-out confirmation modal by clicking outside the modal. | When clicked outside, the modal closes and the page is yet again shown like before | Pass |
| Undo check-out | Undo check-out for a guest for the selected day. | When clicking on the button "Undo Check-Out" of a selected profile, the undo check-out confirmation modal opens. | Pass |
| Undo check-out confirmation modal | Confirming to undo the check-out of the guest for the selected day. | When clicking "Undo Check-Out" in the modal, the check-out is made undone, the information is deleted from the database and the list of the selected day reloads. | Pass |
| Closing undo check-out confirmation modal with button | Closing the undo check-out confirmation modal by clicking the "Stop Undo Check-Out" button. | When the "Stop Undo Check-Out" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing undo check-out confirmation modal with x-button | Closing the undo check-out confirmation modal by clicking the "X" button. | When the "X" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing undo check-out confirmation modal by clicking outside the modal. | Closing the undo check-out confirmation modal by clicking outside the modal. | When clicked outside, the modal closes and the page is yet again shown like before | Pass |
| Profile dropout | Profile in lists expands and shows more information. | When clicking on a profile in the guest list, the profile expands and shows more information and actions to choose from. | Pass |
| Profile collapse | Collapsing the profile when not in focus. | When clicking somewhere else then on one of the action in the expanded profile, the profile collapses and is small like before. | Pass |
| Food indicator collapsed | Showing the food indicator in collapsed profile. | When information is saved in database, the indicator shows up in the collapsed profile. | Pass |
| Food indicator expanded | Showing the food indicator and times in expanded profile. | When information is saved in database, the indicator shows up  in the expanded profile. | Pass |
| Medication indicator collapsed | Showing the medication indicator in collapsed profile. | When information is saved in database, the indicator shows up in the collapsed profile. | Pass |
| Medication indicator expanded | Showing the medication indicator and times in expanded profile. | When information is saved in database, the indicator shows up  in the expanded profile. | Pass |
| Report indicator collapsed | Showing the report indicator in collapsed profile. | When a guest was tagged in a report that day, the indicator is shown in the collapsed profile. | Pass |
| Report indicator expanded | Showing the report indicator and additional option in expanded profile. | When guest was tagged in a report that day, the indicator is shown and the additional button to show reports is displayed in the expanded profile. | Pass |
| Pickup indicator collapsed | Showing the pickup indicator in collapsed profile. | When a pickup name was entered during the check-in process, the indicator is shown in the collapsed profile. | Pass |
| Pickup indicator expanded | Showing the pickup information in the expanded profile. | When a pickup name was entered during the check-in process, the name is shown in the expanded profile. | Pass |
| Read report button | When tagged in a report on the selected day, an additional button is shown to read the reports of the day | When expanding a profile of a guest, that has been tagged in a report that day the button shows up. When clicking the button, the user is directed to the list of the reports of the selected day. | Pass |
| Open file button | Open the profile of the selected guest | When clicking on the button, the profile of the guest loads. | Pass |
</details>


<details>
<summary>All Guests List</summary>
<br>

Testing functionality of the list of all guests in the system, including search, gender selector, date picker, profile behavior and links.<br>

| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **All Guests** |  |  |  |
| --- | --- | --- | --- |
| Date picker | Used to select the date to list the guests of the day. | When clicking on the date picker and selecting a date, the page with the selected date loads and all guests of the day are showing up correctly. | Pass |
| Gender selector female | When selected, only the female guests are shown in the list. | When clicking the female icon at the bottom of the page, the list of guests is filtered to show only female guests. | Pass |
| Gender selector male | When selected, only the female guests are shown in the list. | When clicking the male icon at the bottom of the page, the list of guests is filtered to show only male guests. | Pass |
| Gender selector all | When selected, all guests are shown in the list. | When clicking on "All" at the bottom of the page, the list of guests is not filtered and all guests are shown. | Pass |
| Search | Only matching guests should show up in the list when using the search. | When entering something in the search field, the list automatically filters to only show the matching guests. | Pass |
| Profile dropout | Profile in lists expands and shows more information. | When clicking on a profile in the guest list, the profile expands and shows more information and actions to choose from. | Pass |
| Profile collapse | Collapsing the profile when not in focus. | When clicking somewhere else then on one of the action in the expanded profile, the profile collapses and is small like before. | Pass |
| Food indicator collapsed | Showing the food indicator in collapsed profile. | When information is saved in database, the indicator shows up in the collapsed profile. | Pass |
| Food indicator expanded | Showing the food indicator and times in expanded profile. | When information is saved in database, the indicator shows up  in the expanded profile. | Pass |
| Medication indicator collapsed | Showing the medication indicator in collapsed profile. | When information is saved in database, the indicator shows up in the collapsed profile. | Pass |
| Medication indicator expanded | Showing the medication indicator and times in expanded profile. | When information is saved in database, the indicator shows up  in the expanded profile. | Pass |
| Open file button | Open the profile of the selected guest | When clicking on the button, the profile of the guest loads. | Pass |
</details>


<details>
<summary>Guest Details Page</summary>
<br>

Testing functionality of the guest details page, including deletion, tagged reports and links.<br>

| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **Guest Details** |  |  |  |
| --- | --- | --- | --- |
| Food information | Information about feeding times are shown. | When feeding information were saved to the guest, the information is shown on the profiles detail page | Pass |
| Medication information | Information about medication times are shown. |  When feeding information were saved to the guest, the information is shown on the profiles detail page | Pass |
| Tagged reports | Reports relevant to guest showing. | Reports in which the guest was tagged are shown on the bottom of the page, sorted with the newest first. | Pass |
| Tagged guests | Tagged guests are listed in reports. | When one or more guest have been tagged in a report, the tagged guests are showing up. Clicking on the guest's name loads the guest's profile. | Pass |
| Report details link | Link to go to report details page. | When clicking on the link on the bottom of a report, the details page of the report loads. | Pass |
| Edit guest profile | Go to editor for guest profile | When clicking on the blue "Edit guest profile" button, the profile editor opens with all existing information for the guest already filled in the form fields and profile image showing up. | Pass |
| Delete profile | Open deletion confirmation modal | When clicking in the red "Delete profile" button, a modal to confirm the deletion opens. | Pass |
| Delete profile confirmation modal | Confirming deletion | When clicking on the confirmation for deleting the profile, the profile gets deleted from the database and the user is redirected to the guest list of the most resent day.  | Pass |
| Closing deletion confirmation modal with button | Closing the deletion confirmation modal by clicking the "Cancel" button. | When the "Cancel" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing deletion confirmation modal with x-button | Closing the deletion confirmation modal by clicking the "X" button. | When the "X" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing deletion confirmation modal by clicking outside the modal. | Closing the deletion confirmation modal by clicking outside the modal. | When clicked outside, the modal closes and the page is yet again shown like before | Pass |
</details>


<details>
<summary>Add/Edit Guest Page</summary>
<br>

Testing functionality of the form to add new guests and edit existing guests.<br>

| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **Add/Edit Guest** |  |  |  |
| --- | --- | --- | --- |
| Field: First name | Leave field empty. | Leaving the field empty leads to the profile not being saved and the field getting in focus | Pass |
| Field: First name | Filling field | Filling the field with a string | Pass |
| Field: Last name | Leave field empty. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database | Pass |
| Field: Last name | Filling field | Filling the field with a string | Pass |
| Field: Name addon | Leave field empty when first name not already used. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database. | Pass |
| Field: Name addon | Leave field empty when first name already used. | Leaving the field empty is not possible and prevents the profile from being saved to the database. An error is shown. | Pass |
| Field: Name addon | Filling field | Filling the field with a string | Pass |
| Field: Name addon validation | Filling field with already existing combination of first name and name addon. | Using a combination of first and addon name that already exists is not possible and prevents the profile from being saved to the database. An error is shown with a hint to choose a different name addon. | Pass |
| Field: Gender | Choosing value | Choosing a value isn't preventing the profile from saving. | Pass |
| Field: Image | Leave field empty. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database | Pass |
| Field: Image | Uploading image | Uploading a image that is saved to cloudinary and then shown as profile image | Pass |
| Field: Image | Uploading non image file | Selecting of a non image file is not possible. | Pass |
| Field: Date of birth | Leave field empty. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database | Pass |
| Field: Date of birth | Picking a date | The picked date is correctly saved to the database | Pass |
| Field: Additional information | Leave field empty. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database | Pass |
| Field: Additional information | Filling field | Filling the field with a string is possible and it is saved to the database | Pass |
| Field: Food | Leave field empty. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database | Pass |
| Field: Food | Checking the box | Checking the box and saving to the database is working correctly. | Pass |
| Field: Food time 1 | Leave field empty. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database | Pass |
| Field: Food time 1 | Pick time | Picking a time and saving to the database works correctly | Pass |
| Field: Food time 2 | Leave field empty. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database | Pass |
| Field: Food time 2 | Pick time | Picking a time and saving to the database works correctly | Pass |
| Field: Food time 3 | Leave field empty. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database | Pass |
| Field: Food time 3 | Pick time | Picking a time and saving to the database works correctly | Pass |
| Field: Medication | Leave field empty. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database | Pass |
| Field: Medication | Checking the box | Checking the box and saving to the database is working correctly. | Pass |
| Field: Medication time 1 | Leave field empty. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database | Pass |
| Field: Medication time 1 | Pick time | Picking a time and saving to the database works correctly | Pass |
| Field: Medication time 2 | Leave field empty. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database | Pass |
| Field: Medication time 2 | Pick time | Picking a time and saving to the database works correctly | Pass |
| Field: Medication time 3 | Leave field empty. | Leaving the field empty is possible and doesn't prevent the profile from being saved to the database | Pass |
| Field: Medication time 3 | Pick time | Picking a time and saving to the database works correctly | Pass |
| Field: Owner| Leave field empty. | Leaving the owner field empty shows an error and the profile is not saved. | Pass |
| Field: Owner| Selecting owner from dropdown list. | An owner can be selected from a list consisting of all customers in the system. | Pass |
| Cancel button | Cancel process | Pressing the red "Cancel" button redirects the user to the main page with the most current date. | Pass |
| Add button | Invalid input | Pressing the "Add" button when any field has an invalid input, saving the profile to the database does not work and errors are shown. | Pass |
| Add button | Correct input | Pressing the "Add" button with valid input saves the profile to the database and redirects the user to the newly created/updated profile. | Pass |
</details>


<details>
<summary>Days Reports List</summary>
<br>

Testing functionality of the reports list of a selected date, including tagged guests, links and date picker.<br>

| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **Days Reports List** |  |  |  |
| --- | --- | --- | --- |
| Date picker | Used to select the date to list the reports of the day. | When clicking on the date picker and selecting a date, the page with the selected date loads and all reports of the day are showing up correctly. | Pass |
| Tagged guests | Tagged guests are listed in reports. | When one or more guest have been tagged in a report, the tagged guests are showing up. Clicking on the guest's name loads the guest's profile. | Pass |
| Report details link | Link to go to report details page. | When clicking on the link on the bottom of a report, the details page of the report loads. | Pass |
</details>


<details>
<summary>All Reports List</summary>
<br>

Testing functionality of the list with all reports in the system, including tagged guests, links and date picker.<br>


| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **All Reports** |  |  |  |
| --- | --- | --- | --- |
| Date picker | Used to select the date to list the reports of the day. | When clicking on the date picker and selecting a date, the page with the selected date loads and all reports of the day are showing up correctly. | Pass |
| Tagged guests | Tagged guests are listed in reports. | When one or more guest have been tagged in a report, the tagged guests are showing up. Clicking on the guest's name loads the guest's profile. | Pass |
| Report details link | Link to go to report details page. | When clicking on the link on the bottom of a report, the details page of the report loads. | Pass |
</details>


<details>
<summary>Report Details Page</summary>
<br>

Testing functionality of the report details page, including deletion, tagged guests and links.<br>


| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **Report Details** |  |  |  |
| --- | --- | --- | --- |
| Tagged guests | Tagged guests are listed in reports. | When one or more guest have been tagged in a report, the tagged guests are showing up. Clicking on the guest's name loads the guest's profile. | Pass |
| Edit report profile | Go to the editor for the report | When clicking on the blue "Edit Report" button, the report editor opens with all existing information from the report already filled in the form fields. | Pass |
| Delete report | Open deletion confirmation modal | When clicking in the red "Delete Report" button, a modal to confirm the deletion opens. | Pass |
| Delete report confirmation modal | Confirming deletion | When clicking on the confirmation for deleting the report, the report gets deleted from the database and the user is redirected to the reports list of the most resent day. | Pass |
| Closing deletion confirmation modal with button | Closing the deletion confirmation modal by clicking the "Cancel" button. | When the "Cancel" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing deletion confirmation modal with x-button | Closing the deletion confirmation modal by clicking the "X" button. | When the "X" button is clicked, the modal closes and the page is yet again shown like before | Pass |
| Closing deletion confirmation modal by clicking outside the modal. | Closing the deletion confirmation modal by clicking outside the modal. | When clicked outside, the modal closes and the page is yet again shown like before | Pass |
</details>


<details>
<summary>Add/Edit Report Page</summary>
<br>

Testing functionality of the form to add or edit reports.<br>

| **Test** | **Description** | **Expected Outcome** | **Result** |
| --- | --- | --- | --- |
| **Add/Edit Report** |  |  |  |
| --- | --- | --- | --- |
| Field: Select date | Leaving field empty | When leaving the field empty and not selecting a date, the report is not saved to the database and a hint to select a date is shown. | Pass |
| Field: Select date | Date picker is used to select the date the report is for. | When clicking on the date picker, selecting a date, and saving the report saved the correct date to the database. | Pass |
| Field: Report text | Leave field empty. | Leaving the field empty is not possible, and does prevent the report from being saved to the database. A hint to fill the field is shown. | Pass |
| Field: Report text | Filling field | Filling the field with a string is possible and it is saved to the database | Pass |
| Field: Tag guests | Leaving field empty | When the field is left empty, the report is correctly saved to the database. | Pass |
| Field: Tag guests | Tag one guest on a report | When selecting one guest, the report is correctly saved to the database. | Pass |
| Field: Tag guests | Tag multiple guests on a report | When selecting multiple guests, the report is correctly saved to the database. | Pass |
| Cancel button | Cancel process | Pressing the red "Cancel" button redirects the user to the main page with the most current date. | Pass |
| Add button | Invalid input | Pressing the "Add" button when any field has an invalid input, saving the report to the database does not work and errors are shown. | Pass |
| Add button | Correct input | Pressing the "Add" button with valid input saves the report to the database and redirects the user to the list of reports for the most recent date. | Pass |
</details>

#### Possible Improvements

In a future version, the following improvements should be made:<br>

- Using an alternative for the Django-Bootstrap-Datapicker-Plus Widget (latest version 5.0.5) to ensure no deprecated code is used in the project (improve "Best Practices" rating on Lighthouse).
- Find alternative to Cloudinary or optimize the existing implementation to limit use of 3rd party cookies (improve "Best Practices" rating on Lighthouse).
- Improve search to not be based on a complete list of profiles, showing or hiding using Bootstrap, but use fast and more efficient database requests.
- Improve gender selector, similar to the search feature.
- Pagination on list for all guests and all reports, as well as for all reports on a guest's profile page.

#### Fixed Bugs

**Guest Update Not Working**
When adding the Guest Update feature, the updated data for a guest was not saved in the database, because the form validation has noticed the existing database entry as duplicate of the same dataset and so the validation threw an error.<br>
To solve this, the validation has to ignore the duplicate of their own dataset. So exclude the dataset with given ID in the validation process.<br>
<br>

**Buggy Modals**
During the development, a bug with the confirmation modals came up. Modals did not close properly when clicking outside the modal, like it was supposed to.<br>
After a first fix attempted, it closed correctly, when clicking outside the modal, but the close icon and cancel button stopped working.<br>
The final fix was to redefine the clickable areas and elements rewriting the according JavaScript code.<br>
<br>

**Search Bar Not Showing On Mobile**
During the development, the search bar was missing on smaller screens. This was only noticed later in the development phase.<br>
The issue was based on Bootstrap hiding the search bar on smaller screens. This worked as intended, but a solution to let the search bar show up again was forgotten to be implemented.<br>
The final fix was adding a separate search bar, that is only shown when clicking on the search icon in the top navigation.<br>
<br>


#### Known Unfixed Bugs

Know bugs are know.<br>


## Credits

- Use case is based on working experience of Dennis Schenkel in a dog day care center.
- All content was written and created by Dennis Schenkel.
- Images were created with the help of DALL-E.
<br>
When trying to understand concepts and build this full-stack-application, an unlimited amount of Google searches were conducted and various sources like Stack Overflow, Reddit and the different documentations for Django and Bootstrap were used.

### Acknowledgements

- Thanks to Gareth McGirr for providing great mentorship as part of the Code Academy course.
- Thanks to Kay for they efford as a facilitator of the Code Institute team.
- Great thanks go to [Dajana Isbaner](https://github.com/queenisabaer) for being the best fellow student I could wish for.