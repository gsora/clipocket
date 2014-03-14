# README about `clipocket` development

#### What we know

 - we have a Pocket library
 - we want to use it in a production environment
 - this will be a *read-only* client by now, but options will come soon
 - we have to use things like Instapaper in order to retrieve an already-formatted easy-to-use HTML file
 - we MUST implement a CLI-into-CLI work flow (i.e. there will be a set of clipocket commands)
 
#### Usage flow

  
	1) extended title
	2) extended title
	...
	42) extended title
	clipocket> read 42
	
	**At this point, the Instapaper HTML will be parsed, formatted and displayed into man**
	**When the user exit from the page, a menu will ask what to do with the link**
	
	(A)rchive, (D)elete, (S)tar:
	
	**Now print the links list again**

The formatted pages will be saved as /tmp files, ready to be dumped on the next reboot.

## man pages on steroids
Why reinvent the wheel?
We have man pages!

#### The style we'll use

	.TH "Pocket link" 12/34/5678
	
	.SH "Article title goes here"
	
	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ultricies cursus erat, eu fringilla elit malesuada elementum. Donec rhoncus quis dui eget volutpat. Aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce laoreet fringilla interdum. Sed tortor diam, dapibus vitae nisi ut, congue fringilla est. Interdum et malesuada fames ac ante ipsum primis in faucibus. In ac purus sed eros molestie porta vitae eu lectus. Pellentesque aliquam egestas diam a euismod. Aliquam ac enim quam. Nunc nec tortor erat. Vivamus pretium suscipit nunc.

	Quisque ultrices pharetra ipsum. Mauris hendrerit risus at dui luctus, sit amet commodo augue gravida. Morbi molestie mattis leo, ac aliquet nulla ullamcorper id. Phasellus consectetur ante turpis, eget ultricies est auctor at. Quisque sed ante a metus faucibus accumsan. Quisque non erat et tellus ullamcorper mollis sit amet quis ipsum. Sed fermentum felis enim, eu venenatis sem gravida nec. Vestibulum non ipsum nulla. Etiam sed elementum risus. Suspendisse potenti. Praesent id semper justo.

	Sed lobortis elit et eros pharetra luctus. In mollis massa a enim pharetra tempor. Fusce porta turpis a enim volutpat dictum quis vitae neque. Morbi pulvinar, enim vel dapibus auctor, diam urna venenatis libero, nec vulputate nulla nulla fringilla lorem. Cras pulvinar dapibus enim, a egestas dui cursus nec. Fusce feugiat porttitor tortor a porttitor. Cras lobortis pharetra lorem pharetra porttitor. 
	
	.SH "Original Link"
	
	http://it.lipsum.com/feed/html


Refer to `man groff` to know more about the bold and italic thing

#### File generation and display method
As far as I can understand, **groff >>>>> troff** (thanks, RMS).
This said, the correct procedure to create and display a custom man page without any escape character hassle is:

	# edit your file with the style said before (calling this yourFile now)
	groff -Tascii -man yourFile > yourFile.1
	gzip yourFile.1
	man ./yourFile.gz
	
*BOOM*, man file bitches.