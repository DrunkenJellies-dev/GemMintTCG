
# PokeSmart

**Developer:** Callum Newman

![PokeSmart](readme_imgs/SiteScreenshots/Lightmode.png)

## Live Website

[Link to live website](https://pokesmart-e83201be2611.herokuapp.com/)

## Purpose of the Project

Welcome to PokéSmart!

At PokéSmart, we aim to be more than just a hub for Pokémon news - although of course, our updates are always hot off the press! - we’re the center of the Poké community! Improve your game, stay up-to-date with the latest trends, and reach out to share your thoughts with the community.

## Table of Contents

- [User Experience (UX)](#user-experience-ux)
- [Key Project Goals](#key-project-goals)
- [Target Audience](#target-audience)
- [User Requirements and Expectations](#user-requirements-and-expectations)
- [Epics and User Stories](#epics-and-user-stories)
- [Features](#features)
- [Design](#design)
- [Database Schema](#database-schema)
- [Technology Used](#technology-used)
- [Testing](#testing)
- [User Testing](#user-testing)
- [Responsiveness](#responsiveness)
- [Bugs](#bugs)
- [Deployment](#deployment)

## User Experience (UX)

- **Purpose:** Share and discuss Pokémon-related blog posts, interact with content through comments, and manage user profiles.
- **Features:** Viewing posts, commenting, user profiles, light and dark mode implementation and community engagement.

## Key Project Goals

1. **To Share Pokémon Content:** Provide a space for users to view and discuss Pokémon-related blog posts.
2. **To Build a Community:** Foster interaction through comments, likes, dislikes, and user profiles.
3. **To Encourage User Interaction:** Allow users to comment, like, dislike and share posts and view their own profiles.
4. **To Provide a User-Friendly Experience:** Ensure easy navigation and accessibility across devices.

## Target Audience

- **Pokémon Fans:** Individuals interested in Pokémon and related content.
- **Blog Readers:** Users looking for engaging Pokémon-related blog posts.
- **Community Members:** Users who want to interact and share their thoughts about Pokémon.

## User Requirements and Expectations

- **Content Access:** Users expect to view detailed blog posts about Pokémon.
- **Interactive Features:** Users want to comment, like and share posts and manage their profiles.
- **Community Engagement:** Users anticipate interacting with other fans and sharing their own content - collaboartion is fostered through contact forms.

## Features

#### Navigation Bar

![Navigation Bar](/readme_imgs/Features/NavigationBar.png)

#### Blog Card

![Blog Card](/readme_imgs/Features/BlogCard.png)

#### Comment Form

![Comment Form](/readme_imgs/Features/CommentForm.png)

#### Comment History

![Comment History](/readme_imgs/Features/CommentHistory.png)

#### Contact Us Form

![Contact Us Form](/readme_imgs/Features/ContactUsForm.png)

#### Footer

![Footer](/readme_imgs/Features/Footer.png)

#### Likes / Dislikes

![Likes and Dislikes](/readme_imgs/Features/LikeDislikeButtons.png)

#### Prev and Next Buttons

![Prev and Next Buttons](/readme_imgs/Features/PrevNextButtons.png)

#### Share Posts

![Share Posts](/readme_imgs/Features/SharePosts.png)

## Design

#### Colour Design

Use of vibrant colors related to Pokémon.
![Dark Mode](/readme_imgs/SiteScreenshots/DarkModePage1.png)
![Light Mode](/readme_imgs/SiteScreenshots/Lightmode.png)

#### About Page

![About Page](/readme_imgs/SiteScreenshots/AboutPage.png)

#### Blog Page

![Blog Page](/readme_imgs/SiteScreenshots/BlogPost.png)

#### Contact Us Page

![Contact Us Page](/readme_imgs/SiteScreenshots/ContactUsForm.png)

#### Second Page of Blogs

![SecondPageBlogs](/readme_imgs/SiteScreenshots/Page2.png)

#### Post Comment Section

![Post Comment Section](/readme_imgs/SiteScreenshots/PostCommentSection.png)

#### Profile Comment History

![Profile Comment History](/readme_imgs/SiteScreenshots/ProfileCommentHistory.png)

#### Signed In

![SignedIn](/readme_imgs/SiteScreenshots/SignedIn.png)

#### Sign In

![Sign In](/readme_imgs/SiteScreenshots/SignIn.png)

#### Sign Out

![Sign Out](/readme_imgs/SiteScreenshots/SignOut.png)

#### Sign Up Page

![Sign Up Page](/readme_imgs/SiteScreenshots/SignUpPage.png)

## Database Schema

#### About Content

![About Content](/readme_imgs/Admin/AboutContent.png)

#### Admin Home

![Admin Home](/readme_imgs/Admin/AdminHome.png)

#### Collaberation Requests

![Collaberation Requests](/readme_imgs/Admin/CollaberationReqests.png)

#### Comments

![Comments](/readme_imgs/Admin/Comments.png)

#### Posts

![Posts](/readme_imgs/Admin/Posts.png)

#### Recent Actions

![Recent Actions](/readme_imgs/Admin/RecentActions.png)

#### Users

![Users](/readme_imgs/Admin/Users.png)

## Testing:

### HTML Validation

All HTML pages were tested with the [W3C HTML Validator](https://validator.w3.org/).

#### HTML Result

| page  | validator                                                                                          | result |
| ----- | -------------------------------------------------------------------------------------------------- | ------ |
| Home  | <details><summary>Home Page</summary><img src="./readme_imgs/W3cHTML/HomePageW3C.png"></details>   | PASS   |
| About | <details><summary>About Page</summary><img src="./readme_imgs/W3cHTML/AboutPageW3C.png"></details> | PASS   |

### CSS Validation

Custom CSS was put through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

#### CSS Result

| page | validator                                                                                        | result |
| ---- | ------------------------------------------------------------------------------------------------ | ------ |
| Css  | <details><summary>style.css</summary><img src="./readme_imgs/W3cCss/CssValidator.png"></details> | PASS   |

### JS Validation

JavaScript code in the comment.js and image.js file was put through the [JSHint Validator](https://jshint.com/).

#### JS Result

The js code for all files passed.

| page            | validator                                                                                             | result |
| --------------- | ----------------------------------------------------------------------------------------------------- | ------ |
| Comment.js      | <details><summary>style.css</summary><img src="./readme_imgs/JsHint/CommentsJsHint.png"></details>    | PASS   |
| LikeDislikes.js | <details><summary>style.css</summary><img src="./readme_imgs/JsHint/LikeDislikeJsHint.png"></details> | PASS   |
| Social.js       | <details><summary>style.css</summary><img src="./readme_imgs/JsHint/SocialJsHint.png"></details>      | PASS   |
| Theme.js        | <details><summary>style.css</summary><img src="./readme_imgs/JsHint/ThemeJsHint.png"></details>       | PASS   |

### Python Validation

All python code was put through the [CI Python Linter](https://pep8ci.herokuapp.com/).

#### Python Result

| File             | Validator                                                                                               | Result |
| ---------------- | ------------------------------------------------------------------------------------------------------- | ------ |
| About admin      | <details><summary>About Models</summary><img src="./readme_imgs/Linter/AboutAdmin.png"></details>       | PASS   |
| About apps       | <details><summary>About Views</summary><img src="./readme_imgs/Linter/AboutApps.png"></details>         | PASS   |
| About model      | <details><summary>About Forms</summary><img src="./readme_imgs/Linter/AboutModels.png"></details>       | PASS   |
| About urls       | <details><summary>About urls</summary><img src="./readme_imgs/Linter/AboutUrls.png"></details>          | PASS   |
| About views      | <details><summary>About Admin</summary><img src="./readme_imgs/Linter/AboutViews.png"></details>        | PASS   |
| About forms      | <details><summary>Blog Models</summary><img src="./readme_imgs/Linter/AboutForms.png"></details>        | PASS   |
| About test_forms | <details><summary>Blog Views</summary><img src="./readme_imgs/Linter/AboutTest_Forms.png"></details>    | PASS   |
| About test_views | <details><summary>Blog Forms</summary><img src="./readme_imgs/Linter/AboutTest_Views.png"></details>    | PASS   |
| Blog Admin       | <details><summary>Blog urls</summary><img src="./readme_imgs/Linter/BlogAdmin.png"></details>           | PASS   |
| Blog Apps        | <details><summary>Blog Admin</summary><img src="./readme_imgs/Linter/BlogApps.png"></details>           | PASS   |
| Blog Forms       | <details><summary>Makeover Models</summary><img src="./readme_imgs/Linter/BlogForms.png"></details>     | PASS   |
| Blog Models      | <details><summary>Makeover Views</summary><img src="./readme_imgs/Linter/BlogModels.png"></details>     | PASS   |
| Blog test_forms  | <details><summary>Makeover Forms</summary><img src="./readme_imgs/Linter/BlogTest_Forms.png"></details> | PASS   |
| Blog test_views  | <details><summary>Makeover urls</summary><img src="./readme_imgs/Linter/BlogTest_Views.png"></details>  | PASS   |
| Blog urls        | <details><summary>Makeover Admin</summary><img src="./readme_imgs/Linter/BlogUrls.png"></details>       | PASS   |
| Blog view        | <details><summary>Settings</summary><img src="./readme_imgs/Linter/BlogViews.png"></details>            | PASS   |

## User Testing:

Functionality Testing: Ensured all features work as expected, including comment submissions, profile management, and content viewing.

## Responsiveness:

All pages on the website were tested for responsiveness across multiple devices. All pages display correctly on all devices tested.

## Devices used for testing, OS and Browsers:

- iPhone 12, 13, 14
- Latest and Legacy Android Smartphones: Test on devices from manufacturers Samsung, Google. This includes models running the latest OS versions Android 12 & 13.
- Latest and Legacy iOS Devices: Include the latest and legacy handsets by Apple, iPhone X, iPhone 12 Mini, iPhone 13 Pro, and iPhone 14 Plus. This ensures testing on the latest iOS versions like iOS 15 and 16.
- Windows OS, windows 10 and windows 11 devices were used to test the website
- Mac OS, Mac os was tested using a MacBook air.
- Chrome
- Firefox
- Safari
- Edge
- Opera

## User Testing:

### Notifications and feedback testing for comments on all pages

| Action                                     | Notifications and feedback for comments             | Does it work as expected? |
| ------------------------------------------ | --------------------------------------------------- | ------------------------- |
| Logged out and looking at comments         | It should say "log in to leave a comment"           | PASS                      |
| Submit a comment                           | Comment submitted and awaiting approval             | PASS                      |
| Delete a comment                           | Your comment has been deleted successfully!         | PASS                      |
| Edit a comment modal                       | User is able to edit the comment in the body        | PASS                      |
| Comment text in box on click of edit       | Targeted text appears in comment box                | PASS                      |
| When edit button is clicked                | The word submit changes to update                   | PASS                      |
| Change mind about editing, can click reset | Resets update back to submit and clears comment box | PASS                      |
| Edit a comment successfully                | Comment Updated! Notification appears               | PASS                      |

### Notifications and feedback testing for register, signin and signout

| Action   | Notifications and feedback for signin and out | Does it work as expected? |
| -------- | --------------------------------------------- | ------------------------- |
| signin   | Successfully signed in as username.           | PASS                      |
| signout  | You have signed out.                          | PASS                      |
| register | Successfully signed in as username.           | PASS                      |

### Notification and feedback testing for about page

| Action                     | Notifications and feedback for signin and out | Does it work as expected? |
| -------------------------- | --------------------------------------------- | ------------------------- |
| Navigation menu links work | Successfully navigated to desired page.       | PASS                      |
| Contact button clicked     | Navigate to Contact form                      | PASS                      |
| Contact form completed     | User receives a success message               | PASS                      |

### Notification and feedback testing for social media links

| Action                     | Notifications and feedback for signin and out          | Does it work as expected? |
| -------------------------- | ------------------------------------------------------ | ------------------------- |
| Social media links clicked | Successfully navigated to desired page in a new window | PASS                      |

### Notifications and feedback testing for admin panel

| Action                                       | Notifications and feedback for comments         | Does it work as expected? |
| -------------------------------------------- | ----------------------------------------------- | ------------------------- |
| When contact request is marked in admin      | The request was changed successfully.           | PASS                      |
| When a comment has been approved in admin    | The comment "Comment" was changed successfully. | PASS                      |
| When a comment is deleted by admin           | Successfully deleted 1 comment.                 | PASS                      |
| When more than 1 comment is deleted by admin | Successfully deleted 2 comments.                | PASS                      |

## Deployment:

### Pre deployment

- To ensure successful deployment with Heroku, it's good practice to make sure that the requirements.txt file is kept up to date so as that imported python modules are configured correctly.
- A Procfile is required to allow Heroku deployment to be configured to a gunicorn web app.
- In settings.py configure the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost'], make sure all static files and directories are configured correctly.
- All environment variables on the env.py which gitignored on the repo must be configured correctly with the database url and secret key.

### Deploying with heroku

After account setup, the steps were as follows:

1.  Create a New App on Heroku:
    - Log into your Heroku account.
    - Click on "Create new app" and provide a unique name for your app.
    - Choose the region for your app (e.g., Europe).
    - Click "Create app".
2.  Connect to GitHub:
    - In the deployment method section, select GitHub.
    - Search for your GitHub repository and click "Connect".
3.  Configure Deployment Settings:
    - Choose between manual or automatic deployment. For automatic deployment, ensure the main branch is selected.
    - In the settings tab, reveal config vars and input the required hidden variables.
4.  Set Buildpacks:
    - Go to the settings tab and select "Buildpacks".
    - Add Node.js and Python as the buildpacks for your application.
5.  Deploy Your App: - Click "Deploy" to start the deployment process. - After the first deployment, you will receive a message indicating that your app was successfully deployed. - Use the "View" button to access your deployed application.
    This process leverages Heroku's integration with GitHub to automate the deployment of your application, making it easier to manage and update your project.

The live link for this project can be found here - [PokeSmart](https://pokesmart-e83201be2611.herokuapp.com/)

## Credits

### Code

[CI walkthrough I think therefore I blog](https://github.com/Code-Institute-Solutions/blog/tree/main/12_views_part_3/05_edit_delete) - The CI walkthrough repo was relied upon for the comment section, edit and delete button however I created custom models to suit the theme of the website.

## Technology Used

- **Languages and Frameworks:**
  - HTML5 for content and structure.
  - CSS for styling.
  - JavaScript for dynamic interactions.
  - Django for backend development.
- **Database:**
  - PostgreSQL for data storage.
- **Tools and Services:**
  - GitHub for version control and repository management.
  - Heroku for deployment.

### Technologies and tools:

- [GitHub](https://github.com/ "link to github webpage") was used to store the code files, README files and assets
- [Git](https://git-scm.com/ "link to official git website") was used as a version control software to commit and push the code to the GitHub repository
- [Heroku](https://id.heroku.com/login "link to Heroku login") was used to deploy the project
- [lucidcharts](https://www.lucidchart.com/pages/ "Link to lucidcharts") was used to make a diagram of the database schema and entity relationship diagrams.
- [Prettier](https://prettier.io/ "link to official prettier website") was used as the default formatter in Gitpod IDE, for html and css files.
- [Bootstrap](https://getbootstrap.com/ "link to official bootstrap website") was used to quickly layout, position and size critical website features
- [Google Fonts](https://fonts.google.com/ "link to official google fonts website") was used to import fonts
- [Font Awesome](https://fontawesome.com/ "link to official font awesome website") was used for all icons
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/ "Link to official chrome developer tools website") was used for lighthouse testing, debugging and consistently checking responsiveness
- [SourceTree](https://www.sourcetreeapp.com/ "Link to Official Sourcetree Website") was used instead of git terminal
- [W3C Markup Validator](https://validator.w3.org/ "link to official html validator") was used to validate all live html
- [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/ "link to official css validator") was used to validate CSS code
- [JS Hint](https://jshint.com/ "link to official javascript validator") was used to validate JavaScript code
- [Code Institute Python Linter](https://pep8ci.herokuapp.com/ "link to official python validator") was used to validate all python code
- [Django Summernote](https://pypi.org/project/django-summernote/ "link to official summernote website") was used. This is a rich text editor plugin for Django
- [Django Crispy Forms](https://pypi.org/project/django-crispy-forms/ "link to official crispy forms website") were used throughout the project to quickly create forms

---
