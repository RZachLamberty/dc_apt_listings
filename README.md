# DC Apartment Listings
Inspired largely by the project hosted here, I walked through the process with a different town, to help out a friend. Along the way, I learned a bit about the awesome [scrapy](http://scrapy.org/) library, as well as [PostgreSQL](http://www.postgresql.org/). Hope you like what I've done! Plots on the way.

## Data Note:
The data in this repo was obtained via the command
```bash
wget http://ec2-54-235-58-226.compute-1.amazonaws.com/storage/f/2013-05-12T03%3A50%3A18.251Z/dcneighorhoodboundarieswapo.geojson
```
This geoJSON is courtesy of [OpenDC Data](http://www.opendatadc.org/dataset/neighborhood-boundaries-217-neighborhoods-washpost-justgrimes), so thanks to them!

## Setup Note:
The file `make_raw_data_table.sql` is a postgres statement to make the table which is then loaded via the web scraping tool

You will also need to download a couple of libraries. I set this up with Anaconda and it was super easy -- pip was a bit more of a headache and, as it often does, required quite a few apt-gets for various headers. I found it was only possible if the virtualenv I created was created with the  `--system-site-packages` flag; then `pip install -r requirements.pip.text` worked out okay. And then... `.so` linkage fail.

But seriously, just do the Anaconda thing already. Everybody's doing it

or even better
```bash
conda create -n new environment --file requirements.txt
source activate dcapa
```

## Fire it up!
Activate your venv from above, or in a plain old environment, execute
```bash
scrapy crawl aptspider
```
