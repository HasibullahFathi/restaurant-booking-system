# Manual Testing

[Go to README](README.md)

| Test Case                         | Expected Result                                                                                | Test Result |
|-----------------------------------|-----------------------------------------------------------------------------------------------|-------------|
| Open the Homepage                 | Homepage loads with the correct template and data                                              | ✅ PASS      |
| Register a user with valid data   | Request is successful, user is registered and logged in, message is shown                      | ✅ PASS      |
| Register a user with invalid data | Request fails, form reloads with data and errors                                               | ✅ PASS      |
| Login a user with valid data      | Request is successful, user is logged in, message is shown                                     | ✅ PASS      |
| Login a user with invalid data    | Request fails, form reloads with data and errors                                               | ✅ PASS      |
| Login with super admin user       | All options and data are accessible                                                            | ✅ PASS      |
| Login with regular user           | User can perform CRUD operations only on their own bookings                                    | ✅ PASS      |
| Selecting menu from nav bar       | The menu categories page loads with correct template and data                                  | ✅ PASS      |
| Selecting a category              | Opens the correct menu items belonging to the selected category                                | ✅ PASS      |
| Responsive design                 | The layout adjusts properly without any overlap or misalignment in all screen sizes            | ✅ PASS      |
| **Admin access control**          |                                                                                               |             |
| Add a category                    | Request is successful, category is added to the list, message is shown                         | ✅ PASS      |
| Edit a category                   | Request is successful, category content is edited, message is shown                            | ✅ PASS      |
| Delete a category                 | Request is successful, category is deleted, message is shown                                   | ✅ PASS      |
| Add a menu item                   | Request is successful, item is added to the list, message is shown                             | ✅ PASS      |
| Edit a menu item                  | Request is successful, item content is edited, message is shown                                | ✅ PASS      |
| Delete a menu item                | Request is successful, item is deleted, message is shown                                       | ✅ PASS      |
| View booking list                 | Admin can see and manage all bookings                                                          | ✅ PASS      |
| **Regular User**                  |                                                                                               |             |
| Add a booking                     | Request is successful, booking is added to the list, message is shown                          | ✅ PASS      |
| Edit a booking                    | Request is successful, booking content is edited, message is shown                             | ✅ PASS      |
| Booking overlap validation        | Request fails, and an error message is shown indicating the booking conflict                   | ✅ PASS      |
| Past date booking                 | Request fails, form reloads with an error message indicating that the booking date must be in the future | ✅ PASS      |
| Booking cancellation              | Booking is canceled successfully, and a success message is shown                               | ✅ PASS      |
| Delete a booking                  | Request is successful, booking is deleted, message is shown                                    | ✅ PASS      |
| Form validation feedback          | The form reloads with relevant error messages for each missing or incorrect field              | ✅ PASS      |
| View booking list                 | User can only see and manage their own bookings                                                | ✅ PASS      |
| View booking details              | The booking details page loads with all relevant information displayed correctly               | ✅ PASS      |
