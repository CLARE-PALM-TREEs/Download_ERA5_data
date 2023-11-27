# Download_ERA5_data
A repository for code to download ERA5 data from the Copernicus data portal

***Instructions for setting up access through the cdsapi:***

1. Create a CDS account from https://cds.climate.copernicus.eu/user/register and log in
   
3. In your home directory on JASMIN, create a file called .cdsapirc by:

   `emacs .cdsapirc`

3. Add the lines below to your file:

    url: https://cds.climate.copernicus.eu/api/v2
    key: {uid}:{api-key}

4. Save the file (Ctrl-c then Ctrl-s), then exit (Ctrl-x then Ctrl-c)

5. Install the Climate Data Store api:
  
   `pip install cdsapi`

6. Load jaspy:
   
   `module load jaspy/3.7` 

7. Clone this repository in your code workspace location:

   `git clone https://github.com/CLARE-PALM-TREEs/Download_ERA5_data.git`
   
8. Move into the Download_ERA5_data directory and:
   
   a) Edit the script download_hourly_ERA5_data.py as desired for your needs
   
   b) Edit the batch script lotus_download_hourly_ERA5_data to email you when the script starts and finishes and to save a log file (make a directory called lotus_output in your home space to store the log files)
   
   c) Run the batch script:
   
   `sbatch lotus_download_hourly_ERA5_data`
