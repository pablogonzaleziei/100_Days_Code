
##Generating dynamic content for the celebrity names
I'm using Python and the Flask web framework to randomly select two celebrity names from a list and insert them into the HTML page

##app.py 
This code defines a Flask route that selects two random celebrity names from a list and passes them as arguments to the render_template() function. The render_template() function renders an HTML template file (index.html) with the celebrity names inserted into the appropriate placeholders.

##index.html
The HTML template file includes placeholders for the celeb_left and celeb_right variables, which will be replaced with the actual celebrity names when the page is rendered.