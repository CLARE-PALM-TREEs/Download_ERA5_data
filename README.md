# Download_ERA5_data
A repository for code to download ERA5 data from the Copernicus data portal

***Instructions for setting up access through the cdsapi:***

1. Create a CDS account from https://cds.climate.copernicus.eu/user/register and log in
   
3. In your home directory on JASMIN, create a file called .cdsapirc by emacs or vi:

   `emacs .cdsapirc`

   or

   `vi .cdsapirc`

3. Add the lines below to your file (for vi press i first to allow text insert, add the text, and then Esc key to stop editing):

    url: https://cds.climate.copernicus.eu/api/v2
    key: {uid}:{api-key}

4. Save the file Emacs: (Ctrl-c then Ctrl-s), then exit (Ctrl-x then Ctrl-c), vi: Make sure Esc has been pressed, then type :wq

5. Install the Climate Data Store api:
  
   `pip install cdsapi`

6. Clone this repository in your code workspace location:

   `git clone https://github.com/CLARE-PALM-TREEs/Download_ERA5_data.git`
   
7. Move into the Download_ERA5_data directory and:
   
   a) Edit the script **download_hourly_ERA5_data.py** as desired for your needs
   
   b) Edit the batch script **lotus_download_hourly_ERA5_data** to email you when the script starts and finishes and to save a log file (make a directory called lotus_output in your home space to store the log files)
   
   c) Run the batch script:
   
   `sbatch lotus_download_hourly_ERA5_data`
