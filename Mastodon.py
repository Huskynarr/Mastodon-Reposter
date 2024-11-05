# import Mastodon.py - I installed via PyPI
from mastodon import Mastodon
#import sys tools
import sys
import time

mURL = "https://mastodonnetwork-url"
mTkn = "{secret token}"
mAccs = ["@xboxdev@toad.social", "@Official_GDC@peoplemaking.games", "@unrealengine@noc.social ","@xboxgamepass@mastodon.social","@Xbox@mastodon.social","@XboxDevMastodon@social.xboxdev.com"]

# Instantiate Mastodon API client
mastodon = Mastodon(
    access_token = mTkn,
    api_base_url = mURL
)

try:
    # Loop through each account in the list
    for mAcc in mAccs:
        # Look up the account you want to re-post
        account = mastodon.account_lookup(mAcc)

        # Fetch the list of statuses from the specified account
        statlist = mastodon.account_statuses(account['id'])

        # Iterate through the statuses and reblog and like each one
        for status in statlist:
            # Check if the status has already been reblogged (boosted)
            if not status['reblogged']:
                # Reblog the status
                mastodon.status_reblog(status['id'])
                print(f"Reblogged: {status['id']} - {status['content'][:30]}...")
            else:
                print(f"Already reblogged: {status['id']}")
            
            # Check if the status has already been favorited (liked)
            if not status['favourited']:
                # Like the status
                mastodon.status_favourite(status['id'])
                print(f"Liked: {status['id']} - {status['content'][:30]}...")
            else:
                print(f"Already liked: {status['id']}")
            
            # Pause for 2 seconds before the next action
            time.sleep(2)

except Exception as e:
    # Handle errors, e.g., invalid credentials, account not found, etc.
    print(f"Error: {e}")
    sys.exit(1)

print("Reblogging complete.")
