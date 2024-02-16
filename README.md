# Web Scraper (Project 1)

My name is Austin Morris and this is my submission for Project 1 in CS325 (taught by: Dr. Manas Das)

This project contains a web scraper, software used to gather information online, and lets the user extract information from URL's in "URLs.txt" to files of their own.

In demonstration, I have included the 5 files that contain article information after using this software.

_I may have not gotten the formatting of the files to look gorgeous, but hey! It does what it's supposed to do._

**ARE YOU READY TO RUMBLE?!**

<details><summary> Your answer:</summary>
  <pre>
  Dude... it's just a web scraper. What are you talking about?
  </pre>
  </details>


## Environment Requirements (Conda)

In terms of our environment, there are a few requirements that we will need in order for this software to work properly.

As a base, the required environment was created with python 3.9 through Conda.

If you require help with the creation of the environment, I have included the command to help:
<details><summary>Solution:</summary>
  <pre>
    conda create --name Project1Env python=3.9
  </pre>
</details>

While researching for this project, I happened to come across a couple packages that will allow us to meet the criteria for this project.

    Side Note: Please do not forget to set-up your environment, as this software WILL NOT work without the proper components.


Please be aware that, although I am going to cover the requirements here, all requirements are listed within "requirements.yml".

1. requests
    * This is a package that will allow us to make HTTP requests in python through our software.
    * You can choose to install this through conda or terminal on VSC (I personally chose to install this through conda).
    * <details><summary>Solution:</summary>
        <pre>
            pip install requests
        </pre>
      </details>

2. beautifulsoup4
    * This is a package that will allow us to parse HTML or XML using python.
    * I attempted to install this package through Conda as well, but for some reason it would not recognize the module 'bs4' as we import the package.
        * To fix this, I used the install command inside VSC's terminal instead (it was also installed through Conda, seeing as that is what I attempted first).
    * <details><summary>Solution:</summary>
        <pre>
            pip install beautifulsoup4
        </pre>
      </details>

If you are looking to import this enviroment, you will need an extra step.

To import this environment from the file included on this repo, you will need to enter the following command line into your Conda terminal after obtaining the "requirements.yml" file:

* conda create --name your_desired_filename --file requirements.yml


As I said, there are only a few required packages to deal with - thats all of them!

Now that we have set up our environment, let's check into the program side of this project.


## Software / Programming

In this section, I will cover how to use the software. This part is somewhat self explanatory, but we wouldn't want anyone to get lost!

Before that, I would like to highlight the imported libraries used:

1. urlparse
    * This is a library imported in order to help us automate naming files containing the newly obtained information.
    * The URL is parsed in order to collect the title of the article, as well as eliminate the usage of certain characters.
    * This can be done by utilizing the following code:
        * `from urllib.parse import urlparse`

2. os
    * This is a library imported in order for us to provide a portable way of using system-dependent functionality (i.e. the environment).
    * This can be done by utilizing the following code:
        * `import os`

Now that we've gone over that, we can get into how this software works.

As stated previously, this software is a web scraper. This means that the software covered in this README file will collect information from the websites given in "URLs.txt" (THROUGH the url) and place the gathered information into a file that is named based on the url.

**These are the steps in which the software takes to carry out this process:**

1. A varible is set to the name of the file including the urls in order to pass the file name as an argument.
2. If the path of the file name exists, the software will then start reading the urls.
3. The function "download_and_extract" is then called to parse the URLS while in a loop to iterate through each URL present.
4. While inside this function, the software utilizes requests to send a GET request to the url.
5. The software will then check to see if the request was successful or not. If so, beautifulsoup is then used to parse the HTML content of the web page.
6. Next, a file is created with a name based on the url.
7. The information obtained from the article is then stored within it's respective file.
8. Loop until there are no more urls.

Running the software is an even easier ask, as once you've ensured that your environment is correct (whether that be through Conda or the VSC terminal) you can simply run the program! 

Once again, **YOU MUST ENSURE THAT YOUR ENVIRONMENT IS CORRECTLY SET UP WITH THE CORRECT PACKAGE OR THE SOFTWARE WILL NOT WORK**.

As long as that's not an issue, then everything seems to be all caught up!

I hope this README file has helped you understand the environment, why we need the enivonment to be a specifc way, the software, and how the software is used. Thank you for taking the time to follow along!

    Please note that the information inside of each of the scraped files is pretty far down in the file. I am not sure why it did this.