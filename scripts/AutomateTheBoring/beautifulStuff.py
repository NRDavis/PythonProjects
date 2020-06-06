# webscraping with beautiful soup

import bs4
import requests

# https://quotes.freerealtime.com/
# https://quotes.freerealtime.com/quotes/COKE/Quote
res = requests.get('https://quotes.freerealtime.com/quotes/COKE/Quote')
res.raise_for_status()          # we throw an exeption if our page is note reached
soup = bs4.BeautifulSoup(res.text, 'html.parser')   # we signal to bs4 that we're looking to parse html
 
 # copy css path         
elems = soup.select('html.js.csstransforms.csstransforms3d.csstransitions body.html.not-front.not-logged-in.one-sidebar.sidebar-second.page-quotes.page-quotes-coke.page-quotes-coke-quote div#content.firstpage div.container div.row div.span9 div.region.region-content div#block-system-main.block.block-system div.content div#qmQuoteTable div.qmHeading div.cont div.qtool div.qmod-ui-tool.qmod-detailedquote div.qmod-quotehead div.qmod-block-wrapper.qmod-lang-en div.pure-g div.pure-u-1 div.qmod-head-left div.qmod-mkt-hours div.qmod-mkt-top span.qmod-last')

print(len(elems))