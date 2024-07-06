
Real world use:
Mention the real world scenario for the app.

User management
- In the usecase of this app only the system admin should be allowed to create new users. So there is no public registration form of any kind.


Technologies and services used
- Heroku
- Cloudinary


Plugins used
- bootstrap_datepicker_plus


Steps of development:
- Starting with a basic html and css layout
- Adding the core functionality of guest checkin and checkout.
- Add functionality for searching guests, displaying critical information
- Building guest profiles and CRUD functionality
- Adding authentication feature for access controlle
- Adding basic report system
- Adding guest mentions to report system and showing related reports in guest profile


Features:
- Guest profiles (CRUD)
- Search
- Date selector
- Gender filter
- Check-in/Check-out
- Undo Check-in/Check-out
- Confirmations with modals
- Report system (CRUD)
- Report indicator on guest list
- Medication indicator on guest list
- Food indicator on guest list
- Alternativ pickup with indicator on guest list
- Messages for user feedback
- User authentication

Bugs to mention: 
- Upload of images and the way I fixed it with pillow.
- Buggy closing of modals. Modals did not close properly when clicking outside of the modal.

- When adding the Guest Update feature, the updated data was not saves, because the form validation has noticed the existing database entry as duplicate of the same dataset and so the validation threw an error.
    - To solve this, the validation has to ignore the duplicate of their own dataset. So exclude the dataset with given ID in the validation process.


Agile project management: 
During the process of deveolment, the kanban board and backlog, userstories and milestones where constantly addapting to new findings and changing requirements. Feature request have been modified, added or the priority was changed.