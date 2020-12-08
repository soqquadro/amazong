# amazong

a basic scraper for the inventory status of products on Amazon FR <br /> 

#### Installation and Requirements

_to install from requirements file from the path where reqs.txt is located_ <br /> 
pip3 install -r reqs.txt 

_get the latest chrome driver_ [here](https://sites.google.com/a/chromium.org/chromedriver/) <br />

__[enabling chromedriver on mac os]__

_to add chromdriver path to PATH_ <br /> 
sudo nano /etc/paths

_to enable chromedriver from the path where chrome driver is located_ <br /> 
xattr -d com.apple.quarantine chromedriver 

Control-x to quit <br /> 
Y to save <br /> 

#### About Inputs and Outputs

Input has to be a text file(s) containing a list of ASIN codes, the output generated will be a formatted XLSX file(s).
