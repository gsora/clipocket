# `clipocket`: a nice CLI Pocket client!

#### Dependencies

 - `python3`
 - `python-requests`
 - `pyPocket` (already included)
 - `python-beautifulsoup4`
 - `w3m`

#### Changelog:
 - 0.1: basic functionality
 - 0.2: now displaying entry content with less and markdown
 - 0.3: now displaying content parsed by w3m, which is now a necessary dependency
#### Usage

The first thing you have to do is login to Pocket, and `clipocket` will guide you through the process: simlply execute it:
	
	$ python3 ./clipocket.py

After that, you're ready to rock!

	$ python3 ./clipocket.py --add URL	# add an url to your account
	$ python3 ./clipocket.py --reader	# read!

#### Is it complete/stable?

No it isn't.

By now you can add and read entries but pyPocket doesn't support delete/star/mark as read operation on items: I'm working on it, will take a few days though.

Sometimes the service I use to get a more easy-to-parse HTML (Readability) could go nuts, if you recive some kind of error related to 5xx category simply retry.
