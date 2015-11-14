# Newsletter Builder

When using Sendy and aws for sending newsletters we experienced big problems with the online editor. The responsive template got corrupted if to many drag and drops were performed and creating a simple newsletter took way to long.

This is a simple script that can accept a couple of basic tags in any combination in order to quickly create a newsletter. 

It will also automatically download the price and image for products in a webshop just facilited with the link to the product. This saves a lot of manual copy paste. If you use itemprop markup for the product name, price and image, this should work automatically.

Have a look at newsletter.html for an example of tags to use. 

Run the generator with:
python create_template.py

and the resulting responsive html template will end up in result_template.html containing some default images that can easily be replaced.

This is an afternoon hack to remove manual work when creating newsletter so there is a lot of room for improvement if anyone finds it useful.


