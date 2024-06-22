
Real world use:
Mention the real world scenario for the app.


Technologies and services used
- Heroku
- Cloudinary

Steps of development:
- Starting with a basic html and css layout
- Adding the core functionality of guest checkin and checkout.
- Add functionality for searching guests, displaying critical information
- Building guest profiles and CRUD functionality
- Adding authentication feature for access controlle
- Adding basic report system
- Adding guest mentions to report system and showing related reports in guest profile


Bugs to mention: 
- Upload of images and the way I fixed it with pillow.
- Buggy closing of modals. Modals did not close properly when clicking outside of the modal.

- When adding the Guest Update feature, the updated data was not saves, because the form validation has noticed the existing database entry as duplicate of the same dataset and so the validation threw an error.
    - To solve this, the validation has to ignore the duplicate of their own dataset. So exclude the dataset with given ID in the validation process.


Agile project management: 
During the process of deveolment, the kanban board and backlog, userstories and milestones where constantly addapting to new findings and changing requirements. Feature request have been modified, added or the priority was changed.