# RandomBot

This repository is a sample Slackbot implemented in Python intended to be run
on DigitalOcean's App Platform. This slackbot listens to messages in channels
it is installed in an performs coin flips, dice rolls, or picking random cards
based on what it hears.

Functionality: 
* "flip a coin" - Will flip a coin
* "roll a die" - Will roll a traditional six sided die
* "roll a dX" - Will roll a X sided die. ex: roll a d20
* "pick a card" - Will pick a card from a standard deck of 52 cards.

To setup this slackbot and test it, you can use this tutorial on 
[Building a Slackbot in Python on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-build-a-slackbot-in-python-on-ubuntu-20-04). You won't be able to follow 
this tutorial word for word when it comes to deployment. But Setps 1, 4, and 5 
will walk you through how to setup and test your slackbot. The parts of the 
tutorial that deal with code have already been done and the code is stored
in this repository.


These following steps will get this sample application running for you using
DigitalOcean.

**Note: Following these steps will result in charges for the use of DigitalOcean services**

## Requirements

* You need a DigitalOcean account. If you don't already have one, you can sign up at https://cloud.digitalocean.com/registrations/new
* You need a Slack workspace that you have administrative access to and can install bots.

## The Process

1. Create your slackbot in the [Slack API](https://api.slack.com/apps). You can find instructions [here](https://www.digitalocean.com/community/tutorials/how-to-build-a-slackbot-in-python-on-ubuntu-20-04).
1. Create a folder for virtual environments if you don't already have one 
    1. `mkdir ~/.venvs`
1. Install a python virtual environment 
    1. `python -m venv ~/.venvs/slackbot`
1. Activate your python virtual environment
    1. `source ~/.venvs/slackbot/bin/activate`
1. Install the appropriate Slack and Flask packages
    1. `pip install slackclient slackeventsapi Flask`
1. Run `pip freeze > requirements.txt` so it can be uploaded to GitHub and installed
in App Platform
1. Write the code.
    1. See provided app.py & randombot.py
1. Create a new github repo and upload your code, requirements, and spec file
1. Enable GitHub access to the repository in the create new app workflow
1. Either deploy the bot as a python service
    1. Requeired ENV Vars:
        1. `SLACKBOT_TOKEN` - OAuth Access Token
        1. `SLACKBOT_EVENTS_TOKEN` - Signing Secret
    1. Run Command:
        1. `gunicorn --worker-tmp-dir /dev/shm app:app`
1. Or run `doctl apps create --spec spec.yaml`

## Deploying the App ##

1. Visit https://cloud.digitalocean.com/apps (if you're not logged in, you may see an error message. Visit https://cloud.digitalocean.com/login directly and authenticate, then try again)
1. Click "Launch App" or "Create App"
1. Choose GitHub and authenticate with your GitHub credentials.
1. Under Repository, choose this repository (e.g. `<your-org>/sample-python`)
1. On the next two screens, leave all the defaults unchanged.
1. Click "Launch App"
1. You should see a "Building..." progress indicator. And you can click "Deployments"→"Details" to see more details of the build.
1. It can currently take 5-6 minutes to build this app, so please be patient. Live build logs are coming soon to provide much more feedback during deployments.
1. Once the build completes successfully, click the "Live App" link in the header and you should see your running application in a new tab

## Making Changes to Your App ##

As long as you left the default Autodeploy option enabled when you first launched this app, you can now make code changes and see them automatically reflected in your live application. During these automatic deployments, your application will never pause or stop serving request because the App Platform offers zero-downtime deployments.

Here's an example code change you can make for this app:
1. Edit the necessary Python files to make this slackbot fit your needs.
1. Commit the change to master. Normally it's a better practice to create a new branch for your change and then merge that branch to master after review, but for this demo you can commit to master directly.
1. Visit https://cloud.digitalocean.com/apps and navigate to your sample-python app.
1. You should see a "Building..." progress indicator, just like above.
1. Once the build completes successfully, click the "Live App" link in the header and you should see your updated application running. You may need to force refresh the page in your browser (e.g. using Shift+Reload).

## Learn More ##

You can learn more about the App Platform and how to manage and update your application at https://www.digitalocean.com/docs/apps/.


## Deleting the App #

When you no longer need this sample application running live, you can delete it by following these steps:
1. Visit the Apps control panel at https://cloud.digitalocean.com/apps
1. Navigate to the sample-python app
1. Choose "Settings"->"Destroy"

This will delete the app and destroy any underlying DigitalOcean resources

**Note: If you don't delete your app, charges for the use of DigitalOcean services will continue to accrue.**
