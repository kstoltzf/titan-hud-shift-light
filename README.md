# titan-hud-shift-light
Code for running a shift light indicator with a Raspberry Pi in the TITAN HUD project 

# Building and Running with Docker

* Build the image: `docker build -t titan-hud-shift-light .`
* Run the container: `docker run --network titan-hud --privileged -d --name titan-hud-shift-light titan-hud-shift-light`

# Running Locally

* Clone the repository: `git clone https://github.com/ryzingTitan/titan-hud-shift-light.git`
* Navigate to the folder where the repository has been cloned: `cd titan-hud-shift-light`
* Install required packages: `pip3 install -r requirements.txt`
* Update the the RabbitMQ host in the config.ini file to be `localhost`
* Run the application: `python3 -m shift_light`
