# Quora App

## Project Overview

Welcome to the Django Quora App! This cutting-edge web application offers users an immersive Quora-like experience, enabling them to ask insightful questions, share expertise through answers, follow captivating topics, and connect with a community of knowledge enthusiasts. Crafted with the Django web framework, PostgreSQL database, Django REST Framework, and React for the frontend, the application sets the stage for an exceptional user journey.

## Features

**User Authentication:** Seamlessly register, log in, and log out with a user-friendly interface. The app also incorporates a secure password reset functionality for hassle-free account access.

**Ask and Answer Questions:** Dive into a world of curiosity where users can post intriguing questions and contribute compelling answers, fostering a collaborative and enriching learning environment.

**Voting System:** Express your sentiments on questions and answers through intuitive upvoting and downvoting features, allowing the community to spotlight valuable content.

**User Profiles:** Each user gets a personalized profile page, complete with a vibrant display of their activity and contributions, cultivating a sense of community within the platform.

**Search Functionality:** Easily discover questions or topics of interest using the visually appealing and efficient search feature, ensuring users can find the information they seek effortlessly.

**Categories and Tags:** Enhance organization by categorizing and tagging questions, providing users with a structured and visually appealing way to navigate through the wealth of content.

**Chatbox Functionality:** Engage with other users in real-time through the integrated chatbox feature, fostering collaboration and interaction within the community.

## Technologies Used

**Django:** Powering the application with a robust web framework that enables rapid development and clean, pragmatic design.

**Django REST Framework:** Integrating RESTful APIs seamlessly into the application, facilitating communication between the backend and frontend components. DRF offers a comprehensive toolkit for building Web APIs, ensuring flexibility and scalability in data handling.

**React:** Building the frontend user interface with React, a JavaScript library for building user interfaces. React allows for the creation of reusable UI components and provides a more dynamic and responsive user experience.

**Database:** PostgreSQL is the backbone for storing data, ensuring reliability, and scalability for a seamless user experience.

**Frontend Technologies:** Elevate the user interface with a blend of HTML, CSS, JavaScript, and Bootstrap, ensuring a visually stunning and responsive design.
Along with React and Tailwind.

**Dependency Management:** Utilize Pipenv to manage project dependencies, maintaining a consistent and efficient development environment.

**Deployment:** Simplify deployment with Docker, making it effortless to set up and run the application across diverse environments.

## Getting Started

### Prerequisites

1. [Python](https://www.python.org/) (version 3.10)
2. [Django](https://www.djangoproject.com/) (version 5.0)
3. [Django REST Framework](https://www.django-rest-framework.org/) (version 3.12)
4. [React](https://reactjs.org/) (version 17)
5. [Node.js](https://nodejs.org/) (version 14 or higher)
6. [npm](https://www.npmjs.com/) (typically comes with Node.js installation)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Muhammad-Sibtain-Asad/quora.git
   cd QUORA
   ```

2. Set up a virtual environment with Pipenv:

   ```bash
   pipenv install
   ```

3. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

4. Install project dependencies:

   ```bash
   pipenv install -r requirements.txt
   ```

5. Install frontend dependencies:

   ```bash
   cd quora-frontend/quora
   npm install
   ```

6. Build the React app:

   ```bash
   npm run build
   ```

7. Return to the project root directory:

   ```bash
   cd ..
   ```

8. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

9. Run the development server:

   ```bash
   python manage.py runserver
   ```

10. Access the application in your web browser at [http://localhost:8000/](http://localhost:8000/)

---
