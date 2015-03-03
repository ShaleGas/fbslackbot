# fbslackbot
A slack webhook based facebook bot: pulls messages from a feed and posts to slack

In a semi-working state.

1) Fill in your desired feed ID (be that group/page/person)
2) Fill in your API key
3) Fill in your Slack Webhook address
4) Run. 

Todo:

Expand the try/catch to cover all possible feed post types.
Refactor try/catch into a function.
Implement a system for post tracking and discovery (i.e know what posts have already 
been posted on slack and only post new posts)
Handling comments?
Generally prettify the slack output (perhaps facebook pictures as 'author_icon'?)



