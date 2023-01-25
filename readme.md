# jml
Jeff's Markup Language

```jml
@title My Cool Webpage

@meta,charset='utf8'

@link,rel='stylesheet',href='style.css'

@header @nav @ul
	@li @a,href='index.html' Home
	@li @a,href='about.html' About
	@li @a,href='contact.html' Contact

@main
	@h1 Welcome to my Cool Webpage
	@p Here you can find information about my interests and projects.

	@section
		@h2 My Interests
		@ul
			@li Photography
			@li Travel
			@li Hiking

	@section
		@h2 My Projects
		@ul
			@li @a,href='https://github.com/myusername/myproject' My Project on GitHub
			@li @a,href='https://myphotoblog.com' My Photo Blog

@footer @p Copyright © 2023 My Name
```
