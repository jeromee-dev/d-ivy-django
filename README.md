# DevSearch Application
## Summary
This is the DevSearch application that was developed alongside the videos from the Dennis Ivy course taught on [Udemy](https://www.udemy.com/course/python-django-2021-complete-course/?couponCode=LETSLEARNNOWPP).
I do not take credit for the code, I have made slight adjustments to it but I plan to make more adjustments and improve it in the future as a way to further my learning.

## How to run
This project has both a frontend and a backend component; the backend is what needs explaining.
In order to run this project you will need Python 3, I have also included a requirements.txt file so that you can install the require dependencies easily.


The steps to get this project running are the following:
1. Get this project downloaded loacally by using `git clone https://github.com/jeromee-dev/d-ivy-django.git`
2. Naviagte to the section for the Python/Django backend by navigating as such `cd devsearch`.
3. Create a virtual environment first so that we don't affect the global packages you have by running the command `python -m venv venv`
   * If you are on Windows run `venv\Scripts\activate`
   * If you are on Linux or Mac run `source ./venv/bin/activate`
4. Now you can install all the dependencies:
   * If you are on Windows run `py -m pip install -r "requirements.txt"`
   * If you are on Linux or Mac run `python3 -m pip3 install -r "requirements.txt"`
5. Once the dependancies are installed, you may run the webserver by invoking the Python interpreter on manage.py and then using runserver as the first argument to the manage.py as such:
`python manage.py runserver` after which you should be able to naviagte to `localhost:8000` in your favorite web browser.