### CATALOG PAGE SCRAPE ELEMENTS
- ITRM: product-box
- TITLE: h3.prod-title > a
- LINK: h3.prod-title > a.href
- ORGANIZATON: .moreinfo > a.cur
- SKU: .descriptiontext > TEXT
- DETAILS: .specs > .data-row > (.attribute + .value)
- PAGINATION: ul#pagingDiv 
- PAGINATION NUMBER BUTTON: ul#pagingDiv > li.page-item > a.page-link
- IMAGE: a.imagelink


### SPECIFIC ITEM SCRAPE ELEMENTS 
TITLE: `#ContentPlaceHolder1_lblPartDisplayName`
SKU: `i.d-block detail > p > strong`
ITEM TYPE: `span#ContentPlaceHolder1_lblNodeDisplayName`
ORGANIZATION: `a#hlnkManuDisplayName`
IMAGE: `img#ContentPlaceHolder1_imgPartImage`
DESCRIPTION: `span#ContentPlaceHolder1_lblPartDescription > p`
URL: `URL`
PRODUCT SPECIFCATIONS: `.specs`
- PRODUCT DETAILS
- GENERAL PARAMETERS
TECHNICAL DATASHEET URL: `.spec-container ds-action-container`
