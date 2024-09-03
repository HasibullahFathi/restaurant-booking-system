# Red Chillies

![Responsive Mockup](/media/main-img.png)

Red Chillies is an imaginary restaurant reservation web page that brings facilities like reserve online tables, manage their reservations, check menu, and so on. 
It is not an actual site for a restaurant, this is a project to show my coding knowledge and using technologies.

## Porpose 
This online restaurant booking system offers several key benefits:

### For Restaurant Owners:
- Increased Efficiency: Streamlines table management, reducing manual work.
- Better Customer Insights: Tracks reservations, preferences, and peak times.
- Enhanced Marketing: Collects customer data for targeted promotions.

### For Guests:
- Convenience: Allows 24/7 reservations from any device.
- Immediate Confirmation: Provides instant booking confirmations and updates.
- Reduced Wait Times: Ensures a reserved table, minimizing wait upon arrival.


## Live Page
[https://red-chillies-df2854b5e6de.herokuapp.com/](https://red-chillies-df2854b5e6de.herokuapp.com/)


## Features

### Navigation bar
The navigation bar is the first element that appears on each page.
- Left Side: The restaurant name, which navigates to the home page.
- Right Side:
  - Home: Linked to the home page.
  - Menu: Navigates to a list of menu categories.
  - Logout: Logs the user out.
  - Username: Displays the username of the logged-in user.

![Home page Mockup](/media/home-img.png)

When the user is logged out, the username and logout links are replaced by login and register links.
![Login page Mockup](/media/login.png)

The navigation is fully responsive across all screen sizes.

![Login page Mockup](/media/menu-responsive.png)

### Home page
The homepage features an eye-catching hero image and hero text as the second element that appears after landing on the page.
- First Section: Displays the restaurant's opening and closing times.

![Fiest section Mockup](/media/section1-img.png)

- Second Section: Contains photos accompanied by descriptive text.
- Third Section: An "About" section providing short information about Red Chillies.

![third section Mockup](/media/section3-img.png)

## Menu
This is where all the restaurant's menu items and categories are listed. Users do not need to log in to view the menu.

### Show menu categories
- Menu categories are listed on the menu page as collapsible buttons.

![Category Mockup](/media/menu-category.png)

### Add menu categories (if the user is Admin)
If the user is an Admin, they will see an "Add Category" button at the top of the category list. This button opens a form where the user can add a new category name, which must be unique.
- The form is validated with backend validation to guide the user in case of errors.
- The user will see a confirmation message, error message, or success message after attempting to add a category.

![Add Category Mockup](/media/category-form.png)

### Delete menu categories (if the user is Admin)
At the right side of each category's collapse button is a delete/cancel button. When clicked, a confirmation modal appears, asking the user to confirm the deletion of the selected category. This action is available only if the user is logged in and has admin permissions.
- The user receives a confirmation message or an error message depending on the success of the deletion.

![Delete Category Mockup](/media/delete-category.png)

### Edit menu categories (if the user is Admin)
Next to the delete button on each category's collapse button is an edit button. Clicking this opens the edit form for the selected category. This feature is accessible only to logged-in users with admin permissions.
- The form includes backend validation to guide the user in case of errors.
- After attempting to update a category, the user sees a confirmation message or an error message.

![Edit Category Mockup](/media/edit-category.png)

### Show menu items
Clicking the collapse button of a specific category reveals the menu items belonging to that category. These items are displayed in cards that include:
- Item pictures
- Status (Available or not)
- Price
- Details of the item

![Menu list Mockup](/media/menu-list.png)

### Add menu items (if the user is Admin)
At the top of the category list, there is an "Add Item" button. Clicking this opens a form where the user can add a new item. The form requires:
- A unique item name
- A description (optional)
- A price (must be greater than zero)
- The item's status
- Category selection
- An option to upload a picture (if no picture is chosen, a default image will be set)
- This action is available only if the user is logged in and has admin permissions.
- The form is validated with backend checks to ensure accuracy.
- After attempting to add a menu item, the user receives a confirmation message or an error message.

![Create menu Mockup](/media/menu-form.png)

### Delete menu items (if the user is Admin)
Below each item's image is a delete button. Clicking this button opens a confirmation modal. After confirming, the item will be deleted from the system. This feature is available only if the user is logged in and has admin permissions.
- The user will receive a confirmation message or an error message depending on the success of the deletion.

![Delete menu Mockup](/media/delete-menu-item.png)

### Edit menu items (if the user is Admin)
Below each item's image is an edit button. Clicking this button opens an edit form prefilled with the current item's data. This allows the user to update the item’s details. This feature is available only if the user is logged in and has admin permissions.
- The form includes backend validation to guide the user in case of errors.
- The user will see a confirmation message or an error message after attempting to update a menu item.

![Edit menu Mockup](/media/edit-menu-form.png)

## Booking
- This section displays all table reservations.

### See the booking list (if logged in)
If the user is logged in, a "My Booking" button appears on the home page, which navigates the user to a booking list ordered by booking date in a table format.
- Each user can see only their own reservations.
- Users with admin permissions can view all reservations.

![Booking list Mockup](/media/booking-list.png)

### Paginate booking list
The booking list is paginated, displaying 8 items per page. The number of pages is shown at the bottom of the list.

### View booking details
By clicking the open icon on the right side of the table under the "Action" column, the user can view all details of the selected booking on a dedicated page.
- A "Back to Booking List" button at the bottom of the card allows the user to navigate back to the booking list.

![Booking details Mockup](/media/booking-details.png)

### Create booking (if logged in)
At the top right of the booking page, there is a "Create Booking" button that opens the reservation form. Every logged-in user can create a booking by filling out the form and submitting it, provided the following conditions are met:
- Select Shift: The user must choose an available opening/closing time (shift).
- Availability: The user can only reserve a table that is available during the selected shift. Duplicate reservations are not allowed.
- Time Selection: The user must select a time within the opening and closing hours of the selected shift. Reservations outside these hours are not permitted.
- Future Date: The booking date must be in the future. Past dates are not allowed.
- Guest Count: The number of guests must be greater than zero.

The form includes backend validation to guide the user in case of errors. After submission, the user will see a confirmation message indicating whether the booking was successful or if there was an error. The "Back to Booking List" button at the end of the form returns the user to the booking list.

![Booking Form Mockup](/media/booking-form.png)

### Edit all bookings (if logged in)
Clicking the edit icon on the right side of the booking list, under the "Action" column, opens a pre-filled form with the data of the selected booking. Every logged-in user can edit their booking by modifying the details and submitting the form, provided the following conditions are met:
- Select Shift: The user must choose an available opening/closing time (shift).
- Availability: The user can only reserve a table that is available during the selected shift. Duplicate reservations are not allowed.
- Time Selection: The user must select a time within the opening and closing hours of the selected shift. Reservations outside these hours are not permitted.
- Future Date: The booking date must be in the future. Past dates are not allowed.
- Guest Count: The number of guests must be greater than zero.

The form includes backend validation to guide the user in case of errors. After submission, the user will receive a confirmation message indicating whether the update was successful or if there was an error.

![Edit Booking form Mockup](/media/edit-booking-form.png)

### Delete/Cancel bookings (if logged in)
Clicking the delete icon on the right side of the booking list, under the "Action" column, opens a confirmation modal. Every logged-in user can delete their booking by confirming the deletion.
- The user will receive a confirmation message indicating whether the deletion was successful or if there was an error.

![Delete Booking Mockup](/media/delete-booking.png)

## Restaurant Tables
Creating, updating and deleting tables are at the moment only form admin panel posible.

## Shift(Opening/Closing times)
Creating, updating and deleting Shifts are at the moment only form admin panel posible.

## Register
To access features reserved for members of the website, such as online reservations, users must register. The registration page can be accessed via the link in the navigation bar or through various links available throughout the website.

To become a member, the user needs to provide the following information:

- Username
- Email (Optional)
- Password
- Confirm Password

If the provided information is valid and the username is not already taken, the user is automatically logged in and redirected to the home page. Upon successful registration, a confirmation success message is displayed.

![Singn Up page Mockup](/media/signup.png)

### Create a profile automatically
By default, when a user registers, the system automatically creates a user profile. The admin or super admin can then assign admin permissions to the user if necessary. Note that without a profile, a user cannot book a table.

## Login
If an unauthenticated member wants to use features reserved for members, such as booking a table, they must first log in. The login page can be accessed via the navigation bar or through various links available throughout the website.

To log in, the user must enter:

- Username
- Password

If the username and/or password are incorrect, the form reloads, informing the user of the error. Upon successful login, a confirmation success message is displayed.

![Login page Mockup](/media/login.png)

## Logout
The logout option is visible in the navigation bar when the user is logged in. Clicking the logout button ensures that no one else can access the user's information, especially on a shared or public device.

Upon clicking the logout button:

- The user is immediately logged out and redirected to the homepage.
- The user's session data is cleared.
- Access to secure pages is restricted until the user logs in again.

A confirmation success message is displayed when the user logs out.

## Confirmation Messages
For almost all actions in the system, confirmation messages are used to indicate the result of the action. These can be error or success messages.

![Confirmation alert Mockup](/media/alert.png)

## Personalization
When a user is logged in, their username is displayed on the right side of the navigation bar.

## Footer
The footer displays the copyright text and links to various social media websites. Each link opens in a new tab.

![Footer Mockup](/media/footer.png)

## Additional Features
Features that could be implemented in the future include:

- Notification System: Allow users (both admin and regular users) to receive notifications regarding any changes or new bookings.
- Search Functionality: Search for menu items, categories and bookings.
- Filter/Search Bookings: Filter or search bookings by specific fields.
- Online Food Ordering: Implement an online food ordering system.

## Testing
### Manual testing
This project has been tested manually from both design and functionality perspective, ensuring that it meets user stories and responsiveness requirements.
[List of the Tests](manual_test.md)

#### Validation:
- Python

![Python validation Mockup](/media/python-validation.png)

- JavaScript

![Javascript validation Mockup](/media/js-validation.png)

- HTML

![HTML validation Mockup](/media/html-validation.png)

- CSS

![CSS validation Mockup](/media/css-vlidation.png)

- Lighthouse Report

![Lighthouse report Mockup](/media/lighthouse-vlidation.png)


## Bugs
- There were no unfixed bugs.

### Fixed Bugs
- Modal Issue for Deleting Reservations: There was a problem with the modal for deleting a reservation where the delete and cancel buttons were not clickable on actual phones, though they worked on computer browsers and different screen sizes. This issue was fixed by removing the modal from being a child of the table.

- Date and Time Picker Issue: The date and time picker was not working with the crispy forms. This issue was resolved by adding form fields in forms.py to allow users to input date and time values with the proper format.

## Development process
In the process of developing this project, I followed agile principles as closely as possible. Various tools and methods were employed to design and analyze the development process.

### Development preparation
- User Stories: Defined what functionalities the system should have.
  - User Stories Link [GitHub Project](https://github.com/users/HasibullahFathi/projects/5/views/1)
- Wireframe: Initial design mockups of the pages in the system.

  ![Home page](/media/home-wireframe.png)
  ![Menu page](/media/menu-wireframe.png)
  ![booking page](/media/booking-wireframe.png)

- ERD (Entity-Relationship Diagram): Outlined the data needed to work with and the fields of the models.

  ![Booking ERD](/media/booking-ERD.png) ![Menu ERD](/media/menu-ERD.png)

### Agile Development
- Issue Gathering and Analysis: Collected and analyzed issues.
- Breakdown: Split issues into smaller, manageable user stories for easier tracking.
- Acceptance Criteria: Further divided user stories into more manageable and understandable acceptance criteria.
- Prioritization: Ordered user stories based on priority for development.
- Task Management: Used a task board to track progress by moving tasks from "To Do" to "In Progress" and then to "Done" upon completion.

Link to the user stories in my [GitHub Project](https://github.com/users/HasibullahFathi/projects/5/views/1)

### Git
- Version Control: Used the Code Institute CI-Full Template for version control. [CI-full template](https://github.com/Code-Institute-Org/ci-full-template)
- Commit and Push: Regularly added and committed changes with descriptive and concise comments, then pushed them to Git for version control.
- Issue Resolution: Pulled specific commits to review changes that caused issues when necessary.

## Deployment
The site was deployed on Heroku.

### Preparations
- DEBUG Setting: Set DEBUG to False in settings.py.
- Dependencies: Stored all dependencies in the requirements.txt file using the command: `pip3 freeze --local > requirements.txt`
- Procfile Creation: Created a Procfile with the following command: `echo "web: gunicorn red_chillies.wsgi" > Procfile`

### Deployment Setup
To deploy a project on Heroku, follow these steps:

- Create a Heroku App:
  - Go to the Heroku Dashboard.
  - Click "New" and select "Create new app."
  - Enter a unique name for your app and select a region.

- Configure Environment Variables:
  - Navigate to the "Settings" tab of your Heroku app.
  - Click "Reveal Config Vars" and add the following environment variables:
    - DJANGO_SETTINGS_MODULE: Your Django settings module.
    - DATABASE_URL: Your database URL (if using a database add-on like Heroku Postgres).
    - SECRET_KEY: Your Django secret key.
    - CLOUDINARY_URL: Your Cloudinary API URL (includes API key, secret, and cloud name).

- Add Buildpack:
  - In the "Settings" tab, scroll to the "Buildpacks" section.
  - Click "Add Buildpack" and select heroku/python.

- Deploy from GitHub:
  - Go to the "Deploy" tab.
  - In the "Deployment method" section, select "Connect to GitHub."
  - Search for your project name and connect the repository.

- Choose Deployment Method:
  - You can choose between Automatic Deploys and Manual Deploys. During development, I chose Manual Deploys to deploy changes manually after pushing updates to Git.

## Credits
Special thanks from my mentor Moritz Wach for his support and guidance.

### Usage Technologies and Tools
- [Django:](https://www.djangoproject.com/) Web framework used for development.
- [Bootstrap:](https://getbootstrap.com/) Frontend framework for styling and responsiveness.
- [Heroku:](https://www.heroku.com/) Platform for deploying and hosting the web application.
- [Postgresql:](https://www.postgresql.org/) As the database provider
- [Cloudinary:](https://cloudinary.com/) As the image storage

### Django Apps
- Django Crispy Forms: For rendering forms with Bootstrap styles.
- Cloudinary: For media management and image hosting.

### Content and media
- The template was taken and used with much modifications from [Startbootstrap](https://startbootstrap.com/)
- Images: All images were downloaded from [Pexels](https://www.pexels.com/)
- Icons: All icons on the website are from [FontAwesome](https://fontawesome.com/)


