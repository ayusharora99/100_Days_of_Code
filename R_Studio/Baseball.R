devtools::install_github("BillPetti/baseballr")
install.packages('tidyverse')
library(tidyverse)
library(baseballr)

# Each pitch thrown to Carlos Correa during May 2017
Correa = scrape_statcast_savant(start_date = "2017-05-01", end_date = "2017-05-31", playerid = 621043, player_type = "batter")

# Location of batted balls : hc_x & hc_y
Correa %>%
  select(events, hc_x, hc_y) %>%
  head()

unique(Correa$type)

# subset all balls in play 
Correa_BIP = Correa %>%
  filter(type == 'X')

Correa_BIP %>%
  select(events, hc_x, hc_y) %>%
  head()

# draw baseball field on a blank ggplot2 canvas
spray_chart = function(...){
  ggplot(...) + 
    geom_curve(x = 33, xend = 223, y = -100, yend = -100, curvature = -0.65) +
    geom_segment(x = 128, xend = 33, y = -208, yend = -100) +
    geom_segment(x =  128, xend = 223, y = -208, yend = -100) + 
    geom_curve(x = 83, xend = 173, y = -155, yend = -156, curvature = -0.65, linetype = "dotted") +
    coord_fixed() +
    scale_x_continuous(NULL, limits = c(25,225)) + 
    scale_y_continuous(NULL, limits = c(-225,25))
}

spray_chart(Correa_BIP, aes(x = hc_x, y = -hc_y, color = events)) +
  geom_point() +
  scale_color_grey()


Yaz = scrape_statcast_savant(start_date = "2019/05/25", end_date = "2019/09/09", playerid = 573262,player_type = 'batter')

Yaz_BIP = Yaz %>%
  filter(type == 'X')

# discrete or hue
spray_chart(Yaz_BIP, aes(x = hc_x, y = -hc_y, color = events)) +
  geom_point() +
  scale_color_hue()

spray_chart(Yaz_BIP, aes(x = hc_x, y = -hc_y, color = events)) +
  geom_point() +
  scale_color_viridis_d()

# Acquiring a year's worth of Stacast Data 
install.packages('devtools')
devtools::install_github("beanumber/statcastr")
library(statcastr)
install.packages('dbplyr')
library(dbplyr)
library(DBI)
install.packages("RMySQL")
library(RMySQL)
install.packages("RSQLite")
library(RSQLite)

conn = dbConnect(MySQL(), dbname = "baseball", host = '127.0.0.1', user = "root", password = "Ananda2006!!", port = 3306)
class(conn)
sc = etl("statcastr", conn, dir = "~/dumps/statcastr")
sc %>%
  etl_extract(year = 2017, month = 3:10) %>%
  etl_transform() %>%
  etl_load(tablenames = "statcast")

sc_2017 = sc %>%
  tbl("statcast") %>%
  collect()
