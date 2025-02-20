# PR-Movie-Recommendation

This project is a movie recommendation system built using the Kaggle movie dataset. The application is built using Streamlit and deployed on AWS using Elastic Beanstalk, Docker. It recommends movies based on user input and leverages collaborative filtering and content-based recommendation techniques.

### Features
Movie Recommendations: Get movie suggestions based on your preferences and interests.
Collaborative Filtering: Uses data from other users' preferences to suggest similar movies.
Content-Based Filtering: Recommends movies based on the features of movies you like.
Interactive Interface: A simple, user-friendly interface built with Streamlit.

### Technologies Used
- Streamlit: For building the user interface and deploying the app.
- AWS Elastic Beanstalk: For deploying the application to the cloud.
- Docker: For containerizing the application.
- Kaggle Dataset: For movie data (such as movie titles, genres, ratings, etc.).

### Deployment
The application is deployed on AWS Elastic Beanstalk and is containerized using Docker. Here's a brief on how to run and deploy the project:

#### Prerequisites
- AWS account and access to Elastic Beanstalk and S3.
- Docker installed on your machine.
= Streamlit for app development.
- Kaggle dataset for movie data.
### Running Locally
Clone the repository:

git clone https://github.com/yourusername/PR-Movie-Recommendation.git
Install required dependencies:
pip install -r requirements.txt
Run the Streamlit app locally:
streamlit run app.py
The app should now be available at http://localhost:8501 in your browser.
### Deploying on AWS Elastic Beanstalk
- install the AWS Elastic Beanstalk CLI.
- Set up Docker for your project.
- Create a Dockerfile to containerize the app same as i created.
Deploy the app
Build and push the Docker image to a container registry
eb init -p docker pr-movie-recommendation
eb create pr-movie-recommendation-env
eb open
This will launch the app on an AWS-hosted environment.

### Usage
- Upon visiting the app, users will be prompted to enter their preferences or favorite movies.
- Based on the input, the recommendation system will suggest similar movies using the collaborative and content-based filtering models.



