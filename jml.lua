local function newstack()
	local contents = {}
	local self = {}
	function self:pop()
		local popped = contents[#contents]
		contents[#contents] = nil
		return popped
	end
	function self:push(what)
		table.insert(contents, what)
	end
	return self
end

function translate(jml)
	local html = ''
	local stack = newstack()
	local lines = jml:gmatch('[^\n]+')
	local indentation = 0
	for line in lines do
		local leading_whitespace, content = line:match('^(%s*)(.*)')
		local new_indentation = leading_whitespace:len()
		while new_indentation < indentation do
			html = html..'</'..stack:pop()..'>'
			indentation = indentation - 1
		end
		local tag, props = content:match('^@(%w+)%s*(.*)')
		if tag then
			html = html..'<'..tag
			for key, value in props:gmatch('(%w+)=([^,]+)') do
				html = html..' '..key..'='..value
			end
			html = html..'>'
			stack:push(tag)
			indentation = indentation + 1
		else
			html = html..content
		end
	end
	while indentation > 0 do
		html = html..'</'..stack:pop()..'>'
		indentation = indentation - 1
	end
	return html
end

local jml = [[
@title
	My Cool Webpage

@meta,charset='UTF-8'

@link,rel='stylesheet',href='style.css'

@header
	@nav
		@ul
			@li
				@a,href='index.html'
					Home
			@li
				@a,href='about.html'
					About
			@li
				@a,href='contact.html'
					Contact
@main
	@h1
		Welcome to my Cool Webpage
	@p
		Here you can find information about my interests and projects.
	@section
		@h2
			My Interests
		@ul
			@li
				Photography
			@li
				Travel
			@li
				Hiking
	@section
		@h2
			My Projects
		@ul
			@li
				@a,href='https://github.com/myusername/myproject'
					My Project on GitHub
			@li
				@a,href='https://myphotoblog.com'
					My Photo Blog
@footer
	@p
		Copyright © 2023 My Name
]]

--[[
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
]]

local html = translate(jml)
print(html)