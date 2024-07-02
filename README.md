## Description:
This Django project provides a comprehensive system for managing and analyzing users session's data. It consists of four apps: api, authapi, fetchapi, mlintegration.

## Usage:
first app (api):
- To view available API endpoints and their functionalities `/api/`.
- To add new data, send a POST request to `/api/add/`.
- To view all data, send a GET request to `/api/view/`.
- To separate records of each session for each user, send a GET request to `/api/separated/`.
- To view details of each unique session, send a GET request to `/api/unique/`.
- To view the cumulative duration of sessions for each user, send a GET request to `/api/total_sessions_duration/`.

second app (authapi):
- To login, send a POST request to `/authapi/login/`.
- To sign up, send a POST request to `/authapi/signup/`.
- To logout, send a POST request to `/authapi/logout/`.
- To change password, send a POST request to `/authapi/change_password/`.
- To add a user manually, send a POST request to `/authapi/add_user/`.
- To test token validity, send a GET request to `/authapi/test_token/`.
- To suspend or activate users, send a POST request to `/authapi/suspend_users/`.
- To update user staff status, send a POST request to `/authapi/update_user_staff_status/`.
- To update user superuser status, send a POST request to `/authapi/update_user_superuser_status/`.
 
third app (fetchapi):
- To fetch user quiz data, send a GET request to `/fetchapi/fetchquiz/`.
- To fetch user assignment data, send a GET request to `/fetchapi/fetchassignment/`.
- To fetch user session data, send a GET request to `/fetchapi/fetchsession/`.
- To fetch user data, send a GET request to `/fetchapi/fetchuserdata/`.
- To fetch course data, send a GET request to `/fetchapi/fetchcourse/`.
  
fourth app (mlintegration):
- To get predictions for academic performance based on various features like session data and quiz grades, send a GET request to `/successprediction/`.
- To get grade predictions for academic performance, send a GET request to `/gradeprediction/`.


## Endpoints:
first app (api):
- `/api/`: API Overview
- `/api/add/`: Add new data
- `/api/view/`: View all data
- `/api/separated/`: Separate records of each session for each user
- `/api/unique/`: View details of each unique session
- `/api/total_sessions_duration/`: View the cumulative duration of sessions for each user

second app (authapi):
- `/authapi/login/`: User login
- `/authapi/signup/`: User signup
- `/authapi/logout/`: User logout
- `/authapi/change_password/`: Change user password
- `/authapi/add_user/`: Add user manually
- `/authapi/test_token/`: Test token validity
- `/authapi/suspend_users/`: Suspend or activate users
- `/authapi/update_user_staff_status/`: Update user staff status
- `/authapi/update_user_superuser_status/`: Update user superuser status

third app (fetchapi):
- `/fetchapi/fetchquiz/`: Fetch user quiz data
- `/fetchapi/fetchassignment/`: Fetch user assignment data
- `/fetchapi/fetchsession`/: Fetch user session data
- `/fetchapi/fetchuserdata/`: Fetch user data
- `/fetchapi/fetchcourse/`: Fetch course data

fourth app (mlintegration):
- `/successprediction/`: Get predictions
- `/gradeprediction/`: Get grade predictions


## Technologies Used
- Django
- Django REST Framework


## Contributors
- Amira Mahmoud Ahmed Nayel  (https://github.com/Amira-Nayel)
- Lobna Mohammed AbdElrazak Elnisr  (https://github.com/lobnaelnisr)
- Malak Tarek Muhammed Assem
- Salma Mohammed Abdelrahman Ebrahim


## you can access the rest of the project frome here:
[Frontend Repository](https://github.com/Amira-Nayel/frontend-insight-learn.git)

[Machine Learning Repository](https://github.com/Amira-Nayel/machine-learning-insight-learn.git)

[infrastructure as code Repository](https://github.com/Amira-Nayel/infrastructure-as-code-.git)

