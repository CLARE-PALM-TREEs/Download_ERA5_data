# Download_ERA5_data
A repository for code to download ERA5 data from the Copernicus data portal

***Instructions for setting up access through the cdsapi:***

1. Create a CDS account from https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5

2. If you are not already set up to use conda, download the miniconda installer: 
    
   `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
    
3. Create a base environment: 
    
   `bash Miniconda3-latest-Linux-x86_64.sh`
    
4. Activate the base environment: 
    
   `source ~/miniconda3/bin/activate`

5. Create a new conda environment called cds_download:
    
   `conda create --name cds_download --file cds_download.lock`

6. Add iris to the conda environment:
    
   `conda install -c conda-forge iris`

7. To run code when set up from the terminal:

   a) Activate the environment:
   
   `conda activate cds_download`

   b) Edit the script download_hourly_ERA5_data.py as desired for your needs

   c) Run the script
   
   `python download_hourly_ERA5_data.py`
