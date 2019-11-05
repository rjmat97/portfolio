import urllib.request as urln
from PIL import Image


urls = ["https://farm8.staticflickr.com/7804/32768627628_5545a43ab1_z.jpg",
"https://farm8.staticflickr.com/7857/45918551154_480cd86deb_z.jpg",
"https://farm5.staticflickr.com/4882/45779369454_b042e316ed_z.jpg",
"https://farm5.staticflickr.com/4915/45779362784_97dd8b55d9_z.jpg",
"https://farm5.staticflickr.com/4849/31563039527_56aa3bf518_z.jpg",
"https://farm8.staticflickr.com/7807/46502846821_7fe1c1b01f_z.jpg",
"https://farm5.staticflickr.com/4811/31563019537_f0df0600b7_z.jpg",
"https://farm8.staticflickr.com/7850/45779343594_77bb8daede_z.jpg",
"https://farm5.staticflickr.com/4876/32380615918_d7a1614774_z.jpg",
"https://farm8.staticflickr.com/7918/46502819841_a217c288ce_z.jpg",
"https://farm5.staticflickr.com/4896/31562987347_37bc22289f_z.jpg",
"https://farm5.staticflickr.com/4815/32373269668_1e2bd8b53e_z.jpg",
"https://farm8.staticflickr.com/7838/31562955117_15771a13c6_z.jpg",
"https://farm8.staticflickr.com/7844/46502790541_53b76dd0cb_z.jpg",
"https://farm5.staticflickr.com/4883/46502820221_99a4116d96_z.jpg",
"https://farm1.staticflickr.com/863/39357377490_5c439157e6_z.jpg",
"https://farm2.staticflickr.com/1916/46194977112_d39e9cf0a6_z.jpg",
"https://farm1.staticflickr.com/942/43856736271_53a2d2d931_z.jpg",
"https://farm1.staticflickr.com/905/28126139098_6433463ce1_z.jpg",
"https://farm1.staticflickr.com/807/41166963371_9598a2d04f_z.jpg",
"https://farm1.staticflickr.com/888/41122587242_38d6496e5e_z.jpg",
"https://farm1.staticflickr.com/894/26216528257_0c5120b91e_z.jpg",
"https://farm1.staticflickr.com/881/39278902410_9553ae4885_z.jpg",
"https://farm1.staticflickr.com/813/40193837415_10dbbd82b5_z.jpg",
"https://farm1.staticflickr.com/794/40193836705_fd424f9b87_z.jpg",
"https://farm5.staticflickr.com/4678/25183742877_7fd6812ddb_z.jpg",
"https://farm5.staticflickr.com/4710/39765339512_906f32e2a5_z.jpg",
"https://farm5.staticflickr.com/4626/39087093394_25c1001eed_z.jpg"]


for i in range(len(urls)):
    print("progress: " + str(i) + " of " + str(len(urls)))
    name = str(i)+'.jpg'
    urln.urlretrieve(urls[i], name)
    image = Image.open(name) 
    # image = image.resize((256, 256), Image.ANTIALIAS) # Resize the image and overwrite it
    image.save(name)
    