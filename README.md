# Web-Scraping Project (Web Scraping Sam Altman’s Blog Posts)

This Python script scrapes blog posts from Sam Altman’s website and saves them locally. It’s a handy tool for archiving and reading his insightful content.


**Objectives**

Retrieve Relevant Blog Posts: The script allows you to input specific blog post titles (separated by commas). It then fetches the corresponding blog posts from Sam Altman’s blog.

Save Locally: The downloaded blog posts are saved as HTML files in a directory named after Sam Altman. You can easily access and read them offline.

Handle Errors Gracefully: The script handles errors such as invalid URLs or inaccessible web pages. It also provides a list of incorrect URLs for manual verification.


**How It Works**

-User Input: The script prompts you to enter the titles of Sam Altman’s blog posts. You can input multiple titles separated by commas.

-URL Generation: For each title, the script constructs a URL by converting the title to lowercase, replacing special characters, and joining it with the base blog URL.

-HTTP Requests: It sends HTTP requests to the generated URLs to retrieve the blog content. If successful, it saves the content as an HTML file.

-Error Handling: If an error occurs (e.g., invalid URL or inaccessible page), the script keeps track of the problematic URLs and continues with the next title.

-Fallback Search: For incorrect URLs, the script uses a web browser (in this case, Microsoft Edge) to search for the correct URL based on modified title keywords.

-Browser Automation: The script automates the browser to find the correct URL on Google search results. It then saves the corrected content as an HTML file.

-Usage
Install Dependencies: Make sure you have Python installed. Install the required packages using pip install requests selenium.

-Run the Script: Execute the Python script. It will prompt you for blog post titles.

-Check Output: Navigate to the specified directory (e.g., sam-altman) to find the downloaded HTML files.

**Notes:**
Adjust the directory name (sam-altman) and other settings as needed.
Ensure you have the Chrome WebDriver (for Selenium) installed and configured